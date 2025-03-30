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

#--- Setup Collections ---
Login_df = pd.read_csv('Login.csv')

top = Tk()


def JokeProgram():
    global JokeWindow, Joke_df
    JokeWindow = Tk()
    #------ GUI Setup ------
    JokeWindow.geometry('600x400')
    JokeWindow.title('A Funny App')
    JokeWindow.iconbitmap('OtherFiles/AppIcon.ico')
    
    notebook = ttk.Notebook(JokeWindow)
    notebook.pack(pady=15, expand=True)

    #--- Frames ---
    frame1 = ttk.Frame(notebook, width=1920, height=1080)
    frame2 = ttk.Frame(notebook, width=1920, height=1080)
    frame3 = ttk.Frame(notebook, width=1920, height=1080)
    frame4 = ttk.Frame(notebook, width=1920, height=1080)

    frame1.pack(fill='both', expand=True)
    frame2.pack(fill='both', expand=True)
    frame3.pack(fill='both', expand=True)
    frame4.pack(fill='both', expand=True)


    #--- Notebook ---
    notebook.add(frame1, text='Joke Curation')
    notebook.add(frame2, text='Collections')
    notebook.add(frame3, text='Help')
    notebook.add(frame4, text='Account')


    JokeDisplaySetup = tk.Label(frame1, text="")
    JokeDisplayPunchline = tk.Label(frame1, text="")

    try:
        Joke_df = pd.read_csv(f'Users\{Username}\Collections.csv')
    except: 
        Joke_df = pd.read_csv(f'Collections_Default.csv')

    #--- Setup for Table ---
    pt = Table(frame2, dataframe=Joke_df, showtoolbar=False, showstatusbar=False, editable=True, enable_menus=False)
    pt.show()


    def JokeCuration():
        global JokeAPI, Addrow, Removerow
        def DisplayJokes():
            global JokeAPI 
            
            try:
                JokeAPI = requests.get('https://joke.deno.dev/')
                JokeDisplaySetup.config(text = f'{JokeAPI.json()['setup']}')
                JokeDisplayPunchline.config(text = f'{JokeAPI.json()['punchline']}')

            except:  
                JokeDisplaySetup.config(text = f'Error 404 - API Not Responding')
                JokeDisplayPunchline.config(text = f'Please use the Non-API Functions')

            JokeDisplaySetup.place(x=10, y=50)
            JokeDisplayPunchline.place(x=10, y=100)
            
        DisplayJokes()
        
        DiscardJoke = tk.Button(frame1, 
                    text="👎 Discard Joke", 
                    command=lambda: [DisplayJokes()],
                    anchor="center",
                    bd=3,
                    cursor="hand2",
                    fg="black",
                    font=("Arial", 12),
                    height=2,
                    justify="center",
                    pady=5,
                    width=15,
                    wraplength=300)
        DiscardJoke.place(x=300, y=300)
        
        StoreJoke = tk.Button(frame1, 
                    text="👍 Store Joke", 
                    command=lambda: [Collections(JokeAPI.json()['setup'], JokeAPI.json()['punchline']), DisplayJokes(), Addrow(), Removerow()],
                    anchor="center",
                    bd=3,
                    cursor="hand2",
                    fg="black",
                    font=("Arial", 12),
                    height=2,
                    justify="center",
                    pady=5,
                    width=15,
                    wraplength=300)
        StoreJoke.place(x=50, y=300)

        def Addrow():
            AddJoke = tk.Button(frame2, 
                        text="+ Row", 
                        command=lambda: [Collections('', ''), Addrow(), Removerow()],
                        anchor="center",
                        bd=3,
                        cursor="hand2",
                        fg="black",
                        font=("Arial", 12),
                        height=1,
                        justify="center",
                        pady=5,
                        width=5,
                        wraplength=300,
                        bg="#3bccaa")
            AddJoke.place(x=1470, y=690)

        def Removerow():
            inputtxt = tk.Text(frame2, 
                        height = 1, 
                        width = 5) 
        
            inputtxt.place(x=1470, y=600) 

            

            RemoveJoke = tk.Button(frame2, 
                        text="- Row", 
                        command=lambda: [Drop_Row(), Removerow(), Addrow()],
                        anchor="center",
                        bd=3,
                        cursor="hand2",
                        fg="black",
                        font=("Arial", 12),
                        height=1,
                        justify="center",
                        pady=5,
                        width=5,
                        wraplength=300,
                        bg="#3bccaa")
            RemoveJoke.place(x=1470, y=640)

            def Drop_Row():
                global Joke_df
                try:
                    RowNotFound.destroy()
                except:
                    pass
                try:
                    Joke_df = Joke_df.drop(index=(int(inputtxt.get('1.0', 'end')) - 1)).reset_index(drop=True)
                    try:
                        pt.destroy()
                    except:
                        pass
                    pt = Table(frame2, dataframe=Joke_df, showtoolbar=False, showstatusbar=False, editable=True, enable_menus=False)
                    pt.show()
                except:
                    RowNotFound = tk.Label(frame2, text="Error - Row Not Found - Please Try Again", fg="Red").place(x=0, y=0)
                

        Addrow()
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
        
        pt = Table(frame2, dataframe=Joke_df, showtoolbar=False, showstatusbar=False, editable=True, enable_menus=False)
        pt.show()
        

    def SaveUpdates():
        global JokeWindow, Joke_df, Username
        print(Username)
        try:
            Joke_df.to_csv(path_or_buf=f'Users\{Username}\Collections.csv', index=False)
        except:
            os.mkdir(f'Users\{Username}')
            Joke_df.to_csv(path_or_buf=f'Users\{Username}\Collections.csv', index=False)

        JokeWindow.destroy()
        

    JokeWindow.protocol('WM_DELETE_WINDOW', SaveUpdates) # call function() when window is closed

    JokeCuration()
    Login()

def Login():
    global Username, Password, Login
    top.geometry('600x400')
    top.title('A Funny App Login')
    top.iconbitmap('OtherFiles/AppIcon.ico')

    LoginTxt = tk.Label(top, text="Login:").place(x=25, y=25)
    UsernameLabel = tk.Label(top, text="Username:").place(x=50, y=50)
    PasswordLabel = tk.Label(top, text="Password:").place(x=50, y=100)

    UsernameInput = tk.Entry(top,
                width = 20
                )
    UsernameInput.place(x=150, y=50) 
    
    PasswordInput = tk.Entry(top,
                width = 20
                )
    PasswordInput.place(x=150, y=100)
    
    Login = tk.Button(top, 
                text="Login", 
                command=lambda: [Account(UsernameInput.get().strip(), PasswordInput.get().strip())], #hash_value = calculate_sha256(input_data) converts to sha256, store that, then check the password is stored like that
                anchor="center",
                bd=3,
                cursor="hand2",
                fg="black",
                font=("Arial", 12),
                height=1,
                justify="center",
                pady=5,
                width=5,
                wraplength=300,
                bg="#3bccaa").place(x=50, y=150)
    
    UsernameCreate = tk.Label(top, text="Username:").place(x=50, y=200)
    PasswordCreate = tk.Label(top, text="Password:").place(x=50, y=250)

    UsernameCreateInput = tk.Entry(top,
                width = 20
                )
    UsernameCreateInput.place(x=150, y=200) 
    
    PasswordCreateInput = tk.Entry(top,
                width = 20
                )
    PasswordCreateInput.place(x=150, y=250)
    
    Login = tk.Button(top, 
                text="Create Account", 
                command=lambda: [CreateAccount(UsernameCreateInput.get().strip(), PasswordCreateInput.get().strip())], #hash_value = calculate_sha256(input_data) converts to sha256, store that, then check the password is stored like that
                anchor="center",
                bd=3,
                cursor="hand2",
                fg="black",
                font=("Arial", 12),
                height=1,
                justify="center",
                pady=5,
                width=5,
                wraplength=300,
                bg="#3bccaa").place(x=50, y=300)
    
    
    def Account(User, Pass):
        global Username
        User = User.join(User.splitlines())
        Pass = Pass.join(Pass.splitlines())
        Pass = hashlib.sha256(Pass.encode()).hexdigest()
        

        with open('Login.csv', mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                Username, Password = row[0], row[1]
                print(row[0], row[1])
                print(User, Username, Pass, Password)
                if Username == User and Password == Pass:
                    top.withdraw()
                    JokeProgram()
                    return
                else:
                    print('WTH HAPPENED')
                    

    def CreateAccount(Username, Password):
        global Login_df
        Username = Username.join(Username.splitlines())
        Password = Password.join(Password.splitlines())
        Password = hashlib.sha256(Password.encode()).hexdigest()

        NewLogin = {
        "Username": Username, 
        "Password": Password, 
        }

        Login_df.loc[len(Login_df)] = NewLogin

        Login_df = Login_df.reset_index(drop=True)
        Login_df.to_csv(path_or_buf='Login.csv', index=False)        

Login()
    
top.mainloop()