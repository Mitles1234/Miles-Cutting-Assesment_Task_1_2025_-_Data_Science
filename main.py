#--- Imports ---
import requests
import pandas as pd
from tkinter import *
from pandastable import Table, TableModel

import tkinter as tk
from tkinter import ttk

#--- Setup Collections ---
Joke_df = pd.read_csv('Collections.csv') 

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

frame1.pack(fill='both', expand=True)
frame2.pack(fill='both', expand=True)
frame3.pack(fill='both', expand=True)

#--- Notebook ---
notebook.add(frame1, text='Joke Curation')
notebook.add(frame2, text='Collections')
notebook.add(frame3, text='Help')

JokeDisplaySetup = tk.Label(frame1, text="")
JokeDisplayPunchline = tk.Label(frame1, text="")

#--- Setup for Table ---
pt = Table(frame2, dataframe=Joke_df, showtoolbar=True, showstatusbar=True)
pt.show()

def JokeCuration():
    global JokeAPI
    def DisplayJokes():
        global JokeAPI, JokeDisplaySetup, JokeDisplaySetup
        
        JokeAPI = requests.get('https://joke.deno.dev/')
        JokeDisplaySetup.config(text = f'{JokeAPI.json()['setup']}')
        JokeDisplayPunchline.config(text = f'{JokeAPI.json()['punchline']}')
        
        JokeDisplaySetup.place(x=10, y=50)
        JokeDisplayPunchline.place(x=10, y=75)
        
    DisplayJokes()
    
    DiscardJoke = tk.Button(frame1, 
                text="👎 Discard Joke", 
                command=lambda: [DisplayJokes(), Joke_df.to_csv(path_or_buf='Collections.csv', index=False)],
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
                command=lambda: [Collections(JokeAPI.json()['setup'], JokeAPI.json()['punchline']), DisplayJokes(), Joke_df.to_csv(path_or_buf='Collections.csv', index=False)],
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

def Collections(Setup, Punchline):
    global Joke_df, NewJoke, pt
        
    NewJoke = {
    "Setup": Setup, 
    "Punchline": Punchline
    }
    '''
    Joke_df = pd.concat([Joke_df, NewJoke])
    '''

    # Create a dictionary with the data for the new row

    # Inserting the new row
    Joke_df.loc[len(Joke_df)] = NewJoke

    # Reset the index
    Joke_df = Joke_df.reset_index(drop=True)
    
    try:
        pt.destroy()
    except:
        pass
    pt = Table(frame2, dataframe=Joke_df, showtoolbar=True, showstatusbar=True)
    pt.adjustColumnWidths()
    pt.show()
    


JokeCuration()
inputtxt = tk.Text(frame2, 
                    height = 1, 
                    width = 20) 
    
inputtxt.place(x=1600, y=180) 

DeleteText = tk.Label(frame1, text="")

    
top.mainloop()