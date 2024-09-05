# from src.extract_table import ExtractTable
from mdtable_to_csv.src import ExtractTable
import pytest


def test_extrac_table_from_file_simple():
    file="res/test_file.md"
    end_result = """| Month    | Savings |
| -------- | ------- |
| January  | $250    |
| February | $80     |
| March    | $420    |"""
    table_extractor = ExtractTable(file)
    tables = table_extractor.extract_table_from_file()

    assert end_result in tables

def test_extract_table_from_file_no_newline_at_end():
    file = "res/test_file_2.md"
    end_result = """| Item              | In Stock | Price |
| :---------------- | :------: | ----: |
| Python Hat        |   True   | 23.99 |
| SQL Hat           |   True   | 23.99 |
| Codecademy Tee    |  False   | 19.99 |
| Codecademy Hoodie |  False   | 42.99 |"""
    table_extractor = ExtractTable(file)
    tables = table_extractor.extract_table_from_file()

    assert end_result in tables

        
