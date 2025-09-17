import tkinter as tk
from tkinter import ttk, messagebox
import secrets
import string

# --- password generator function ---
def generate_password():
    try:
        length = int(length_var.get())
        if length <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid length (positive number).")
        return

    charset = ""
    if use_lower.get():
        charset += string.ascii_lowercase
    if use_upper.get():
        charset += string.ascii_uppercase
    if use_digits.get():
        charset += string.digits
    if use_symbols.get():
        charset += "!@#$%^&*()-_=+[]{};:,.<>?/"

    if not charset:
        messagebox.showerror("Error", "Select at least one character type!")
        return

    password = "".join(secrets.choice(charset) for _ in range(length))
    password_var.set(password)


# --- copy password to clipboard ---
def copy_password():
    pwd = password_var.get()
    if pwd:
        root.clipboard_clear()
        root.clipboard_append(pwd)
        messagebox.showinfo("Copied", "Password copied to clipboard!")
    else:
        messagebox.showwarning("Warning", "No password to copy.")


# --- GUI setup ---
root = tk.Tk()
root.title("Password Generator")

frame = ttk.Frame(root, padding=15)
frame.grid()

# length input
ttk.Label(frame, text="Password Length:").grid(row=0, column=0, sticky="w")
length_var = tk.StringVar(value="12")
ttk.Entry(frame, textvariable=length_var, width=5).grid(row=0, column=1, sticky="w")

# options
use_lower = tk.BooleanVar(value=True)
use_upper = tk.BooleanVar(value=True)
use_digits = tk.BooleanVar(value=True)
use_symbols = tk.BooleanVar(value=False)

ttk.Checkbutton(frame, text="Lowercase (a-z)", variable=use_lower).grid(row=1, column=0, sticky="w")
ttk.Checkbutton(frame, text="Uppercase (A-Z)", variable=use_upper).grid(row=1, column=1, sticky="w")
ttk.Checkbutton(frame, text="Digits (0-9)", variable=use_digits).grid(row=2, column=0, sticky="w")
ttk.Checkbutton(frame, text="Symbols (!@#...)", variable=use_symbols).grid(row=2, column=1, sticky="w")

# generate button
ttk.Button(frame, text="Generate", command=generate_password).grid(row=3, column=0, pady=10)
ttk.Button(frame, text="Copy", command=copy_password).grid(row=3, column=1)

# output field
password_var = tk.StringVar()
ttk.Entry(frame, textvariable=password_var, width=40).grid(row=4, column=0, columnspan=2, pady=10)

root.mainloop()
