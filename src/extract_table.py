from rich import print as rprint

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
        end_of_file = None

        # Check if a table exists in the markdown file
        init_idx = 0
        
        while True: # Looping through the entire file to identify tables
            if not md_file.find("|", init_idx) == -1:
                tbl_start_idx = md_file.find("|", init_idx)
                tbl_end_idx = None
            else: break

            # Scan the length of table to find the end of table. Find the last "|"
            # The last "|" is found when there isn't another "|" after "|"

            search_idx = tbl_start_idx # helper flag to update end search idx
            while True: # Looping the length of table
                row_end_idx = md_file.find("|\n", search_idx)
                if row_end_idx == -1:
                    # Check if this is the last table or end of file
                    end_of_file = len(md_file)
                    diff = end_of_file - search_idx
                    if md_file[search_idx : search_idx + diff] == "|":
                        tbl_end_idx = end_of_file
                    break
                
                if md_file[row_end_idx + 2] == "|":
                    search_idx = row_end_idx + 2
                    continue
                else:
                    tbl_end_idx = row_end_idx
                    break
            if end_of_file == None:
                tables.append(md_file[tbl_start_idx: tbl_end_idx+1])
            else:
                tables.append(md_file[tbl_start_idx: tbl_end_idx])
                
            if end_of_file == None:
                init_idx = tbl_end_idx+1
            else: break
        
        for table in tables:
            print(table)
            print("----------")

        return tables