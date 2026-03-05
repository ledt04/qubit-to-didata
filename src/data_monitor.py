import os
from pathlib import Path

class DataMonitor:
    def __init__(self, file_path):
        self.file_path = file_path

    def check_file_exists(self):
        if not os.path.exists(self.file_path):
            print(f"File not found: {self.file_path}")
            return None
        
        if not os.path.isdir(self.file_path):
            print(f"Path is not a directory: {self.file_path}")
            return None
        
        items = os.listdir(self.file_path)
        full_paths = [os.path.join(self.file_path, item) for item in items]
        return full_paths