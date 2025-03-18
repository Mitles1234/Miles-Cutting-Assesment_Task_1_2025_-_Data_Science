#--- Imports ---
import requests
import pandas as pd
from tkinter import *

import tkinter as tk
from tkinter import ttk

#--- Setup Collections ---
# Joke_df = pd.read_csv('Collections.csv') 
Joke_df = pd.DataFrame(columns=['Setup', 'Punchline'])

#--- API ---


#------ GUI Setup ------
top = Tk()
top.geometry('600x400')
top.title('A Funny App')

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

def JokeCuration():
    global JokeAPI
    def DisplayJokes():
        global JokeAPI, JokeDisplaySetup, JokeDisplaySetup
        
        JokeAPI = requests.get('https://joke.deno.dev/')
        JokeDisplaySetup.config(text = f'{JokeAPI.json()['setup']}')
        JokeDisplayPunchline.config(text = f'{JokeAPI.json()['punchline']}')
        
        JokeDisplaySetup.place(x=10, y=50)
        JokeDisplayPunchline.place(x=10, y=75)
        
    NewJoke = tk.Button(frame1, 
                text="↻ NewJoke", 
                command=DisplayJokes,
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
    NewJoke.place(x=50, y=300)
    NewJoke = tk.Button(frame1, 
                text="👍 Store Joke", 
                command=Collections(JokeAPI.json()['setup'], JokeAPI.json()['punchline']),
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
    NewJoke.place(x=300, y=300)

def Collections(Setup, Punchline):
    NewJoke = {
    "Setup":[Setup], 
    "Punchline": [Punchline]
}
    Joke_df = pd.concat([Joke_df, NewJoke])
    
    Joke_df

JokeCuration()
top.mainloop()