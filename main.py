#--- Imports ---
import requests
import pandas as pd
from tkinter import *
from pandastable import Table, TableModel
import tkinter as tk
from tkinter import ttk
import hashlib
import csv
import os
from cryptography.fernet import Fernet
from tkinter import font

#--- Colours ---
BgColour = "#32a2a8"
AccentColour1 = "#3bccaa"

#--- Setup Collections ---
Login_df = pd.read_csv('Login.csv')

top = Tk()
top['bg'] = BgColour

def JokeProgram():
    global JokeWindow, Joke_df, RollingJoke
    JokeWindow = Tk()

    BackgroundColour = BgColour
    #JokeWindow['bg'] = BackgroundColour

    #------ GUI Setup ------
    JokeWindow.geometry('600x400')
    JokeWindow.title('A Funny App')
    JokeWindow.iconbitmap('OtherFiles/AppIcon.ico')
    
    notebook = ttk.Notebook(JokeWindow)
    notebook.pack(pady=15, expand=True)

    #--- Frames ---
    frame1 = Frame(notebook, width=1920, height=1080, bg=BackgroundColour)
    frame2 = Frame(notebook, width=1920, height=1080)
    frame3 = Frame(notebook, width=1920, height=1080)
    frame4 = Frame(notebook, width=1920, height=1080, bg=BackgroundColour)

    frame1.pack(fill='both', expand=True)
    frame2.pack(fill='both', expand=True)
    frame3.pack(fill='both', expand=True)
    frame4.pack(fill='both', expand=True)
    
    #--- Notebook ---
    notebook.add(frame1, text='Joke Curation')
    notebook.add(frame2, text='Collections')
    notebook.add(frame3, text='History')
    notebook.add(frame4, text='Help')


    
    #--- Unencrypt Collection ---
    try:
        with open(f'Keys\{Username}.key', 'rb') as filekey:
            key = filekey.read()
            
        # using the key
        fernet = Fernet(key)
        
        # opening the encrypted file
        with open(f'Users\{Username}\Collections.csv', 'rb') as enc_file:
            encrypted = enc_file.read()
        
        # decrypting the file
        decrypted = fernet.decrypt(encrypted)
        
        # opening the file in write mode and
        # writing the decrypted data
        with open(f'Users\{Username}\Collections.csv', 'wb') as dec_file:
            dec_file.write(decrypted)
            
        Joke_df = pd.read_csv(f'Users\{Username}\Collections.csv')
    except: 
        Joke_df = pd.read_csv(f'Collections_Default.csv')

    #--- Setup for Table ---
    pt = Table(frame2, dataframe=Joke_df, showtoolbar=False, showstatusbar=False, editable=False, enable_menus=False)
    pt.show()


    def JokeCuration():
        global JokeAPI, Removerow, RollingJoke, RollingJoke_df, RollingJokeTable
        Space = tk.Label(frame1, text="", font=("Ariel", 14, "bold"), fg='white', bg=BackgroundColour).pack(pady=5)
        Space = tk.Label(frame1, text="", font=("Ariel", 14, "bold"), fg='white', bg=BackgroundColour).pack(pady=5)


        Joke = tk.Label(frame1, text="Joke:", font=("Ariel", 14, "bold"), fg='white', bg=BackgroundColour).pack(pady=5)

        RollingJoke = [
        {'Setup': 'No History', 'Punchline': 'No History'},
        {'Setup': 'No History', 'Punchline': 'No History'}
            ]   

        RollingJoke_df = pd.DataFrame(RollingJoke)

        for i in range(2,5):
            try:
                JokeAPI = requests.get('https://joke.deno.dev/')
                NewRollingJoke_df = ({'Setup': JokeAPI.json()['setup'], 'Punchline': JokeAPI.json()['punchline']})
            except:
                NewRollingJoke_df = ({'Setup': f'Error 404 - API Not Responding', 'Punchline': f'Please use the Non-API Functions'})
            
            RollingJoke_df.loc[len(RollingJoke_df)] = NewRollingJoke_df

            RollingJoke_df = RollingJoke_df.reset_index(drop=True)

        RollingJokeTable = Table(frame3, dataframe=RollingJoke_df, showtoolbar=False, showstatusbar=False, editable=False, enable_menus=False)
        RollingJokeTable.show()

        RollingButtonFrame = tk.Frame(frame3, bg=BackgroundColour)
        RollingButtonFrame.grid(column=2, row=1, sticky='n')
        def AddJokeButton():
            AddJokeButton1 = tk.Button(RollingButtonFrame, text="Add Joke (1)", font=("Arial", 10, "bold"), width=20, cursor="hand2", command=lambda: [Collections(RollingJoke_df.iloc[0]["Setup"], RollingJoke_df.iloc[0]["Punchline"])]).pack(side="top")
            AddJokeButton2 = tk.Button(RollingButtonFrame, text="Add Joke (2)", font=("Arial", 10, "bold"), width=20, cursor="hand2", command=lambda: [Collections(RollingJoke_df.iloc[1]["Setup"], RollingJoke_df.iloc[1]["Punchline"])]).pack(side="top")
            AddJokeButton3 = tk.Button(RollingButtonFrame, text="Add Joke (3)", font=("Arial", 10, "bold"), width=20, cursor="hand2", command=lambda: [Collections(RollingJoke_df.iloc[2]["Setup"], RollingJoke_df.iloc[2]["Punchline"])]).pack(side="top")
            AddJokeButton4 = tk.Button(RollingButtonFrame, text="Add Joke (4)", font=("Arial", 10, "bold"), width=20, cursor="hand2", command=lambda: [Collections(RollingJoke_df.iloc[3]["Setup"], RollingJoke_df.iloc[3]["Punchline"])]).pack(side="top")
            AddJokeButton5 = tk.Button(RollingButtonFrame, text="Add Joke (5)", font=("Arial", 10, "bold"), width=20, cursor="hand2", command=lambda: [Collections(RollingJoke_df.iloc[4]["Setup"], RollingJoke_df.iloc[4]["Punchline"])]).pack(side="top")

        def DisplayJokes():
            global JokeAPI, RollingJoke_df
            try:
                JokeAPI = requests.get('https://joke.deno.dev/')
                NewRollingJoke_df = ({'Setup': JokeAPI.json()['setup'], 'Punchline': JokeAPI.json()['punchline']})
            except:
                NewRollingJoke_df = ({'Setup': f'Error 404 - API Not Responding', 'Punchline': f'Please use the Non-API Functions'})
            
            RollingJoke_df = pd.concat([RollingJoke_df.iloc[1:], pd.DataFrame([NewRollingJoke_df])], ignore_index=True)

            JokeDisplaySetup.config(text = RollingJoke_df.iloc[2]['Setup'])
            JokeDisplayPunchline.config(text = RollingJoke_df.iloc[2]['Punchline'])

            JokeDisplaySetup.pack(pady=2)
            JokeDisplayPunchline.pack(pady=2)
            
            try:
                RollingJokeTable.destroy()
            except:
                pass

            RollingJokeTable = Table(frame3, dataframe=RollingJoke_df, showtoolbar=False, showstatusbar=False, editable=False, enable_menus=False)
            RollingJokeTable.show()
            AddJokeButton()

        JokeDisplaySetup = tk.Label(frame1, text="", font=("Ariel", 10, "bold"), fg='white', bg=BackgroundColour)
        JokeDisplayPunchline = tk.Label(frame1, text="", font=("Ariel", 10, "bold"), fg='white', bg=BackgroundColour)
            
        DisplayJokes()

        ButtonFrame = tk.Frame(frame1, bg=BackgroundColour)
        ButtonFrame.pack(pady=10, anchor="center")
        
        StoreJoke = tk.Button(ButtonFrame, 
                    text="👍 Store Joke", 
                    command=lambda: [Collections(JokeAPI.json()['setup'], JokeAPI.json()['punchline']), DisplayJokes(), Removerow()],
                    anchor="center",
                    bd=3,
                    cursor="hand2",
                    fg="black",
                    font=("Arial", 12),
                    height=1,
                    justify="center",
                    pady=5,
                    width=15,
                    wraplength=300)
        StoreJoke.pack(side=tk.LEFT, padx=10, expand=True)
        
        DiscardJoke = tk.Button(ButtonFrame, 
                    text="👎 Discard Joke", 
                    command=lambda: [DisplayJokes()],
                    anchor="center",
                    bd=3,
                    cursor="hand2",
                    fg="black",
                    font=("Arial", 12),
                    height=1,
                    justify="center",
                    pady=5,
                    width=15,
                    wraplength=300)
        DiscardJoke.pack(side=tk.LEFT, padx=10, expand=True)
        
        tk.Label(frame1, text="---------------------------", bg=BgColour).pack(pady=5)

        Collection = tk.Label(frame1, text="Collection:", font=("Ariel", 14, "bold"), fg='white', bg=BackgroundColour).pack(pady=5)

        CollectionDisplaySetup = tk.Label(frame1, text="", font=("Ariel", 10, "bold"), fg='white', bg=BackgroundColour)
        CollectionDisplayPunchline = tk.Label(frame1, text="", font=("Ariel", 10, "bold"), fg='white', bg=BackgroundColour)

        CollectionDisplaySetup.pack(pady=2)
        CollectionDisplayPunchline.pack(pady=2)

        def RandomCollectionJoke():
            try:
                CollectionJoke_df.iloc[:0]
            except:
                pass
            CollectionJoke_df = Joke_df.sample(n=1)

            CollectionDisplaySetup.config(text=CollectionJoke_df.iloc[0,0])
            CollectionDisplayPunchline.config(text=CollectionJoke_df.iloc[0,1])

            CollectionDisplaySetup.pack(pady=2)
            CollectionDisplayPunchline.pack(pady=2)

        CollectionJoke = tk.Button(frame1, 
            text="Get Collection Joke", 
            command=lambda: [RandomCollectionJoke()],
            anchor="center",
            bd=3,
            cursor="hand2",
            fg="black",
            font=("Arial", 12),
            height=1,
            justify="center",
            pady=2,
            width=25,
            wraplength=300)
        CollectionJoke.pack(pady=10)

        tk.Label(frame1, text="---------------------------", bg=BgColour).pack(pady=5)

        ManualJoke = tk.Label(frame1, text="Add Joke:", font=("Ariel", 14, "bold"), fg='white', bg=BackgroundColour).pack(pady=5)

        SetupInput = tk.Entry(frame1, width=40, fg="grey", font=("Arial", 10, "italic"), justify="center")
        SetupInput.insert(0, "Setup")
        SetupInput.bind("<FocusIn>", lambda e: SetupInput.delete(0, tk.END) and SetupInput.config(fg="black") if SetupInput.get() == "Setup" else SetupInput.config(fg="grey"))
        SetupInput.bind("<FocusOut>", lambda e: SetupInput.insert(0, "Setup") and SetupInput.config(fg="grey") if SetupInput.get() == "" else SetupInput.config(fg="black"))
        SetupInput.bind("<KeyRelease>", lambda e: SetupInput.config(fg="black") if SetupInput.get() != "Setup" else SetupInput.config(fg="grey"))
        SetupInput.pack(pady=2)

        PunchlineInput = tk.Entry(frame1, width=40, fg="grey", font=("Arial", 10, "italic"), justify="center")
        PunchlineInput.insert(0, "Punchline")
        PunchlineInput.bind("<FocusIn>", lambda e: PunchlineInput.delete(0, tk.END) and PunchlineInput.config(fg="black") if PunchlineInput.get() == "Punchline" else PunchlineInput.config(fg="grey"))
        PunchlineInput.bind("<FocusOut>", lambda e: PunchlineInput.insert(0, "Punchline") and PunchlineInput.config(fg="grey") if PunchlineInput.get() == "" else PunchlineInput.config(fg="black"))
        PunchlineInput.bind("<KeyRelease>", lambda e: PunchlineInput.config(fg="black") if PunchlineInput.get() != "Punchline" else PunchlineInput.config(fg="grey"))
        PunchlineInput.pack(pady=2)

        AddJokeButton = tk.Button(frame1, text="Add Joke", font=("Arial", 10, "bold"), width=20, cursor="hand2", command=lambda: [Collections(SetupInput.get(), PunchlineInput.get())])
        AddJokeButton.pack(pady=2)

        def Removerow():
            global RemoveRow
            RemoveRow = tk.Entry(frame2, 
                        #height = 1, 
                        width = 5) 
        
            RemoveRow.grid(column=1, row=0, sticky=E, padx=12)


            RemoveJoke = tk.Button(frame2, 
                        text="- Row", 
                        command=lambda: [Drop_Row(), Removerow()],
                        anchor="center",
                        bd=3,
                        cursor="hand2",
                        fg="black",
                        font=("Arial", 12),
                        height=1,
                        justify="center",
                        pady=5,
                        width=7,
                        wraplength=300,
                        bg=AccentColour1)
            RemoveJoke.grid(column=2, row=0)

            def Drop_Row():
                global Joke_df
                try:
                    RowNotFound.destroy()
                except:
                    pass
                try:
                    Joke_df = Joke_df.drop(index=(int(RemoveRow.get()) - 1)).reset_index(drop=True)
                    try:
                        pt.destroy()
                    except:
                        pass
                    pt = Table(frame2, dataframe=Joke_df, showtoolbar=False, showstatusbar=False, editable=False, enable_menus=False)
                    pt.show()
                except:
                    RowNotFound = tk.Label(frame2, text="Error - Row Not Found - Please Try Again", fg="Red").place(x=0, y=0)
                
        Removerow()  

    def Collections(Setup, Punchline):
        global Joke_df, NewJoke, pt
            
        Setup.join(Setup.splitlines())

        NewJoke = {
        "Setup": Setup, 
        "Punchline": Punchline
        }

        # Create a dictionary with the data for the new row

        # Inserting the new row
        Joke_df.loc[len(Joke_df)] = NewJoke

        # Reset the index
        Joke_df = Joke_df.reset_index(drop=True)
        
        try:
            pt.destroy()
        except:
            pass
        
        pt = Table(frame2, dataframe=Joke_df, showtoolbar=False, showstatusbar=False, editable=False, enable_menus=False)
        pt.show()
        Removerow()
        
    def SaveUpdates():
        global JokeWindow, Joke_df, Username
        try:
            Joke_df.to_csv(path_or_buf=f'Users\{Username}\Collections.csv', index=False)
        except:
            Userfolder = f"Users"  # This is the folder where keys will be stored
            file_path_user = os.path.join(Userfolder, f"{Username}")
            os.makedirs(file_path_user, exist_ok=True)

            Joke_df.to_csv(path_or_buf=f'Users\{Username}\Collections.csv', index=False)
        
        directory = "Keys"  # This is the folder where keys will be stored
        file_path = os.path.join(directory, f"{Username}.key")  # Define the actual key file

            # Ensure the directory exists before saving the key
        os.makedirs(directory, exist_ok=True)  # Creates 'Keys' folder if it doesn't exist

        # opening the key
        with open(file_path, 'rb') as filekey:
            key = filekey.read()
        
        # using the generated key
        fernet = Fernet(key)

        # opening the original file to encrypt
        with open(f'Users\{Username}\Collections.csv', 'rb') as file:
            original = file.read()
            
        # encrypting the file
        encrypted = fernet.encrypt(original)
        
        # opening the file in write mode and 
        # writing the encrypted data
        with open(f'Users\{Username}\Collections.csv', 'wb') as encrypted_file:
            encrypted_file.write(encrypted)
            
        try:
            JokeWindow.destroy()
        except:
            pass
        try:
            top.destroy()
        except:
            pass
        
    JokeWindow.protocol('WM_DELETE_WINDOW', SaveUpdates) # call function() when window is closed

    JokeCuration()

def Login():
    global Username, Password, UsernameInput, PasswordInput

    BackgroundColour = AccentColour1
    
    #--- Setup for Window ---
    top.geometry('250x400') # Size of Window
    top.title('A Funny App Login') # Name of Windows
    top.iconbitmap('OtherFiles/AppIcon.ico') # App icon of Window

    HidePassword = tk.BooleanVar(value=True) # Sets the Hide Password 'tKinter Integer' to False

    def PasswordHidder():
        if HidePassword.get():
            PasswordInput.config(show='*')
            PasswordCreateInput.config(show='*')
        else:
            PasswordInput.config(show='')
            PasswordCreateInput.config(show='')

    # --- Login Section ---
    tk.Label(top, text="Login", font=("Ariel", 14, "bold"), fg='white', bg=BgColour).pack(pady=(10, 5))

    ErrorMessage = tk.Label(top, text='', fg="red", bg=BgColour, font=("Arial", 10,))
    ErrorMessage.place(x=0,y=0)

    UsernameInput = tk.Entry(top, width=25, fg="grey", font=("Arial", 10, "italic"), justify="center")
    UsernameInput.insert(0, "Username")
    UsernameInput.bind("<FocusIn>", lambda e: UsernameInput.delete(0, tk.END) and UsernameInput.config(fg="black") if UsernameInput.get() == "Username" else None)
    UsernameInput.bind("<FocusOut>", lambda e: UsernameInput.insert(0, "Username") and UsernameInput.config(fg="grey") if UsernameInput.get() == "" else None)
    UsernameInput.bind("<KeyRelease>", lambda e: UsernameInput.config(fg="black") if UsernameInput.get() != "Username" else UsernameInput.config(fg="grey"))
    UsernameInput.pack(pady=2)

    PasswordInput = tk.Entry(top, width=25, fg="grey", font=("Arial", 10, "italic"), justify="center", show="*")
    PasswordInput.insert(0, "Password")
    PasswordInput.bind("<FocusIn>", lambda e: (PasswordInput.delete(0, tk.END) and PasswordInput.config(fg="black")) if PasswordInput.get() == "Password" else None, (PasswordInput.config(show='*') if HidePassword.get() else None))
    PasswordInput.bind("<FocusOut>", lambda e: (PasswordInput.insert(0, "Password") and PasswordInput.config(fg="grey")) if PasswordInput.get() == "" else None, (PasswordInput.config(show='*') if HidePassword.get() else None))
    PasswordInput.bind("<KeyRelease>", lambda e: PasswordInput.config(fg="black") if PasswordInput.get() != "Password" else PasswordInput.config(fg="grey"))
    PasswordInput.pack(pady=2)

    ShowPassword = tk.Checkbutton(top, text="Hide Password", variable=HidePassword, onvalue=True, offvalue=False, command=lambda: PasswordInput.config(show='*') and PasswordCreateInput.config(show='*') if HidePassword.get() else PasswordInput.config(show='') and PasswordCreateInput.config(show=''), fg='white', bg=BgColour, selectcolor='Darkslategrey')
    ShowPassword.pack(pady=2)

    LoginButton = tk.Button(top, text="Login", font=("Arial", 10, "bold"), width=20, bg=BackgroundColour, cursor="hand2", command=lambda: [Account(UsernameInput.get(), PasswordInput.get(), False)])
    LoginButton.pack(pady=2)

    tk.Label(top, text="---------------------------", bg=BgColour).pack(pady=5)

    # --- Create Account Section ---
    tk.Label(top, text="Create Account", font=("Arial", 14, "bold"), fg='white', bg=BgColour).pack(pady=(5, 5))

    UsernameCreateInput = tk.Entry(top, width=25, fg="grey", font=("Arial", 10, "italic"), justify="center")
    UsernameCreateInput.insert(0, "Create Username")
    UsernameCreateInput.bind("<FocusIn>", lambda e: UsernameCreateInput.delete(0, tk.END) and UsernameCreateInput.config(fg="black") if UsernameCreateInput.get() == "Create Username" else None)
    UsernameCreateInput.bind("<FocusOut>", lambda e: UsernameCreateInput.insert(0, "Create Username") and UsernameCreateInput.config(fg="grey") if UsernameCreateInput.get() == "" else None)
    UsernameCreateInput.bind("<KeyRelease>", lambda e: UsernameCreateInput.config(fg="black") if UsernameCreateInput.get() != "Create Username" else UsernameCreateInput.config(fg="grey"))
    UsernameCreateInput.pack(pady=2)

    PasswordCreateInput = tk.Entry(top, width=25, fg="grey", font=("Arial", 10, "italic"), justify="center", show="*")
    PasswordCreateInput.insert(0, "Create Password")
    PasswordCreateInput.bind("<FocusIn>", lambda e: (PasswordCreateInput.delete(0, tk.END) and PasswordCreateInput.config(fg="black")) if PasswordCreateInput.get() == "Create Password" else None, (PasswordCreateInput.config(show='*') if HidePassword.get() else None))
    PasswordCreateInput.bind("<FocusOut>", lambda e: (PasswordCreateInput.insert(0, "Create Password") and PasswordCreateInput.config(fg="grey")) if PasswordCreateInput.get() == "" else None, (PasswordCreateInput.config(show='*') if HidePassword.get() else None))
    PasswordCreateInput.bind("<KeyRelease>", lambda e: PasswordCreateInput.config(fg="black") if PasswordCreateInput.get() != "Create Password" else PasswordCreateInput.config(fg="grey"))
    PasswordCreateInput.pack(pady=2)

    ShowPasswordCreate = tk.Checkbutton(top, text="Hide Password", variable=HidePassword, onvalue=True, offvalue=False, command=lambda: PasswordInput.config(show='*') and PasswordCreateInput.config(show='*') if HidePassword.get() else PasswordInput.config(show='') and PasswordCreateInput.config(show=''), fg='white', bg=BgColour, selectcolor='Darkslategrey')
    ShowPasswordCreate.pack(pady=2)

    CreateAccountButton = tk.Button(top, text="Create Account", font=("Arial", 10, "bold"), width=20, bg=BackgroundColour, cursor="hand2", command=lambda: [CreateAccount(UsernameCreateInput.get(), PasswordCreateInput.get())])
    CreateAccountButton.pack(pady=2)
    
    
    def Account(User, Pass, Logedin):
        global Username
        if Logedin == False:
            User = User.join(User.splitlines())
            Pass = Pass.join(Pass.splitlines())
            Pass = hashlib.sha256(Pass.encode()).hexdigest()
        else:
            directory = "Keys"  # This is the folder where keys will be stored
            file_path = os.path.join(directory, f"{User}.key")  # Define the actual key file

            # Ensure the directory exists before saving the key
            os.makedirs(directory, exist_ok=True)  # Creates 'Keys' folder if it doesn't exist

            # Generate an encryption key
            key = Fernet.generate_key()

            # Write the key to a file
            with open(file_path, 'wb') as filekey:
                filekey.write(key)
        
        with open('Login.csv', mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                Username, Password = row[0], row[1]
                if Username == User and Password == Pass:
                    top.withdraw()
                    JokeProgram()
                    return
                
        ErrorMessage.config(text='Error - Username or Password Incorrect')
        UsernameInput.delete(0, tk.END)
        PasswordInput.delete(0, tk.END)

                                    

    def CreateAccount(Username, Password):
        global Login_df
        
        Username = Username.join(Username.splitlines())
        Password = Password.join(Password.splitlines())
        Password = hashlib.sha256(Password.encode()).hexdigest()

        with open('Login.csv', mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                User = row[0]
                if User == Username:
                    UsernameTaken = True
                    UsernameCreateInput.delete(0, tk.END)
                    PasswordCreateInput.delete(0, tk.END)
                    break
                else:
                    UsernameTaken = False
        if UsernameTaken == False:
            NewLogin = {
            "Username": Username, 
            "Password": Password, 
            }

            Login_df.loc[len(Login_df)] = NewLogin

            Login_df = Login_df.reset_index(drop=True)
            Login_df.to_csv(path_or_buf='Login.csv', index=False)   

            Account(Username, Password, True)

            UsernameCreateInput.delete(0, tk.END)
            PasswordCreateInput.delete(0, tk.END)

        else:
            ErrorMessage.config(text='Error - Username Taken')

#----- Saves Updates to Account ---
def SaveUpdatesTop():
    global JokeWindow, Joke_df, Username
    try:
        JokeWindow.destroy()
    except:
        pass
    try:
        top.destroy()
    except:
        pass
    
top.protocol('WM_DELETE_WINDOW', SaveUpdatesTop) # Replaces the X button command with the command 'SaveUpdatesTop'

Login()
    
top.mainloop()