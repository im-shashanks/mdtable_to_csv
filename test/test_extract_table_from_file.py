# from src.extract_table import ExtractTable
from mdtable_to_csv.src import ExtractTable
import pytest


def test_extrac_table_from_file_simple():
    file="test/test_res/test_file.md"
    end_result = """| Month    | Savings |
| -------- | ------- |
| January  | $250    |
| February | $80     |
| March    | $420    |"""
    table_extractor = ExtractTable(file)
    tables = table_extractor.extract_table_from_file()

    assert end_result in tables

def test_extract_table_from_file_no_newline_at_end():
    file = "test/test_res/test_file_2.md"
    end_result = """| Item              | In Stock | Price |
| :---------------- | :------: | ----: |
| Python Hat        |   True   | 23.99 |
| SQL Hat           |   True   | 23.99 |
| Codecademy Tee    |  False   | 19.99 |
| Codecademy Hoodie |  False   | 42.99 |"""
    table_extractor = ExtractTable(file)
    tables = table_extractor.extract_table_from_file()

    assert end_result in tables

def test_extract_table_from_file_heading_after_tbl():
    file = "test/test_res/test_file_3.md"
    end_result = ["""| Item              | In Stock | Price |
| :---------------- | :------: | ----: |
| Python Hat        |   True   | 23.99 |
| SQL Hat           |   True   | 23.99 |
| Codecademy Tee    |  False   | 19.99 |
| Codecademy Hoodie |  False   | 42.99 |""",
"""| Month    | Savings |
| -------- | ------- |
| January  | $250    |
| February | $80     |
| March    | $420    |"""]
    table_extractor = ExtractTable(file)
    tables = table_extractor.extract_table_from_file()

    assert set(end_result) == set(tables)

def test_extract_table_from_file_spaces_after_tbl():
    file = "test/test_res/test_file_4.md"
    end_result = """| Item              | In Stock | Price |
| :---------------- | :------: | ----: |
| Python Hat        |   True   | 23.99 |
| SQL Hat           |   True   | 23.99 |
| Codecademy Tee    |  False   | 19.99 |
| Codecademy Hoodie |  False   | 42.99 |"""
    table_extractor = ExtractTable(file)
    tables = table_extractor.extract_table_from_file()

    assert end_result in tables

        
def test_extract_table_from_file_cell_widths_vary():
    file = "test/test_res/test_file_5.md"
    
    table_extractor = ExtractTable(file)
    tables = table_extractor.extract_table_from_file()

    assert len(tables) == 3

def test_extract_table_from_file_real_life_md():
    file = "test/test_res/test_file_6.md"

    table_extractor = ExtractTable(file)

    tables = table_extractor.extract_table_from_file()

    for table in tables:
        print(table)

    assert len(tables) == 6