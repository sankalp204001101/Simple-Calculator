import tkinter as tk

def on_click(button_value):
    current_text = display_entry.get()
    if button_value == "=":
        try:
            result = eval(current_text)
            display_entry.delete(0, tk.END)
            display_entry.insert(tk.END, str(result))
        except Exception as e:
            display_entry.delete(0, tk.END)
            display_entry.insert(tk.END, "Error")
    elif button_value == "C":
        display_entry.delete(0, tk.END)
    else:
        display_entry.insert(tk.END, button_value)

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")
root.config(bg="aqua")

# Entry widget to display the numbers and results
display_entry = tk.Entry(root, width=30, borderwidth=5)
display_entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Define the buttons
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+",
    "C"
]

# Create and position the buttons
row_num = 1
col_num = 0
for button in buttons:
    tk.Button(root, text=button, padx=20, pady=10, command=lambda val=button: on_click(val)).grid(row=row_num, column=col_num)
    col_num += 1
    if col_num > 3:
        col_num = 0
        row_num += 1

root.mainloop()
