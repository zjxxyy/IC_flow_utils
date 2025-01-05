from deal_xlsx import *
class XLSX_TO_PST:
    def __init__(self,xlsx_content):
        self.xlsx_content = xlsx_content
        self.origin_pst = []
        self.dfvs_dict = {}

    def deal_xlsx_content(self):
        None


if __name__ == '__main__':
    #print("hh")
    xlsx_result = DEAL_XLSX('./top_pst.xlsx')
    xlsx_result.read_excel_xlsx('Sheet1')
    xlsx_result.show_xlxs_content()
    test = XLSX_TO_PST(xlsx_result.rows_data)