import unittest
from qubit_data import QubitData
from data_type_identifier import DataTypeIdentifier
from data_formatter import DataFormatter

class TestQubitData(unittest.TestCase):
    def test_load_data(self):
        file_path = "path_to_some_data_file.csv"
        qubit_data = QubitData(file_path)
        qubit_data.load_data()
        self.assertIsNotNone(qubit_data.df)

class TestDataTypeIdentifier(unittest.TestCase):
    def test_identifier(self):
        file_path = "path_to_some_data_file.csv"
        data_type_identifier = DataTypeIdentifier(file_path)
        data_type_identifier.load_data()
        data_type = data_type_identifier.identifier()
        self.assertEqual(data_type, "PCR Pool 1-3")

class TestDataFormatter(unittest.TestCase):
    def test_format_data(self):
        file_path = "path_to_some_data_file.csv"
        data_formatter = DataFormatter(file_path, "PCR Pool 1-3")
        data_formatter.load_data()
        formatted_data = data_formatter.format_data()
        self.assertTrue(formatted_data is not None)

if __name__ == "__main__":
    unittest.main()