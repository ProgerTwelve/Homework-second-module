from typing import Any
import os
import pandas as pd

current_dir = os.path.dirname(os.path.abspath(__file__))
real_file_path_csv = os.path.join(current_dir, "../data/transactions.csv")
abs_file_path_csv = os.path.abspath(real_file_path_csv)
real_file_path_excel = os.path.join(current_dir, "../data/transactions_excel.xlsx")
abs_file_path_excel = os.path.abspath(real_file_path_excel)

def get_csv_data(path: str = abs_file_path_csv) -> list[dict[str, str]]:
    """Считывает финансовые операции из CSV-файла"""

    csv_data = pd.read_csv(path, delimiter=";").to_dict(orient="records")

    return csv_data


def get_excel_data(path: str = abs_file_path_excel) -> list[dict[Any, Any]]:
    """Считывает финансовые операции из Excel-файла"""

    excel_data = pd.read_excel(path)

    return excel_data.to_dict(orient="records")
