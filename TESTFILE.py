'''
import tkinter as tk

# Create main window
top = tk.Tk()
top.geometry('400x350')
top.title('A Funny App Login')

# BooleanVar to track password visibility
HidePassword = tk.BooleanVar(value=True)

def PasswordHidder():
    """Toggles password visibility based on checkbox state"""
    show_char = '' if HidePassword.get() else '*'
    PasswordInput.config(show=show_char)
    PasswordCreateInput.config(show=show_char)

# --- Login Section ---
tk.Label(top, text="Login", font=("Arial", 12, "bold")).pack(pady=(10, 5))

frame_login = tk.Frame(top)
frame_login.pack(pady=5)

tk.Label(frame_login, text="Username:").grid(row=0, column=0, sticky="e", padx=5, pady=2)
UsernameInput = tk.Entry(frame_login, width=25)
UsernameInput.grid(row=0, column=1, pady=2)

tk.Label(frame_login, text="Password:").grid(row=1, column=0, sticky="e", padx=5, pady=2)
PasswordInput = tk.Entry(frame_login, width=25, show='*')
PasswordInput.grid(row=1, column=1, pady=2)

# Checkbox for password visibility
ShowPassword = tk.Checkbutton(frame_login, text="Show Password", variable=HidePassword, command=PasswordHidder)
ShowPassword.grid(row=2, column=1, sticky="w", pady=2)

# Login Button
LoginButton = tk.Button(top, text="Login", font=("Arial", 10, "bold"), width=20, bg="#3bccaa", cursor="hand2")
LoginButton.pack(pady=10)

# --- Separator ---
tk.Label(top, text="---------------------------").pack(pady=5)

# --- Create Account Section ---
tk.Label(top, text="Create Account", font=("Arial", 12, "bold")).pack(pady=(5, 5))

frame_signup = tk.Frame(top)
frame_signup.pack(pady=5)

tk.Label(frame_signup, text="Username:").grid(row=0, column=0, sticky="e", padx=5, pady=2)
UsernameCreateInput = tk.Entry(frame_signup, width=25)
UsernameCreateInput.grid(row=0, column=1, pady=2)

tk.Label(frame_signup, text="Password:").grid(row=1, column=0, sticky="e", padx=5, pady=2)
PasswordCreateInput = tk.Entry(frame_signup, width=25, show='*')
PasswordCreateInput.grid(row=1, column=1, pady=2)

# Checkbox for password visibility in sign-up
ShowPasswordSignUp = tk.Checkbutton(frame_signup, text="Show Password", variable=HidePassword, command=PasswordHidder)
ShowPasswordSignUp.grid(row=2, column=1, sticky="w", pady=2)

# Create Account Button
CreateAccountButton = tk.Button(top, text="Create Account", font=("Arial", 10, "bold"), width=20, bg="#3bccaa", cursor="hand2")
CreateAccountButton.pack(pady=10)

# Run the app
top.mainloop()

'''
'''
import tkinter as tk


global UsernameInput, PasswordInput, UsernameCreateInput, PasswordCreateInput

top = tk.Tk()
top.geometry('400x350')
top.title('A Funny App Login')

HidePassword = tk.BooleanVar(value=True)

# Function to toggle password visibility
def PasswordHidder():
    show_char = '' if HidePassword.get() else '*'
    PasswordInput.config(show=show_char)
    PasswordCreateInput.config(show=show_char)

# Function to handle placeholder text
def add_placeholder(entry, placeholder):
    """Adds a placeholder in grey italics to an entry widget"""
    entry.insert(0, placeholder)
    entry.config(fg="grey", font=("Arial", 10, "italic"), justify="center")

    def on_focus_in(event):
        if entry.get() == placeholder:
            entry.delete(0, tk.END)
            entry.config(fg="black", font=("Arial", 10), justify="center")

    def on_focus_out(event):
        if entry.get() == "":
            entry.insert(0, placeholder)
            entry.config(fg="grey", font=("Arial", 10, "italic"), justify="center")

    entry.bind("<FocusIn>", on_focus_in)
    entry.bind("<FocusOut>", on_focus_out)

# --- Login Section ---
tk.Label(top, text="Login", font=("Arial", 12, "bold")).pack(pady=(10, 5))

frame_login = tk.Frame(top)
frame_login.pack(pady=5)

UsernameInput = tk.Entry(frame_login, width=25)
UsernameInput.grid(row=0, column=1, pady=2)
add_placeholder(UsernameInput, "Username")

PasswordInput = tk.Entry(frame_login, width=25, show='*')
PasswordInput.grid(row=1, column=1, pady=2)
add_placeholder(PasswordInput, "Password")

ShowPassword = tk.Checkbutton(frame_login, text="Show Password", variable=HidePassword, command=PasswordHidder)
ShowPassword.grid(row=2, column=1, sticky="w", pady=2)

LoginButton = tk.Button(top, text="Login", font=("Arial", 10, "bold"), width=20, bg="#3bccaa", cursor="hand2")
LoginButton.pack(pady=10)

tk.Label(top, text="---------------------------").pack(pady=5)

# --- Create Account Section ---
tk.Label(top, text="Create Account", font=("Arial", 12, "bold")).pack(pady=(5, 5))

frame_signup = tk.Frame(top)
frame_signup.pack(pady=5)

UsernameCreateInput = tk.Entry(frame_signup, width=25)
UsernameCreateInput.grid(row=0, column=1, pady=2)
add_placeholder(UsernameCreateInput, "Username")

PasswordCreateInput = tk.Entry(frame_signup, width=25, show='*')
PasswordCreateInput.grid(row=1, column=1, pady=2)
add_placeholder(PasswordCreateInput, "Password")

ShowPasswordSignUp = tk.Checkbutton(frame_signup, text="Show Password", variable=HidePassword, command=PasswordHidder)
ShowPasswordSignUp.grid(row=2, column=1, sticky="w", pady=2)

CreateAccountButton = tk.Button(top, text="Create Account", font=("Arial", 10, "bold"), width=20, bg="#3bccaa", cursor="hand2")
CreateAccountButton.pack(pady=10)

top.mainloop()
'''
import tkinter as tk


global UsernameInput, PasswordInput, UsernameCreateInput, PasswordCreateInput

top = tk.Tk()
top.geometry('400x350')
top.title('A Funny App Login')

HidePassword = tk.BooleanVar(value=True)

# Toggle password visibility
def PasswordHidder():
    show_char = '' if HidePassword.get() else '*'
    PasswordInput.config(show=show_char)
    PasswordCreateInput.config(show=show_char)

# --- Login Section ---
tk.Label(top, text="Login", font=("Arial", 12, "bold")).pack(pady=(10, 5))

UsernameInput = tk.Entry(top, width=25, fg="grey", font=("Arial", 10, "italic"), justify="center")
UsernameInput.insert(0, "Username")
UsernameInput.bind("<FocusIn>", lambda e: UsernameInput.delete(0, tk.END) if UsernameInput.get() == "Username" else None)
UsernameInput.bind("<FocusOut>", lambda e: UsernameInput.insert(0, "Username") if UsernameInput.get() == "" else None)
UsernameInput.pack(pady=2)

PasswordInput = tk.Entry(top, width=25, fg="grey", font=("Arial", 10, "italic"), justify="center", show="*")
PasswordInput.insert(0, "Password")
PasswordInput.bind("<FocusIn>", lambda e: (PasswordInput.delete(0, tk.END), PasswordInput.config(fg="black", show="")) if PasswordInput.get() == "Password" else None)
PasswordInput.bind("<FocusOut>", lambda e: (PasswordInput.insert(0, "Password"), PasswordInput.config(fg="grey", show="*")) if PasswordInput.get() == "" else None)
PasswordInput.pack(pady=2)

ShowPassword = tk.Checkbutton(top, text="Show Password", variable=HidePassword, command=PasswordHidder)
ShowPassword.pack(pady=2)

LoginButton = tk.Button(top, text="Login", font=("Arial", 10, "bold"), width=20, bg="#3bccaa", cursor="hand2")
LoginButton.pack(pady=10)

tk.Label(top, text="---------------------------").pack(pady=5)

# --- Create Account Section ---
tk.Label(top, text="Create Account", font=("Arial", 12, "bold")).pack(pady=(5, 5))

UsernameCreateInput = tk.Entry(top, width=25, fg="grey", font=("Arial", 10, "italic"), justify="center")
UsernameCreateInput.insert(0, "Create Username")
UsernameCreateInput.bind("<FocusIn>", lambda e: UsernameCreateInput.delete(0, tk.END) if UsernameCreateInput.get() == "Create Username" else None)
UsernameCreateInput.bind("<FocusOut>", lambda e: UsernameCreateInput.insert(0, "Create Username") if UsernameCreateInput.get() == "" else None)
UsernameCreateInput.pack(pady=2)

PasswordCreateInput = tk.Entry(top, width=25, fg="grey", font=("Arial", 10, "italic"), justify="center", show="*")
PasswordCreateInput.insert(0, "Create Password")
PasswordCreateInput.bind("<FocusIn>", lambda e: (PasswordCreateInput.delete(0, tk.END), PasswordCreateInput.config(fg="black", show="")) if PasswordCreateInput.get() == "Create Password" else None)
PasswordCreateInput.bind("<FocusOut>", lambda e: (PasswordCreateInput.insert(0, "Create Password"), PasswordCreateInput.config(fg="grey", show="*")) if PasswordCreateInput.get() == "" else None)
PasswordCreateInput.pack(pady=2)

ShowPasswordSignUp = tk.Checkbutton(top, text="Show Password", variable=HidePassword, command=PasswordHidder)
ShowPasswordSignUp.pack(pady=2)

CreateAccountButton = tk.Button(top, text="Create Account", font=("Arial", 10, "bold"), width=20, bg="#3bccaa", cursor="hand2")
CreateAccountButton.pack(pady=10)

top.mainloop()