from rich import print as rprint
import re

class ExtractTable(object):

    def __init__(self, file_path: str):
        self.file_path = file_path
    

    def extract_table_from_file(self) -> list[str]:
        """_summary_

        Returns:
            str: _description_
        """

        with open(self.file_path, 'r') as md_file:
            md_file = md_file.read().strip()

        tables = []
        lines = md_file.splitlines()
        table = []
        inside_table = False

        for line in lines:
            stripped_line = line.strip()

            # Detect if this line is part of a table (starts with '|')
            if stripped_line.startswith("|"):
                inside_table = True
                table.append(line)  # Add line to the current table
            else:
                if inside_table:
                    # End of a table if a non-table line is encountered
                    tables.append("\n".join(table).strip())
                    table = []  # Reset for the next table
                    inside_table = False

        # If a table was being processed when the file ends, append it
        if table:
            tables.append("\n".join(table).strip())

        return tables