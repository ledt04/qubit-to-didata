import pandas as pd
import numpy as np
from qubit_data import QubitData

class DataFormatter(QubitData):
    def __init__(self, file_path, data_type):
        super().__init__(file_path)
        self.data_type = data_type

    def format_data(self):
        if self.data_type == "DNA Extraction":
            return self.dna_formatter()
        elif self.data_type == "PCR Pool 1-3":
            return self.pcr_formatter()
        elif self.data_type == "Library Quantification":
            return self.lib_formatter()
        else:
            print("Unknown data type, cannot format.")
            return None

    def dna_formatter(self):
        return pd.DataFrame({
            'Test Date': self.df['Test Date'],
            'Assay Name': self.df['Assay Name'],
            'Sample_Id': self.df['Sample Name'],
            'Extracted DNA ng/ul': self.df['Original Sample Conc.'],
            'Sample Volume': np.nan,
            'Status': np.nan
        })

    def pcr_formatter(self):
        return pd.DataFrame({
            'Test Date': self.df['Test Date'],
            'Assay Name': self.df['Assay Name'],
            'Sample_Id': self.df['Sample Name'],
            'ng/ul pool 1': self.df['Original Sample Conc.'],
            'ng/ul pool 2': np.nan,
            'ng/ul pool 3': np.nan,
            'Sample Volume': np.nan,
            'Status': np.nan
        })

    def lib_formatter(self):
        return pd.DataFrame({
            'Test Date': self.df['Test Date'],
            'Assay Name': self.df['Assay Name'],
            'Sample_Id': self.df['Sample Name'] + 'L',
            'Library ng/ul': self.df['Original Sample Conc.'],
            'Sample Volume': np.nan,
            'Status': np.nan
        })