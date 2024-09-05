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
            md_file = md_file.read()

        tables = []
        no_more_tables = False
        page_end = len(md_file)
        
        try:
            tbl_start_idx = md_file.index("|")
        except:
            no_more_tables = True
        try:
            tbl_end_idx = md_file.index("|\n\n", tbl_start_idx)
        except:
            tbl_end_idx = md_file.index("\n", tbl_start_idx)
            no_more_tables = True
        
        tbl = md_file[tbl_start_idx: tbl_end_idx+1]
        tables.append(tbl)

        while no_more_tables==False:
            try:
                tbl_start_idx = md_file.index("|", tbl_end_idx + 1)
            except: break
            try:
                tbl_end_idx = md_file.index("|\n\n", tbl_start_idx)
            except:
                tbl_end_idx = md_file.index("\n", tbl_start_idx)
                no_more_tables = True

            tbl = md_file[tbl_start_idx: tbl_end_idx+1]
            tables.append(tbl)

        # for table in tables:
        #     print(table)

        # return tables