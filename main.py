#--- Imports ---
import requests
import pandas as pd
from tkinter import *
from pandastable import Table, TableModel
import tkinter as tk
from tkinter import ttk
import hashlib

#--- Setup Collections ---
Joke_df = pd.read_csv('Collections.csv') 

Username = 'Guest'
Password = 'Guest1'

#------ GUI Setup ------
top = Tk()
top.geometry('600x400')
top.title('A Funny App')
top.iconbitmap('OtherFiles/AppIcon.ico')


notebook = ttk.Notebook(top)
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

#--- Setup for Table ---
pt = Table(frame2, dataframe=Joke_df, showtoolbar=False, showstatusbar=False, editable=True, enable_menus=False)
pt.show()


def JokeCuration():
    global JokeAPI
    def DisplayJokes():
        global JokeAPI, JokeDisplaySetup, JokeDisplaySetup
        
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
                command=lambda: [Collections(JokeAPI.json()['setup'], JokeAPI.json()['punchline']), DisplayJokes()],
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
                Joke_df = Joke_df.drop([int(inputtxt.get('1.0', 'end')) - 1])
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
    global top, Joke_df
    Joke_df.to_csv(path_or_buf='Collections.csv', index=False)
    '''
    newWindow = Toplevel(top)
 
    # sets the title of the
    # Toplevel widget
    newWindow.title("New Window")
 
    # sets the geometry of toplevel
    newWindow.geometry("300x20")
 
    # A Label widget to show in toplevel
    Label(newWindow, text ="Someone became a little less funny just then").pack()'''
    top.destroy()
    top.destroy()
    top.destroy()
    top.destroy()
    top.destroy()
    top.destroy()

top.protocol('WM_DELETE_WINDOW', SaveUpdates) # call function() when window is closed

def Login():
    global Username, Password, Login
    LoginTxt = tk.Label(frame4, text="Login:").place(x=25, y=25)
    Username = tk.Label(frame4, text="Username:").place(x=50, y=50)
    Password = tk.Label(frame4, text="Password:").place(x=50, y=100)

    UsernameInput = tk.Text(frame4,
                height = 1, 
                width = 20
                )
    UsernameInput.place(x=150, y=50) 
    
    PasswordInput = tk.Text(frame4,
                height = 1, 
                width = 20
                )
    PasswordInput.place(x=150, y=100)
    
    Login = tk.Button(frame4, 
                text="Login", 
                command=lambda: [Account(UsernameInput.get(1.0, 'end'), PasswordInput.get(1.0, 'end'))],
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
    
    def Account(Name, Pass):
        global LoginSuccess

        if Name == 'Miles' and Pass == ' Rulez':
            LoginSuccess = tk.Label(frame4, text='Login Successful').place(x=50, y=200)

        else:
            LoginSuccess = tk.Label(frame4, text='Login UnSuccessful').place(x=50, y=200)
            print(Name,Pass)


JokeCuration()
Login()

    
top.mainloop()