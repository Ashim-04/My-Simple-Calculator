import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Ashim's Calculator")

        # Creating an input box for the user
        self.entry = tk.Entry(master, width=20, font=("Times New Roman", 16))
        self.entry.grid(row=0, column=0, columnspan=4, padx=5, pady=5)
        self.entry.bind('<Return>', lambda event: self.calculate())

        #Create buttons for digits
        digits = ['7', '8', '9', '4', '5', '6', '1', '2', '3', '0', '.', 'C']
        for i, digit in enumerate(digits):
            row = i // 3 + 1
            col = i % 3
            if digit == 'C':
                button = tk.Button(master, text=digit, width=5, command=self.clear)
            else:
                button = tk.Button(master, text=digit, width=5, command=lambda digit=digit: self.press(digit))
            button.grid(row=row, column=col, padx=5, pady=5)

        #Create buttons for Operators
        operators = ['+', '-', '*', '/']
        for i, operator in enumerate(operators):
            button = tk.Button(master, text=operator, width=5, command=lambda operator=operator: self.press(operator))
            button.grid(row=i+1, column=3, padx=5, pady=5)

        #Create button for equals
        equalsButton= tk.Button(master, text='=', width=5, command=self.calculate)
        equalsButton.grid(row=5, column=2, padx=5, pady=5)

    def press(self, digit):
        self.entry.insert(tk.END, digit)

    def clear(self):
        self.entry.delete(0, tk.END)

    def calculate(self):
        try:
            result = eval(self.entry.get())
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, str(result))
        except:
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, "Error")

root = tk.Tk()
calc = Calculator(root)
root.mainloop()