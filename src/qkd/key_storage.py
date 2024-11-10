# src/qkd/key_storage.py

import logging
import json
import os
from cryptography.fernet import Fernet

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class KeyStorage:
    def __init__(self, storage_file='keys.json', encryption_key=None):
        """Initialize the Key Storage with a specified file and optional encryption key."""
        self.storage_file = storage_file
        self.encryption_key = encryption_key or Fernet.generate_key()
        self.cipher = Fernet(self.encryption_key)
        self.keys = self.load_keys()

    def load_keys(self):
        """Load keys from the storage file."""
        if os.path.exists(self.storage_file):
            with open(self.storage_file, 'rb') as file:
                encrypted_data = file.read()
                decrypted_data = self.cipher.decrypt(encrypted_data)
                return json.loads(decrypted_data)
        return {}

    def save_keys(self):
        """Save keys to the storage file."""
        with open(self.storage_file, 'wb') as file:
            encrypted_data = self.cipher.encrypt(json.dumps(self.keys).encode())
            file.write(encrypted_data)
        logging.info(f"Keys saved to {self.storage_file}.")

    def add_key(self, key_id, key):
        """Add a new key to the storage."""
        self.keys[key_id] = key
        self.save_keys()
        logging.info(f"Key with ID '{key_id}' added.")

    def get_key(self, key_id):
        """Retrieve a key by its ID."""
        key = self.keys.get(key_id)
        if key is not None:
            logging.info(f"Key with ID '{key_id}' retrieved.")
        else:
            logging.warning(f"Key with ID '{key_id}' not found.")
        return key

    def delete_key(self, key_id):
        """Delete a key from the storage."""
        if key_id in self.keys:
            del self.keys[key_id]
            self.save_keys()
            logging.info(f"Key with ID '{key_id}' deleted.")
        else:
            logging.warning(f"Key with ID '{key_id}' not found. Cannot delete.")

    def list_keys(self):
        """List all stored keys."""
        logging.info(f"Stored keys: {list(self.keys.keys())}")
        return list(self.keys.keys())

    def get_encryption_key(self):
        """Return the encryption key used for storage."""
        return self.encryption_key
