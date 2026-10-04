import re
import yaml
import os
import importlib
from kernel.brain import LocalBrain
from memory.store import NormalizedStore
from kernel.persona_manager import PersonaManager

class FreelanceKernel:
    def __init__(self):
        self.brain = LocalBrain()
        self.memory = NormalizedStore()
        self.persona_mgr = PersonaManager()
        self.services = {}
        self.skills = {}
        self._load_services()
        self._load_skills()
        self._inject_tool_list()

    def _load_services(self):
        services_dir = "C:/Users/ADMIN/FreelanceOS/services"
        if not os.path.exists(services_dir): return
        for filename in os.listdir(services_dir):
            if filename.endswith(".py") and filename != "__init__.py":
                module_name = f"services.{filename[:-3]}"
                module = importlib.import_module(module_name)
                for attr_name in dir(module):
                    attr = getattr(module, attr_name)
                    if isinstance(attr, type) and attr_name.endswith("Service"):
                        service_instance = attr()
                        self.services[service_instance.name] = service_instance
                        print(f"[Kernel] Loaded Service: {service_instance.name}")

    def _validate_args(self, action_path, args):
        """Security layer to prevent command injection and malicious inputs."""
        forbidden_patterns = [';', '&&', '||', '`', '$(', '>', '<', '|']
        if any(pattern in args for pattern in forbidden_patterns):
            print(f"[SECURITY ALERT] Blocked potentially malicious arguments in {action_path}: {args}")
            return False
        return True

    def _load_skills(self):
        skills_dir = "C:/Users/ADMIN/FreelanceOS/skills"
        if not os.path.exists(skills_dir): return
        for filename in os.listdir(skills_dir):
            if filename.endswith(".py"):
                module_name = f"skills.{filename[:-3]}"
                module = importlib.import_module(module_name)
                for attr_name in dir(module):
                    attr = getattr(module, attr_name)
                    if isinstance(attr, type) and hasattr(attr, 'execute') and not attr.__name__.endswith('Service'):
                        try:
                            skill_instance = attr()
                            self.skills[skill_instance.name] = skill_instance
                            print(f"[Kernel] Loaded Agentic Skill: {skill_instance.name}")
                        except:
                            continue

    def _inject_tool_list(self):
        service_list = ", ".join(self.services.keys())
        skill_list = ", ".join(self.skills.keys())
        tool_guidance = (
            f"\n\nSTRICT TOOLSET:\n"
            f"CORE SKILLS: [{skill_list}]\n"
            f"SYSTEM SERVICES: [{service_list}]\n"
            f"RULE: You MUST use a tool from this list. Do not invent tool names. "
            f"To search the web, use 'web_search(query)'. To extract data, use 'client_extractor(url)'."
        )
        self.brain.system_prompt += tool_guidance

    def switch_persona(self, persona_name):
        modifier = self.persona_mgr.get_modifier(persona_name)
        if modifier:
            self.brain.system_prompt += f"\n\n{modifier}"
            return f"Persona switched to {persona_name}."
        return f"Persona {persona_name} not found."

    def run(self, user_input, session_id="default"):
        if user_input.startswith("/persona"):
            name = user_input.replace("/persona ", "").strip()
            return self.switch_persona(name)
        
        if user_input.startswith("/set-model"):
            model = user_input.replace("/set-model ", "").strip()
            return self.brain.update_model(model)
            
        if user_input == "/brain-status":
            status = self.brain.get_status()
            return f"Brain Status: {status['status']} | Model: {status.get('current_model')} | Available: {status.get('available_models', [])}"

        # MODE DETECTION: Normal vs System
        system_keywords = ["system", "os", "kernel", "execute", "run tool", "agent", "brain"]
        is_system_mode = any(kw in user_input.lower() for kw in system_keywords) or any(tool in user_input for tool in self.services.keys())

        if not is_system_mode:
            # NORMAL MODE: Direct conversational response
            # We bypass the agentic loop for a more natural flow
            response = self.brain.chat(user_input, context=str(self.memory.get_session(session_id)))
            # Clean up any accidental THOUGHT/ACTION markers if the brain still uses them
            clean_response = re.sub(r"(THOUGHT:|ACTION:|FINAL_ANSWER:)", "", response).strip()
            return clean_response

        # SYSTEM MODE: Agentic Tool-Calling Loop
        context = self.memory.get_session(session_id)
        current_prompt = user_input
        iteration = 0
        max_iterations = 7

        print(f"\n[Kernel] SYSTEM MODE active: Processing request: {user_input}")

        while iteration < max_iterations:
            iteration += 1
            response = self.brain.chat(current_prompt, context=str(context))
            
            if "OBSERVATION:" in response and "ACTION:" in response:
                response = response.split("OBSERVATION:")[0]
            
            print(f"\n--- Iteration {iteration} ---")
            print(response)

            action_match = re.search(r"ACTION:\s*([\w_.]+)\((.*)\)", response)
            final_match = re.search(r"FINAL_ANSWER:\s*(.*)", response, re.DOTALL)

            if final_match:
                return final_match.group(1).strip()

            if action_match:
                action_path = action_match.group(1)
                args = action_match.group(2).strip('"\'')

                if action_path in self.skills:
                    if not self._validate_args(action_path, args):
                        current_prompt = f"OBSERVATION: Security violation detected in arguments. Action blocked."
                        continue
                    print(f"[Kernel] Executing Skill: {action_path}({args})")
                    observation = self.skills[action_path].execute(args)
                    current_prompt = f"OBSERVATION: {observation}\nContinue based on this."
                    self.memory.update_session(session_id, f"step_{iteration}", {"action": action_path, "result": observation})
                    continue

                if "." in action_path:
                    service_name, method_name = action_path.split(".")
                else:
                    service_name, method_name = action_path, "execute"

                if service_name in self.services:
                    if not self._validate_args(action_path, args):
                        current_prompt = f"OBSERVATION: Security violation detected in arguments. Action blocked."
                        continue
                    service = self.services[service_name]
                    method = getattr(service, method_name, service.execute)
                    print(f"[Kernel] Executing {action_path}({args})")
                    try:
                        observation = method(args)
                    except Exception as e:
                        observation = f"Error executing {action_path}: {str(e)}"
                    current_prompt = f"OBSERVATION: {observation}\nContinue based on this."
                    self.memory.update_session(session_id, f"step_{iteration}", {"action": action_path, "result": observation})
                else:
                    available = list(self.skills.keys()) + list(self.services.keys())
                    current_prompt = f"OBSERVATION: Tool '{action_path}' does not exist. You MUST use one of these: {available}. Please try again."
            else:
                return "The Brain failed to provide a valid action or final answer."

        return "Max iterations reached without final answer."
