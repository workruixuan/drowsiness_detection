import gspread
import numpy as np

print("<<Connecting to Googlesheets>>")
sa = gspread.service_account(filename="service_account.json")
sh = sa.open("MESSYVision")
wks = sh.worksheet("Sheet1")


class Googlesheets: 

    def __init__(self, name):
        record_row = wks.find(name, in_column=1)
        self.record_row = record_row
        self.name = name
        # array = np.array([[1, 2, 3], [4, 5, 6]])


        # print('Rows: ', wks.row_count)
        # print('Column: ', wks.add_cols(1))

        # print(wks.acell('A2').value)
        # print(wks.cell(1,1).value)
        # print(wks.get('A1:B2'))

        # print(wks.get_all_records())
        # print(wks.get_all_values())

        # wks.update('A3', 'test')
        # wks.update('A4:B6', [['testa', 'testb'], ['sota','sotb'], ['sotc','sotd']])

        # wks.update('C2', '=UPPER(A4)', raw=False)
        # wks.delete_rows(5)
        # Write the array to worksheet starting from the A2 cell
        # wks.update('A2', array.tolist())
        # new_row = next_available_row(wks)
        # print(new_row)

    def next_available_row():
        str_list = list(filter(None, wks.col_values(1)))
        return str(len(str_list)+1)

    def addYawn(self, name, record_row): #yawn
        print("Update yawn: " , name)
        wks.update('B'+str(record_row.row), int(wks.acell('B'+str(record_row.row)).value) + 1)
        return 1

    def addSleepy(self, name, record_row): #eye blink
        print("Update sleepy eye: " , name)
        wks.update('C'+str(record_row.row), int(wks.acell('C'+str(record_row.row)).value) + 1)
        return 1
    
    def createIfNotFound(self, name, record_row): #search if the record exist, else create it
        cell = wks.find(name, in_column=1)
        if cell == None:
            new_row = Googlesheets.next_available_row()
            wks.update('A'+new_row, name)
            wks.update('B'+new_row, 0)
            wks.update('C'+new_row, 0)
            print("create")
        else:
            print("Found record")
        return 1
    
    def getEmail(self, name):
        cell = wks.find(name, in_column=1)
        email = ""
        if cell == None: # no record found so just ignore
            return 0
        else:
            email = wks.acell('E'+str(cell.row)).value
        return email


# gg = Googlesheets()
print("<<Connected to Googlesheets>>")
# gg.createIfNotFound("Rui Xuan")