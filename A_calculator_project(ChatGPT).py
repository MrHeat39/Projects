import tkinter as tk

class Calculator:44
def __init__(self, root):
        self.root = root
        self.root.title("🧮 Advanced Calculator")
        self.root.geometry("300x400")
        self.root.resizable(False, False)

        self.equation = ""
        self.input_text = tk.StringVar()

        self.input_frame = tk.Frame(self.root, height=50, bd=0)
        self.input_frame.pack(side=tk.TOP)

        self.input_field = tk.Entry(
            self.input_frame,
            font=('arial', 18),
            textvariable=self.input_text,
            justify="right",
            bd=10,
            bg="#eee"
        )
        self.input_field.grid(row=0, column=0)
        self.input_field.pack(ipady=10)

        self.buttons_frame = tk.Frame(self.root)
        self.buttons_frame.pack()

        buttons = [
            ('C', 1, 0), ('/', 1, 1), ('*', 1, 2), ('-', 1, 3),
            ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('+', 2, 3),
            ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('=', 3, 3),
            ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('.', 4, 3),
            ('0', 5, 0)
        ]

        for (text, row, col) in buttons:
            if text == '0':
                tk.Button(self.buttons_frame, text=text, width=30, height=2, command=lambda t=text: self.on_click(t)).grid(row=row, column=col, columnspan=4)
            elif text == '=':
                tk.Button(self.buttons_frame, text=text, width=5, height=2, bg="#4CAF50", fg="white", command=self.calculate).grid(row=row, column=col)
            elif text == 'C':
                tk.Button(self.buttons_frame, text=text, width=5, height=2, bg="#f44336", fg="white", command=self.clear).grid(row=row, column=col)
            else:
                tk.Button(self.buttons_frame, text=text, width=5, height=2, command=lambda t=text: self.on_click(t)).grid(row=row, column=col)

