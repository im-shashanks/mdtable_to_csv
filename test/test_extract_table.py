from src.extract_table import ExtractTable
import pytest


def test_extractable_from_file():
    file="res/test_file.md"
    table_extractor = ExtractTable(file)
    tables = table_extractor.extract_table_from_file()

    assert type(tables) == str

        
