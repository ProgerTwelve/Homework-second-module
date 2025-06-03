from typing import Any
import csv
import pandas as pd

csv_path = r"C:\Users\Admin\PycharmProjects\PythonProject\data\transactions.csv"
excel_path = r"C:\Users\Admin\PycharmProjects\PythonProject\data\transactions_excel.xlsx"
def get_csv_data(path: str = csv_path) -> list[dict[str,str]]:
    """Считывает финансовые операции из CSV-файла"""
    csv_list = []
    with open(path, encoding="utf-8") as csv_file:
        csv_data = csv.DictReader(csv_file, delimiter=';')
        for row in csv_data:
            csv_list.append(row)

    return csv_list







def get_excel_data(path: str = excel_path) -> list[dict[Any,Any]]:
    """Считывает финансовые операции из Excel-файла"""

    excel_data = pd.read_excel(path)



