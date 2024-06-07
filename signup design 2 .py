import tkinter as tk
from tkinter import ttk, messagebox

# Initialize the main window
root = tk.Tk()
root.minsize(300, 300)
root.title("SignUp")
root.configure(bg="black")

# Configure styles
style = ttk.Style()
style.configure("Custom.TLabel", background="black", foreground="skyblue", font=("Bell MT", 25))

# Create a Label with the custom style
label = ttk.Label(root, text="SignUp", style="Custom.TLabel")
label.pack(pady=(150,0))

nameentry = tk.Entry(root, font=("Book Antiqua", 15, 'bold'), highlightthickness=2, bg='black', fg='white', highlightcolor='white', justify='center', insertbackground="white")
nameentry.pack(pady=10)

emailentry = tk.Entry(root, font=("Book Antiqua", 15, 'bold'), highlightthickness=2, bg='black', fg='white', highlightcolor='white', justify='center', insertbackground="white")
emailentry.pack(pady=10)

passwordentry = tk.Entry(root, font=("Book Antiqua", 15, 'bold'), highlightthickness=2, bg='black', fg='white', highlightcolor='white', show='*', justify='center', insertbackground="white")
passwordentry.pack(pady=10)

confirmpasswordentry = tk.Entry(root, font=("Book Antiqua", 15, 'bold'), highlightthickness=2, bg='black', fg='white', highlightcolor='white', show='*', justify='center', insertbackground="white")
confirmpasswordentry.pack(pady=10)
# Define the placeholder functionality
def add_placeholder(entry, placeholder):
    def on_focus_in(event):
        if entry.get() == placeholder:
            entry.delete(0, tk.END)
            entry.config(fg='white', show='*' if entry in [passwordentry, confirmpasswordentry] else '')

    def on_focus_out(event):
        if entry.get() == '':
            entry.insert(0, placeholder)
            entry.config(fg='grey', show='*' if entry in [passwordentry, confirmpasswordentry] else '')

    entry.insert(0, placeholder)
    entry.config(fg='grey')
    entry.bind("<FocusIn>", on_focus_in)
    entry.bind("<FocusOut>", on_focus_out)

# Add placeholders
add_placeholder(nameentry, "User Name")
add_placeholder(emailentry, "Email/Number")
add_placeholder(passwordentry, "Password")
add_placeholder(confirmpasswordentry, "Confirm Password")

# Pack the widgets
nameentry.pack()
emailentry.pack()
passwordentry.pack()
confirmpasswordentry.pack()

# Define the signup function
def signup():
    messagebox.showinfo("Success", "Signup Successfully")

# Create the signup button and bind it to the signup function
button = tk.Button(root, text="SignUp", font=("Book Antiqua", 15, 'bold'), bg='black', fg='skyblue', command=signup)
button.pack(padx=10, pady=10)

# Set the window transparency
root.attributes('-alpha', 0.9)

# Run the main event loop
root.mainloop()
