import csv
import os
from termcolor import colored
from tabulate import tabulate
from utilities.csv2xlsx import convertCsv2Xlsx

def list_columns(file_path):
    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        headers = next(reader)
        table = [[idx, header] for idx, header in enumerate(headers, start=1)]
        print(tabulate(table, headers=["Index", "Header"], tablefmt="grid"))
        return headers

def get_columns_to_copy(headers):
    selected_columns = input(colored("Enter the columns you want to copy separated by commas, press Enter to include all columns: ", "light_yellow"))
    if not selected_columns.strip():
        return headers
    selected_indices = [int(num.strip()) - 1 for num in selected_columns.split(',')]
    return [headers[i] for i in selected_indices]

def copy_selected_columns(input_file, output_file, columns_to_copy):
    with open(input_file, mode='r', newline='', encoding='utf-8') as infile, \
         open(output_file, mode='w', newline='', encoding='utf-8') as outfile:
        reader = csv.DictReader(infile)
        writer = csv.DictWriter(outfile, fieldnames=columns_to_copy)
        writer.writeheader()
        for row in reader:
            writer.writerow({col: row[col] for col in columns_to_copy})

def main():
    print(colored("\nCleanCSV\n---------", 'blue'))
    input_file = input(colored("Enter the location of your CSV-file: ", 'light_yellow')).strip('"')
    if not input_file.lower().endswith('.csv'):
        print(colored("Input must be a .csv file", 'red'))
        main()

    output_file = input(colored("Provide new filename, press Enter to skip: ", "light_yellow"))
    if len(output_file) == 0:
        output_file = os.path.splitext(input_file)[0] + f"_CLEANCSV.csv"
    else:
        output_file = os.path.join(os.path.dirname(input_file), output_file + ".csv")

    columns_to_copy = get_columns_to_copy(list_columns(input_file))
    copy_selected_columns(input_file, output_file, columns_to_copy)
    print(colored(f"Cleaned up CSV and stored as {output_file}.", "green"))
    convert = input(colored(f"Do you want to convert {output_file} to Excel? (y=yes): ", "light_yellow"))
    if convert == "y" or "Y" or "Yes" or "yes":
        convertCsv2Xlsx(output_file)