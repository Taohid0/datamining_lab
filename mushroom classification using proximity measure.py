from tkinter import *
import xlrd

class Prozimity_measure:

    def __init__(self):
        self.feature_dataset = None
        self.sheet = None
        self.rows = None
        self.columns = None

        self.test_dataset = None
        self.test_sheet = None
        self.test_dataset_rows = None
        self.test_dataset_columns = None

    def load_feature_data(self):
        self.feature_dataset = xlrd.open_workbook("Main Dataset.xlsx")
        self.sheet = self.feature_dataset.sheet_by_index(0)
        self.rows = self.sheet.nrows
        self.columns = self.sheet.ncols

    def load_test_data(self):
        self.test_dataset = xlrd.open_workbook("test dataset.xrlx")
        self.test_sheet = self.test_dataset.sheet_by_index(0)
        self.test_dataset_rows =  self.test_sheet.nrows
        self.test_dataset_columns = self.test_sheet.ncols


win = Tk()
win.title("Mushroom classification using proximity measure")
win.state("zoomed")


scrollbar = Scrollbar(win)
scrollbar.pack( side = RIGHT, fill = Y )

mylist = Listbox(win, yscrollcommand = scrollbar.set,height=30)
for line in range(100):
    mylist.insert(END, "This is line number " + str(line))

mylist.pack(fill = X ,anchor=CENTER)
scrollbar.config( command = mylist.yview )


load_feature_data_button = Button(win,text="Load feature data", command= load_feature_data)
load_feature_data_button.pack(side=LEFT, expand=True)

load_query_data_button = Button(win, text="Load query data")
load_query_data_button.pack(side=LEFT, expand=True)

calculate_proximity_button = Button(win, text="Calculate proximity")
calculate_proximity_button.pack(side=LEFT, expand=True)

show_mushroom_type_button = Button(win, text = "Show mushroom type")
show_mushroom_type_button.pack(side=LEFT, expand=True)

win.mainloop()
