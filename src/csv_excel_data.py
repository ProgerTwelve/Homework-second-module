from typing import Any

import pandas as pd

csv_path = r"C:\Users\Admin\PycharmProjects\PythonProject\data\transactions.csv"
excel_path = r"C:\Users\Admin\PycharmProjects\PythonProject\data\transactions_excel.xlsx"


def get_csv_data(path: str = csv_path) -> list[dict[str, str]]:
    """Считывает финансовые операции из CSV-файла"""

    csv_data = pd.read_csv(path, delimiter=";").to_dict(orient="records")

    return csv_data


def get_excel_data(path: str = excel_path) -> list[dict[Any, Any]]:
    """Считывает финансовые операции из Excel-файла"""

    excel_data = pd.read_excel(path)

    return excel_data.to_dict(orient="records")
