import random
import tkinter as tk
from tkinter import messagebox

def generate_password():
    try:
        psw_length = int(length_entry.get())
        if(psw_length <= 0):
            raise ValueError("Your password length needs to be above 0")
    except ValueError:
        messagebox.showwarning("Error","Introduce a valid integer number for length ")
        return
    inc_low = lowercase_option.get()
    inc_cap = capcase_option.get()
    inc_num = numbers_option.get()
    inc_sym = symbols_option.get()
    inc_spc = spaces_option.get()
    inc_enie = enie_option.get()
    
    capital_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
    numbers = "0123456789"
    symbols = "'-!\"#$%&()*,./:;?@[]^_`{|}~+<=>"
    forbidden_spanish_letter_cap = "Ñ"
    forbidden_spanish_letter_low = "ñ"
    
    psw_builder = ""
    if inc_low:
        psw_builder += lowercase_letters
    if inc_cap:
        psw_builder += capital_letters
    if inc_num:
        psw_builder += numbers
    if inc_sym:
        psw_builder += symbols
    if inc_spc:
        psw_builder += " "
    if inc_enie and inc_low:
        psw_builder += forbidden_spanish_letter_low
    if inc_enie and inc_cap:
        psw_builder += forbidden_spanish_letter_cap
    if not psw_builder:
        messagebox.showerror("Error", "You need to select at least one option")
        return
    
    password = "".join(random.sample(psw_builder,psw_length))
    password_entry.config(state="normal")
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)
    password_entry.config(state="readonly")

def copy_pass():
    password = password_entry.get()
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        root.update()
        messagebox.showinfo("Copy","Password copied to clipboard")

#Main window
root = tk.Tk()
root.title("Password generator")

tk.Label(root, text="Password length: ").grid(row = 0, column = 0, padx = 5, pady = 10)
length_entry = tk.Entry(root, width = 10)
length_entry.grid(row = 0, column = 1, pady = 5)

#Options for password
lowercase_option = tk.BooleanVar(value = True)
capcase_option = tk.BooleanVar(value = True)
numbers_option = tk.BooleanVar(value = True)
symbols_option = tk.BooleanVar(value = True)
spaces_option = tk.BooleanVar(value = False)
enie_option = tk.BooleanVar(value = False)

#Checkbuttons binded to variables
tk.Checkbutton(root, text = "Include lowercase", variable = lowercase_option).grid(row = 1, column = 0, columnspan = 2, sticky = "w", padx = 10, pady = 2)
tk.Checkbutton(root, text = "Include capitalcase", variable = capcase_option).grid(row = 1, column = 1, columnspan = 2, sticky = "w", padx = 10, pady = 2)
tk.Checkbutton(root, text = "Include numbers", variable = numbers_option).grid(row = 2, column = 0, columnspan = 2, sticky = "w", padx = 10, pady = 2)
tk.Checkbutton(root, text = "Include symbols", variable = symbols_option).grid(row = 2, column = 1, columnspan = 2, sticky = "w", padx = 10, pady = 2)
tk.Checkbutton(root, text = "Include spaces", variable = spaces_option).grid(row = 3, column = 0, columnspan = 2, sticky = "w", padx = 10, pady = 2)
tk.Checkbutton(root, text = "Include ñ", variable = enie_option).grid(row = 3, column = 1, columnspan = 2, sticky = "w", padx = 10, pady = 2)

#Password field
tk.Label(root, text = "Password: ").grid(row = 5, column = 0, padx = 10, pady = 5)
password_entry = tk.Entry(root, width = 30, state="readonly")
password_entry.grid(row = 5, column = 1, padx = 10, pady = 5)

#Buttons
tk.Button(root, text = "Generate password", command = generate_password).grid(row = 6, column = 0, padx = 10, pady = 5)
tk.Button(root, text = "Copy password", command = copy_pass).grid(row = 6, column = 1, padx = 10, pady = 5)

if __name__ == "__main__":
    root.mainloop()