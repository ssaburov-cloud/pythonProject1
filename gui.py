from tkinter import *
import math


class CalculatorModel:
    def __init__(self):
        self.expression = ""

    def press(self, num):
        self.expression += str(num)

    def evaluate(self):
        try:
            result = str(eval(self.expression))
            self.expression = result
            return result
        except:
            self.expression = ""
            return "Error"

    def clear(self):
        self.expression = ""

    def backspace(self):
        self.expression = self.expression[:-1]

    def square_root(self):
        try:
            result = str(math.sqrt(float(self.expression)))
            self.expression = result
            return result
        except:
            self.expression = ""
            return "Error"

    def log(self):
        try:
            result = str(math.log(float(self.expression)))
            self.expression = result
            return result
        except:
            self.expression = ""
            return "Error"

    def sin(self):
        try:
            result = str(math.sin(math.radians(float(self.expression))))
            self.expression = result
            return result
        except:
            self.expression = ""
            return "Error"

    def cos(self):
        try:
            result = str(math.cos(math.radians(float(self.expression))))
            self.expression = result
            return result
        except:
            self.expression = ""
            return "Error"

    def tan(self):
        try:
            result = str(math.tan(math.radians(float(self.expression))))
            self.expression = result
            return result
        except:
            self.expression = ""
            return "Error"

    def pi(self):
        self.expression = str(math.pi)
        return self.expression


class CalculatorView:
    def __init__(self, root):
        self.root = root
        self.equation = StringVar()
        self.create_widgets()

    def create_widgets(self):
        self.expression_field = Entry(self.root, textvariable=self.equation, font=("Arial", 24), bd=10, relief=SUNKEN, justify=RIGHT, bg="#F0F4F8", fg="#2E3B4E")
        self.expression_field.grid(columnspan=5, ipadx=10)

        self.buttons = []
        # Add button references to the list
        button_labels = [
            ('1', 2, 0), ('2', 2, 1), ('3', 2, 2),
            ('4', 3, 0), ('5', 3, 1), ('6', 3, 2),
            ('7', 4, 0), ('8', 4, 1), ('9', 4, 2),
            ('0', 5, 1), ('.', 5, 0)
        ]

        for (text, row, col) in button_labels:
            button = self.create_button(text, row, col)
            self.buttons.append(button)

        self.operators = []
        operator_labels = [
            ('+', 2, 4), ('-', 3, 4), ('*', 4, 4), ('/', 5, 4),
            ('√', 1, 1), ('=', 5, 2), ('OFF', 1, 4), ('⌫', 1, 3),
            ('log', 2, 3), ('sin', 3, 3), ('cos', 4, 3), ('tan', 5, 3), ('π', 1, 2)
        ]

        for (text, row, col) in operator_labels:
            button = self.create_button(text, row, col)
            self.operators.append(button)

    def create_button(self, text, row, col):
        button = Button(self.root, text=text, fg='white', bg='#4D6A8C', font=("Arial", 16), height=2, width=4, relief=SOLID, bd=3, activebackground="#3E5362", activeforeground="white")
        button.grid(row=row, column=col, padx=5, pady=5)
        return button

    def update_display(self, expression):
        self.equation.set(expression)

    def show_error(self, error_message):
        messagebox.showerror("Error", error_message)
