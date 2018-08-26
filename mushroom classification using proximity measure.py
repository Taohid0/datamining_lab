from tkinter import *
import xlrd
from tkinter.filedialog import askopenfilename
from tkinter import messagebox


win = Tk()
win.title("Mushroom classification using proximity measure")
win.state("zoomed")

scrollbar = Scrollbar(win)
scrollbar.pack(side=RIGHT, fill=Y)

mylist = Listbox(win, yscrollcommand=scrollbar.set, height=30)


mylist.pack(fill=X, anchor=CENTER)
scrollbar.config(command=mylist.yview)


class ProximityMeasure:
    def __init__(self):

        self.main_similarity_list = []

        self.feature_dataset = None
        self.sheet = None
        self.rows = None
        self.columns = None

        self.test_dataset = None
        self.test_sheet = None
        self.test_dataset_rows = None
        self.test_dataset_columns = None

    def load_feature_data(self):
        self.feature_dataset = xlrd.open_workbook(askopenfilename())
        self.sheet = self.feature_dataset.sheet_by_index(0)
        self.rows = self.sheet.nrows
        self.columns = self.sheet.ncols
        messagebox.showinfo("Successful", "Feature dataset loading successful")

    def load_test_data(self):
        self.test_dataset = xlrd.open_workbook(askopenfilename())
        self.test_sheet = self.test_dataset.sheet_by_index(0)
        self.test_dataset_rows =  self.test_sheet.nrows
        self.test_dataset_columns = self.test_sheet.ncols
        messagebox.showinfo("Successful", "Test dataset loading successful")

    def calculate_similarity(self):
        self.main_similarity_list = []
        for i in range(self.test_dataset_rows):
            temp_similarity_list = []
            for j in range(self.rows):
                similarity = 0

                for k in range(1, self.columns):
                    if self.test_sheet.cell_value(i, k) == self.sheet.cell_value(j, k):
                        similarity = similarity+1

                similarity_pencantage = similarity/(self.columns-1)
                temp_similarity_list.append((self.sheet.cell_value(j,0),similarity_pencantage))
            self.main_similarity_list.append((i, temp_similarity_list))
        messagebox.showinfo("Successful", "Calculation successfully completed")

    def show_mushroom_type(self):
        mylist.delete(0, END)
        for counter, i in enumerate(self.main_similarity_list):
            all_values = [j[1] for j in i[1]]
            maximum_percentage = max(all_values)
            maximum_matches = [j for j in i[1] if j[1]==maximum_percentage]

            if len(maximum_matches) == 1:
                mylist.insert(END, "Sample {} is {}".format(counter+1, maximum_matches[0][0]))
            else:
                p_counter= 0
                e_counter = 0

                for k in maximum_matches:
                    if k[0] == "p":
                        p_counter = p_counter + 1
                    else:
                        e_counter = e_counter + 1
                if e_counter > e_counter:
                    mylist.insert(END, "Sample {} is {}".format(counter + 1, "e"))
                else:
                    mylist.insert(END, "Sample {} is {}".format(counter + 1, "p"))

    def show(self):
        load_feature_data_button = Button(win, text="Load feature data", command=self.load_feature_data)
        load_feature_data_button.pack(side=LEFT, expand=True)

        load_query_data_button = Button(win, text="Load query data", command=self.load_test_data)
        load_query_data_button.pack(side=LEFT, expand=True)

        calculate_proximity_button = Button(win, text="Calculate proximity", command=self.calculate_similarity)
        calculate_proximity_button.pack(side=LEFT, expand=True)

        show_mushroom_type_button = Button(win, text="Show mushroom type", command = self.show_mushroom_type)
        show_mushroom_type_button.pack(side=LEFT, expand=True)

        win.mainloop()


proximity_measure_object = ProximityMeasure()
proximity_measure_object.show()
