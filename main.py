#--- Imports ---
import requests
import pandas as pd
from tkinter import *

import tkinter as tk
from tkinter import ttk

#--- Setup Collections ---
Joke_df = pd.read_csv('Collections.csv')

#--- API ---
JokeAPI = requests.get('https://api.jokes.one/jod?category=knock-knock')

#------ GUI Setup ------
top = Tk()
top.geometry('600x400')s
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

ThumbsUp = Radiobutton(frame1, text='Albury', variable=ChoiceLocation, value='Albury', cursor="hand2", command=Graph)