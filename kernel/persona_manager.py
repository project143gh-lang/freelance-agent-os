import yaml
import os

class PersonaManager:
    def __init__(self, personas_dir="C:/Users/ADMIN/FreelanceOS/personas"):
        self.personas_dir = personas_dir
        self.personas = self._load_personas()
        self.current_persona = "default"

    def _load_personas(self):
        personas = {}
        for filename in os.listdir(self.personas_dir):
            if filename.endswith(".yaml"):
                with open(os.path.join(self.personas_dir, filename), 'r') as f:
                    data = yaml.safe_load(f)
                    personas[data['name'].lower().replace(" ", "_")] = data
        return personas

    def get_modifier(self, persona_name):
        name = persona_name.lower().replace(" ", "_")
        if name in self.personas:
            self.current_persona = name
            return self.personas[name]['system_modifier']
        return ""

    def list_personas(self):
        return list(self.personas.keys())
