import pandas as pd
import os
from termcolor import colored


def convertCsv2Xlsx(path):
    csv_file_path = path.replace('"', "")
    # Read the CSV file
    df = pd.read_csv(csv_file_path)
    # Get the directory of the original file
    directory = os.path.dirname(csv_file_path)
    # Create the base file name without extension
    base_name = os.path.splitext(os.path.basename(csv_file_path))[0]
    new_file_name = input(
        colored("Provide new filename, press Enter to skip: ", "light_yellow")
    )
    if not new_file_name.strip():
        new_file_path = os.path.join(directory, f"{base_name}_2XLSX.xlsx")
    else:
        new_file_path = os.path.join(directory, f"{new_file_name}.xlsx")
    # Save the DataFrame to an Excel file
    df.to_excel(new_file_path, index=False)
    print(colored(f"Converted file saved as: {new_file_path}", "green"))


def main():
    print(colored("\nConvert CSV to Excel\n--------------------", "blue"))
    csv_file_path = input(
        colored("Enter the full path of the CSV file: ", "light_yellow")
    )
    convertCsv2Xlsx(csv_file_path)
