import re
from qubit_data import QubitData

class DataTypeIdentifier(QubitData):
    def __init__(self, file_path):
        super().__init__(file_path)

    def identifier(self):
        sample_names = self.df["Sample Name"]
        std_re = re.compile(r"^STANDARD\d+$", re.IGNORECASE)
        pcr_re = re.compile(r"^.*PD\d+$", re.IGNORECASE)
        lib_re = re.compile(r"^.*L\d+$", re.IGNORECASE)
        dna_re = re.compile(r"^.*D\d+$", re.IGNORECASE)

        for name in sample_names:
            if std_re.fullmatch(name):
                continue
            elif pcr_re.fullmatch(name):
                return "PCR Pool 1-3"
            elif lib_re.fullmatch(name):
                return "Library Quantification"
            elif dna_re.fullmatch(name):
                return "DNA Extraction"
        return "Unknown Data Type"