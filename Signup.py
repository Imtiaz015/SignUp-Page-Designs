import tkinter as tk
from tkinter import ttk , messagebox




root = tk.Tk()
root.minsize(300, 300)
root.title("SignUp")
root.configure(bg="black")


style = ttk.Style()
style.configure("Custom.TLabel", background="black", foreground="skyblue", font=("Book Antiqua", 25,'bold'))



# Create a Label with the custom style
label = ttk.Label(root, text="SignUp", style="Custom.TLabel")
label.grid(row=0, column=0, columnspan=2, pady=(200, 10),padx=(600,180))

# Create another Label and an Entry widget
nameLabel = ttk.Label(root, text="Enter User Name :", font=("Book Antiqua", 15,'bold'), style="Custom.TLabel")
nameLabel.grid(row=1, column=0, padx=(430,0), pady=10, sticky="E")

nameentry = tk.Entry(root, font=("Book Antiqua", 15,'bold',),highlightthickness=2,bg='black',fg='white',highlightcolor='white',justify='center',insertbackground="white")
nameentry.grid(row=1, column=1, padx=10, pady=10, sticky="W")

# Create another Label and an Entry widget
passwordLabel = ttk.Label(root, text="Enter Email/Number :", font=("Book Antiqua", 15,'bold'), style="Custom.TLabel")
passwordLabel.grid(row=2, column=0, padx=10, pady=10, sticky="E")

passwordentry = tk.Entry(root, font=("Book Antiqua", 15,'bold'),highlightthickness=2,bg='black',fg='white',highlightcolor='white',show='*',justify='center',insertbackground="white")
passwordentry.grid(row=2, column=1, padx=10, pady=10, sticky="W")



# Create another Label and an Entry widget
nameLabel = ttk.Label(root, text="Enter User Password:", font=("Book Antiqua", 15,'bold'), style="Custom.TLabel")
nameLabel.grid(row=3, column=0, padx=(430,0), pady=10, sticky="E")

nameentry = tk.Entry(root, font=("Book Antiqua", 15,'bold',),highlightthickness=2,bg='black',fg='white',highlightcolor='white',justify='center',insertbackground="white")
nameentry.grid(row=3, column=1, padx=10, pady=10, sticky="W")

# Create another Label and an Entry widget
passwordLabel = ttk.Label(root, text="Confirm Password :", font=("Book Antiqua", 15,'bold'), style="Custom.TLabel")
passwordLabel.grid(row=4, column=0, padx=10, pady=10, sticky="E")

passwordentry = tk.Entry(root, font=("Book Antiqua", 15,'bold'),highlightthickness=2,bg='black',fg='white',highlightcolor='white',show='*',justify='center',insertbackground="white")
passwordentry.grid(row=4, column=1, padx=10, pady=10, sticky="W")



# Define the login function
def signup():
    messagebox.showinfo(text='Signup Successfully')

button =tk.Button(text="SignUp",font=("Book Antiqua", 15,'bold'),bg='black',fg='skyblue',command=signup)
button.grid(row=5,column=1 , padx=10,pady=10,sticky='W')

root.attributes('-alpha', 0.9)
root.mainloop()
