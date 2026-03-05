import pandas as pd
import numpy as np
from utils import load_csv, save_csv, delete_file

class QubitData:
    def __init__(self, file_path):
        self.file_path = file_path
        self.df = None

    def load_data(self):
        self.df = load_csv(self.file_path)
        
    def save_data(self, output_path):
        return save_csv(self.df, output_path)
    
    def delete_file(self):
        return delete_file(self.file_path)