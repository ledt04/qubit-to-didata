import os
import pandas as pd
import numpy as np
import shutil
from pathlib import Path

def check_file_exists(file_path):
    """Check if a file exists at the given path."""
    if not os.path.exists(file_path):
        raise None
    if not os.path.isdir(file_path):
        raise None
    return [os.path.join(file_path, item) for item in os.listdir(file_path)]

def load_csv(file_path):
    """Load a CSV file into a pandas DataFrame."""
    try:
        df = pd.read_csv(file_path)
        return df
    except Exception as e:
        print(f"Error loading CSV file: {e}")
        return None
    
def save_csv(df, output_path):
    """Save a pandas DataFrame to a CSV file."""
    try:
        df.to_csv(output_path, index=False)
        return True
    except Exception as e:
        print(f"Error saving CSV file: {e}")
        return False
    
def delete_file(file_path):
    """Delete a file at the given path."""
    try:
        os.remove(file_path)
        return True
    except Exception as e:
        print(f"Error deleting file: {e}")
        return False