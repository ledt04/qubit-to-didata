from data_monitor import DataMonitor
from qubit_data import QubitData
from data_type_identifier import DataTypeIdentifier
from data_formatter import DataFormatter

def run_pipeline(input_path, output_path):
    while True:
        datamonitor = DataMonitor(input_path)
        files = datamonitor.check_file_exists()

        if files:
            for file in files:
                print(f"Processing file: {file}")
                data = QubitData(file)
                data.load_data()

                if data.df is not None:
                    data_type = DataTypeIdentifier(file).identifier()
                    print(f"Identified data type: {data_type}")

                    formatter = DataFormatter(file, data_type)
                    formatted_data = formatter.format_data()

                    if formatted_data is not None:
                        output_file = output_path / f"formatted_{file.name}"
                        if not formatter.save_data(output_file):
                            print(f"Failed to save data for {file}")
                        else:
                            formatter.delete_file()
                else:
                    print(f"Failed to load data from {file}")
        break

if __name__ == "__main__":
    input_path = "path_to_raw_data"
    output_path = "path_to_processed_data"
    run_pipeline(input_path, output_path)