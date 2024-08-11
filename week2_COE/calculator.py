import tkinter as tk
from math import sqrt

# Function to update the expression in the text entry box
def update_expression(expression):
    current_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current_text + expression)

# Function to evaluate the expression and display the result
def evaluate_expression():
    try:
        result = str(eval(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Function to clear the text entry box
def clear_expression():
    entry.delete(0, tk.END)

# Function to delete the last character
def backspace():
    current_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current_text[:-1])

# Function to calculate the square root
def square_root():
    try:
        result = str(sqrt(float(entry.get())))
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Function to calculate the square
def square():
    try:
        result = str(float(entry.get()) ** 2)
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Creating the main application window
app = tk.Tk()
app.title("Colorful Calculator")
app.configure(bg='#333')

# Creating the entry widget where the expression will be displayed
entry = tk.Entry(app, width=16, font=('Arial', 24), borderwidth=2, relief="solid")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Defining buttons
buttons = [
    ('7', '#f1c40f'), ('8', '#f1c40f'), ('9', '#f1c40f'), ('/', '#e74c3c'),
    ('4', '#f1c40f'), ('5', '#f1c40f'), ('6', '#f1c40f'), ('*', '#e74c3c'),
    ('1', '#f1c40f'), ('2', '#f1c40f'), ('3', '#f1c40f'), ('-', '#e74c3c'),
    ('0', '#f1c40f'), ('.', '#f1c40f'), ('=', '#2ecc71'), ('+', '#e74c3c'),
]

# Creating the buttons and assigning them to the grid
row = 1
col = 0
for (button, color) in buttons:
    if button == '=':
        btn = tk.Button(app, text=button, width=5, height=2, font=('Arial', 18), 
                        command=evaluate_expression, bg=color, fg='white')
    else:
        btn = tk.Button(app, text=button, width=5, height=2, font=('Arial', 18), 
                        command=lambda b=button: update_expression(b), bg=color, fg='white')
    btn.grid(row=row, column=col, padx=5, pady=5)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Additional functionality buttons
tk.Button(app, text='C', width=5, height=2, font=('Arial', 18), 
          command=clear_expression, bg='#e67e22', fg='white').grid(row=row, column=0, padx=5, pady=5)
tk.Button(app, text='√', width=5, height=2, font=('Arial', 18), 
          command=square_root, bg='#3498db', fg='white').grid(row=row, column=1, padx=5, pady=5)
tk.Button(app, text='x²', width=5, height=2, font=('Arial', 18), 
          command=square, bg='#9b59b6', fg='white').grid(row=row, column=2, padx=5, pady=5)
tk.Button(app, text='⌫', width=5, height=2, font=('Arial', 18), 
          command=backspace, bg='#c0392b', fg='white').grid(row=row, column=3, padx=5, pady=5)

# Running the application
app.mainloop()
