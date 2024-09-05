# from src.extract_table import ExtractTable
from mdtable_to_csv.src import ExtractTable
import pytest


def test_extractable_from_file():
    file="res/test_file.md"
    end_result = """| Month    | Savings |
| -------- | ------- |
| January  | $250    |
| February | $80     |
| March    | $420    |"""
    table_extractor = ExtractTable(file)
    tables = table_extractor.extract_table_from_file()

    assert end_result in tables

        
