import pandas
import matplotlib.pyplot as plt
import numpy
from sympy import *
from tkinter import *
from tkinter import filedialog

BG_COLOR = "white"
FONT_NAME = "Unispace"

x_title = None
y_title = None

x_data = None
y_data = None

data_type = "Line Graph"

window = Tk()
window.title("Data Visualizer")
window.minsize(width=500, height=300)
window.config(bg=BG_COLOR)

starting_page_frame = Frame(window)
import_data_frame = Frame(window)
create_data_frame = Frame(window)

# Stacks the frames on top of each other
for frame in (starting_page_frame, import_data_frame, create_data_frame):
    frame.grid(row=0, column=0, sticky="news")


def change_frame(page):
    page.tkraise()


def select_file():
    global x_data, y_data, data_type
    for selection in option_spinbox.curselection():
        data_type = option_spinbox.get(selection)

    file_path = filedialog.askopenfilename()
    data = pandas.read_csv(file_path)
    data_col_names = [col_name for col_name in data.to_dict().keys()]

    x_data = data[data_col_names[0]].to_list()
    y_data = data[data_col_names[1]].to_list()

    create_data(x=x_data, y=y_data)


# Starting Page
starting_page_frame.config(bg=BG_COLOR)
starting_page_canvas = Canvas(starting_page_frame, width=500, height=222, bg=BG_COLOR, highlightthickness=0)

logo = PhotoImage(file="logo2.png")
starting_page_canvas.create_image(250, 111, image=logo)
starting_page_canvas.grid(column=0, row=0)

import_data_button = Button(starting_page_frame, text="Import CSV Data", width=40, pady=5,
                            command=lambda: change_frame(import_data_frame))
import_data_button.grid(column=0, row=3, pady=10)

create_new_graph_button = Button(starting_page_frame, text="Create New Graph", width=40, pady=5,
                                 command=lambda: change_frame(create_data_frame))
create_new_graph_button.grid(column=0, row=5, pady=10)

# Import Data Page
import_data_frame.config(bg=BG_COLOR)

visualize_label = Label(import_data_frame, text="Data Type:", font=(FONT_NAME, 12, "bold"))
visualize_label.grid(column=0, row=0, pady=10)

option_spinbox = Listbox(import_data_frame, font=(FONT_NAME, 10, "bold"), height=4, selectmode="single", width=50)
option_spinbox.insert(1, "Pie Chart")
option_spinbox.insert(2, "Bar Graph")
option_spinbox.insert(3, "Line Graph")
option_spinbox.insert(4, "Scatterplot")
option_spinbox.grid(column=0, row=1, padx=10, columnspan=4)

visualize_button = Button(import_data_frame, text="Select File", width=20, command=select_file)
visualize_button.grid(column=0, row=6, padx=20, pady=20)

back_button = Button(import_data_frame, text="Back", command=lambda: change_frame(starting_page_frame), width=20)
back_button.grid(column=1, row=6, padx=20, pady=20)

import_data_label = Label(import_data_frame, text="IMPORT DATA", font=(FONT_NAME, 20), bg=BG_COLOR, width=30)
import_data_label.grid(column=0, row=7, columnspan=2, rowspan=2)

# Create Graph Page
create_data_frame.config(bg=BG_COLOR)
# X
x_values_label = Label(create_data_frame, text="Enter X-Values")
x_values_label.grid(column=0, row=0, padx=10, pady=10)

x_values_entry = Entry(create_data_frame, width=50)
x_values_entry.grid(column=1, row=0, padx=10, pady=10, columnspan=2)

x_title_label = Label(create_data_frame, text="Enter X-Title")
x_title_label.grid(column=0, row=1, padx=10, pady=10)

x_title_entry = Entry(create_data_frame, width=50)
x_title_entry.grid(column=1, row=1, padx=10, pady=10, columnspan=2)

# Y
y_values_label = Label(create_data_frame, text="Enter Y-Values")
y_values_label.grid(column=0, row=3, padx=10, pady=10)

y_values_entry = Entry(create_data_frame, width=50)
y_values_entry.grid(column=1, row=3, padx=10, pady=10, columnspan=2)

y_title_label = Label(create_data_frame, text="Enter Y-Title")
y_title_label.grid(column=0, row=4, padx=10, pady=10)

y_title_entry = Entry(create_data_frame, width=50)
y_title_entry.grid(column=1, row=4, padx=10, pady=10, columnspan=2)

# Data Type
create_label = Label(create_data_frame, text="Data Type:", font=(FONT_NAME, 10, "bold"))
create_label.grid(column=0, row=5)

create_spinbox = Listbox(create_data_frame, font=(FONT_NAME, 10, "bold"), height=4, selectmode="single")
create_spinbox.insert(1, "Pie Chart")
create_spinbox.insert(2, "Bar Graph")
create_spinbox.insert(3, "Line Graph")
create_spinbox.insert(4, "Scatterplot")
create_spinbox.grid(column=0, row=6, padx=10, columnspan=2, pady=10)

create_button = Button(create_data_frame, text="Create", width=10, command=lambda: assign_values())
create_button.grid(column=1, row=7, padx=10, pady=10)

create_back_button = Button(create_data_frame, text="Back", width=10, command=lambda: change_frame(starting_page_frame))
create_back_button.grid(column=2, row=7, padx=10, pady=10)


# Visualization
def assign_values():
    global x_data, y_data, x_title, y_title, data_type
    x_title = x_title_entry.get()
    y_title = y_title_entry.get()
    x_data = []
    y_data = []
    data_type = ""

    num = ""
    y_str = y_values_entry.get()
    for digit in y_str:
        if digit.isdigit():
            num += digit
        if not digit.isdigit() or y_str[-1] == digit:
            y_data.append(num)
            num = ""
    if '' in y_data:
        y_data.remove('')

    x_str = x_values_entry.get()
    num = ""
    for digit in x_str:
        if digit.isdigit():
            num += digit
        if not digit.isdigit() or x_str[-1] == digit:
            x_data.append(num)
            num = ""
    if '' in x_data:
        x_data = []

    if len(x_data) == 0:
        word = ""
        x_str = x_values_entry.get()
        for letter in x_str:
            if letter.isalpha():
                word += letter
            if not letter.isalpha() or x_str[-1] == letter:
                x_data.append(word)
                word = ""

    x_data = [x for x in x_data if x != '']
    y_data = [x for x in y_data if x != '']

    for selection in create_spinbox.curselection():
        data_type += create_spinbox.get(selection)

    create_data(x=x_data, y=y_data)


def create_data(**kwargs):
    data = pandas.DataFrame(kwargs)
    data.to_csv("data.csv")
    visualize(data)


def visualize(data=None):
    if data_type != "Bar Graph" and data_type != "Pie Chart":
        data['x'] = data['x'].astype(float)
    else:
        pass
    data['y'] = data['y'].astype(float)

    if data_type == "Line Graph":
        x_matrix = []
        for x in x_data:
            row = [1.0, float(x)]
            x_matrix.append(row)

        m_and_b = calculate_least_square(x_matrix)
        m = m_and_b[1]
        b = m_and_b[0]

        equation_str = f"y = {str(m).rstrip('0').rstrip('.') if m != 0 else '0'}*x + {str(b).rstrip('0').rstrip('.') if b != 0 else '0'}"

        xlist = numpy.arange(-100, 110, 10)
        ylist = linear_equation(m, b, xlist)

        plt.plot(xlist, ylist, label=equation_str)
    elif data_type == "Scatterplot":
        plt.scatter(data['x'], data['y'])
    elif data_type == "Bar Graph":
        data_y = [None if v == '' else float(v) for v in y_data]
        plt.bar(x_data, data_y)
    else:
        plt.pie(y_data, labels=x_data)

    plt.xlabel(x_title)
    plt.ylabel(y_title)
    plt.legend()
    plt.show()


# Math
def linear_equation(m, b, x):
    return m * x + b


def calculate_least_square(x_matrix):
    x_matrix = Matrix(x_matrix)
    y_matrix = Matrix(y_data)
    x_transpose_matrix = x_matrix.transpose()

    x_matrix = numpy.array(x_matrix)
    y_matrix = numpy.array(y_matrix)
    x_transpose_matrix = numpy.array(x_transpose_matrix)

    y_matrix = numpy.matmul(x_transpose_matrix, y_matrix)
    x_matrix = numpy.matmul(x_transpose_matrix, x_matrix)

    augmented_matrix = numpy.column_stack((x_matrix, y_matrix))
    augmented_matrix = Matrix(augmented_matrix)
    augmented_matrix = augmented_matrix.rref()

    m = augmented_matrix[0][2]
    b = augmented_matrix[0][5]

    return m, b


# Show starting page initially
change_frame(starting_page_frame)

window.mainloop()
