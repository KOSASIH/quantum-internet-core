# utils/config.py

import json
import os

class Config:
    def __init__(self, config_file='config.json'):
        """Load configuration from a JSON file."""
        self.config_file = config_file
        self.config_data = self.load_config()

    def load_config(self):
        """Load configuration data from the specified JSON file."""
        if os.path.exists(self.config_file):
            with open(self.config_file, 'r') as file:
                return json.load(file)
        else:
            raise FileNotFoundError(f"Configuration file '{self.config_file}' not found.")

    def get(self, key, default=None):
        """Get a configuration value by key, with an optional default."""
        return self.config_data.get(key, default)

    def set(self, key, value):
        """Set a configuration value by key."""
        self.config_data[key] = value
        self.save_config()

    def save_config(self):
        """Save the current configuration data back to the JSON file."""
        with open(self.config_file, 'w') as file:
            json.dump(self.config_data, file, indent=4)
