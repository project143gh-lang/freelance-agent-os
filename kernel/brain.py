import requests
import json
import yaml
import os

class LocalBrain:
    def __init__(self, config_path="C:/Users/ADMIN/FreelanceOS/config.yaml"):
        self.config_path = config_path
        self._load_config()

    def _load_config(self):
        with open(self.config_path, 'r') as f:
            self.config = yaml.safe_load(f)
        self.model = self.config['model']
        self.url = self.config['ollama_url']
        self.system_prompt = self.config['system_prompt']

    def update_model(self, new_model):
        self.model = new_model
        # Update config file permanently
        self.config['model'] = new_model
        with open(self.config_path, 'w') as f:
            yaml.dump(self.config, f)
        return f"Brain updated to model: {new_model}"

    def get_status(self):
        """Check if the local Ollama instance is healthy."""
        try:
            # Ollama tags endpoint returns available models
            response = requests.get(f"{self.url.replace('/api/generate', '/api/tags')}", timeout=2)
            if response.status_code == 200:
                models = [m['name'] for m in response.json().get('models', [])]
                return {
                    "status": "Online",
                    "current_model": self.model,
                    "available_models": models,
                    "endpoint": self.url
                }
        except Exception as e:
            return {"status": "Offline", "error": str(e)}

    def chat(self, prompt, context=""):
        full_prompt = f"{self.system_prompt}\n\nContext: {context}\n\nUser: {prompt}\n\nBrain:"
        
        payload = {
            "model": self.model,
            "prompt": full_prompt,
            "stream": False,
            "options": {
                "temperature": 0.2,
                "num_ctx": 4096
            }
        }
        
        try:
            response = requests.post(self.url, json=payload)
            response.raise_for_status()
            return response.json().get('response', '')
        except Exception as e:
            return f"Error connecting to Local Brain: {str(e)}"
