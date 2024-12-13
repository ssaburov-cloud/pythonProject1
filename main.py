from tkinter import *
from gui import CalculatorView, CalculatorModel

def main():
    root = Tk()
    root.configure(background="#2E3B4E")
    root.title("Calculator")
    root.geometry("450x500")
    root.resizable(False, False)
    app = CalculatorController(root)
    root.mainloop()

class CalculatorController:
    def __init__(self, root):
        self.model = CalculatorModel()
        self.view = CalculatorView(root)
        self.setup_event_handlers()

    def setup_event_handlers(self):
        for button in self.view.buttons:
            button.config(command=lambda num=button.cget("text"): self.button_press(num))
        for button in self.view.operators:
            button.config(command=lambda operator=button.cget("text"): self.operator_press(operator))

    def button_press(self, num):
        self.model.press(num)
        self.view.update_display(self.model.expression)

    def operator_press(self, operator):
        if operator == "=":
            result = self.model.evaluate()
            self.view.update_display(result)
        elif operator == "OFF":
            self.model.clear()
            self.view.update_display(self.model.expression)
        elif operator == "⌫":
            self.model.backspace()
            self.view.update_display(self.model.expression)
        elif operator == "√":
            result = self.model.square_root()
            self.view.update_display(result)
        elif operator == "log":
            result = self.model.log()
            self.view.update_display(result)
        elif operator == "sin":
            result = self.model.sin()
            self.view.update_display(result)
        elif operator == "cos":
            result = self.model.cos()
            self.view.update_display(result)
        elif operator == "tan":
            result = self.model.tan()
            self.view.update_display(result)
        elif operator == "π":
            result = self.model.pi()
            self.view.update_display(result)
        else:
            self.model.press(operator)
            self.view.update_display(self.model.expression)


if __name__ == "__main__":
    main()
