#----- IMPORTS -----
# Imports the required external libaries and modules used throughout the program.

#--- Requests ---
# Allows for the retrieving of external data sets / API's
import requests

#--- Pandas ---
# Is used to create data frames, and store information. Pandastable is used for displaying that information
import pandas as pd
from pandastable import Table, TableModel

#--- Tkinter ---
# Is used for creating simple GUI's that allows for faster interaction with python programs
from tkinter import *
import tkinter as tk
from tkinter import ttk

#--- CSV ---
# Is used to better manipulate CSV files from within python
import csv

#--- OS ---
# Is used to allow programs to better interact with systems as a whole, used in this program for directories.
import os

#--- Encryption ---
# Is used to encrypt specific data, or entire files in a range of unique formats. 
# Hashlib is used for SHA256 encrypting, while cryptopgraphy allows for encrypting entire files with a key
import hashlib
from cryptography.fernet import Fernet

#----- PROGRAM SETUP -----

#--- Colours ---
BgColour = "#32a2a8" # Sets the Background Colour to be used throughout the program
AccentColour1 = "#3bccaa" # Sets the Accent Colour to be used throughout the program

#--- Setup Login ---
Login_df = pd.read_csv('Login.csv') # Creates the Login_df pulled from the Login.csv which allows it to be used across multiple sessions

#--- Setup Tkinter ---
top = Tk() # Sets 'top' as the top level for widget in the program
top['bg'] = BgColour # Sets the background for 'top' to be the Background Colour chosen earlier

#----- JOKE PROGRAM -----
def JokeProgram():
    '''
    This function runs the Joke program window after the Login window has been used. Running this program opens a new 'main' windows, that contains the Joke Curation tab,
    the Joke Collection tab, and the Joke History tab. It also contains the code for encrypting and decrypting user collection files on opening and closing of the program.
    '''
    global JokeWindow, Joke_df, RollingJoke
    JokeWindow = Tk() # Sets 'JokeWindow' as the Top of the Program

    #------ GUI Setup ------
    JokeWindow.geometry('600x400') # Sets default Window size -=- In this case, 600 pixels wide by 400 pixels tall
    JokeWindow.title('A Funny App') # Sets App name -=- In this case, 'A Funny App'
    JokeWindow.iconbitmap('OtherFiles/AppIcon.ico') # Sets app icon -=- In this case, a laughing emoji
    
    notebook = ttk.Notebook(JokeWindow) # Defines 'notebook' to be used for creating 'Tabs' in tKinter
    notebook.pack(fill='both', expand=True) # Places the notebook in the window to take up the entire screen

    #--- Frames ---
    frame1 = Frame(notebook, width=1920, height=1080, bg=BgColour) # Creates a frame that is 1920 x 1080, and has a background colour that is the same as the whole programs
    frame2 = Frame(notebook, width=1920, height=1080) # Creates a frame that is 1920 x 1080, and has no background colour
    frame3 = Frame(notebook, width=1920, height=1080) # Creates a frame that is 1920 x 1080, and has no background colour

    frame1.pack(fill='both', expand=True) # Places Frame 1 to take up the whole screen
    frame2.pack(fill='both', expand=True) # Places Frame 2 to take up the whole screen
    frame3.pack(fill='both', expand=True) # Places Frame 3 to take up the whole screen
    
    #--- Notebook ---
    notebook.add(frame1, text='Joke Curation') # Sets reference and name for each notbook, i.e frame 1, Joke Curation
    notebook.add(frame2, text='Collections') # Sets reference and name for each notbook
    notebook.add(frame3, text='History') # Sets reference and name for each notbook
    
    #--- Unencrypt Collection ---
    try: # Try this code, if it produces an error, run except
        with open(f'Keys\{Username}.key', 'rb') as filekey: # Sets key as the User's Key
            key = filekey.read()
            
        fernet = Fernet(key) # Loads key into the Unencrypytion funciton
        
        with open(f'Users\{Username}\Collections.csv', 'rb') as enc_file: # Reads the Encrypted File
            encrypted = enc_file.read()
        
        decrypted = fernet.decrypt(encrypted) # Decrypts the Files
        
        with open(f'Users\{Username}\Collections.csv', 'wb') as dec_file: # Saves the Unencrypted file replacing the encrypted file
            dec_file.write(decrypted)
            
        Joke_df = pd.read_csv(f'Users\{Username}\Collections.csv') # Sets Joke_df/Collection Data frame to the Users Collection File
    except: 
        Joke_df = pd.read_csv(f'Collections_Default.csv')  # Sets Joke_df/Collection Data frame to the Default Collection File

    #--- Setup for Table ---
    pt = Table(frame2, dataframe=Joke_df, showtoolbar=False, showstatusbar=False, editable=False, enable_menus=False)
    # Creates a table in Frame 2 (Which takes over the entire frame), using the data from 'Joke_df', with a range of features specifically disabled

    pt.show() # Displays the Table


    def JokeCuration(): # Majority of Setup for the Widgets/Elements in the Main program
        '''
        This function runs the program that sets up different parts of GUI, and curating process. This function contains the code that sets up the history system, the API 
        functionality, and places many elements of the GUI.
        '''
        global JokeAPI, Removerow, RollingJoke, RollingJoke_df, RollingJokeTable, AddJokeButton

        Joke = tk.Label(frame1, text="Joke:", font=("Ariel", 14, "bold"), fg='white', bg=BgColour).pack(pady=(30, 5)) 
        # Displays 'Joke' title in frame 1, with 30 units of padding on the top, and 5 units on the bottom

        #--- Joke History Setup ---
        RollingJoke = [
        {'Setup': 'No History', 'Punchline': 'No History'},
        {'Setup': 'No History', 'Punchline': 'No History'}
            ]   
        
        # Creates a list with dictionaries to create a basic data table, that has two rows, and two columns, all filled with 'No History'

        RollingJoke_df = pd.DataFrame(RollingJoke) # Converts the basic data table to a pandas dataframe

        for i in range(0,3): # Runs 3 times (0, 1, 2)
            try:
                JokeAPI = requests.get('https://joke.deno.dev/') # Sets JokeAPI to the JSON file at the end of that link (Is reset each time to get a new joke)
                NewRollingJoke_df = {'Setup': JokeAPI.json()['setup'], 'Punchline': JokeAPI.json()['punchline']}
                # Creates a new DF with the same columns, but a row, filled with the information from the JSON file retrieved from the API file
            except:
                NewRollingJoke_df = {'Setup': f'Error 404 - API Not Responding', 'Punchline': f'Please use the Non-API Functions'}
                # If the API File doesn't respond, replace the information in the table with the an error code which will be presented to the User
            
            RollingJoke_df.loc[len(RollingJoke_df)] = NewRollingJoke_df
            # Adds the New dataframe to the end of the old one

            RollingJoke_df = RollingJoke_df.reset_index(drop=True)
            # Resets the index of the new combined dataframe

        RollingJokeTable = Table(frame3, dataframe=RollingJoke_df, showtoolbar=False, showstatusbar=False, editable=False, enable_menus=False)
        # Creates a table in Frame 3 (Which takes over the entire frame), using the data from 'RollingJoke_df', with a range of features specifically disabled

        RollingJokeTable.show() # Displays the Table

        #--- Rolling Joke Button Frame ---
        # Creates a new dataframe inside of a grid space, allowing me to place multiple elements per grid space, which I used to better align the buttons next to the respective row they affected
        RollingButtonFrame = tk.Frame(frame3, bg=BgColour)
        RollingButtonFrame.grid(column=2, row=1, sticky='n')

        def AddJokeButton(): # Allows me to replace the buttons ontop after redrawing the updated table
            # Creates a new button to add each joke from the Users history to the collection
            AddJokeButton1 = tk.Button(RollingButtonFrame, text="Add Joke (1)", font=("Arial", 10, "bold"), width=20, cursor="hand2", command=lambda: [Collections(RollingJoke_df.iloc[0]["Setup"], RollingJoke_df.iloc[0]["Punchline"])]).pack(side="top")
            AddJokeButton2 = tk.Button(RollingButtonFrame, text="Add Joke (2)", font=("Arial", 10, "bold"), width=20, cursor="hand2", command=lambda: [Collections(RollingJoke_df.iloc[1]["Setup"], RollingJoke_df.iloc[1]["Punchline"])]).pack(side="top")
            AddJokeButton3 = tk.Button(RollingButtonFrame, text="Add Joke (3)", font=("Arial", 10, "bold"), width=20, cursor="hand2", command=lambda: [Collections(RollingJoke_df.iloc[2]["Setup"], RollingJoke_df.iloc[2]["Punchline"])]).pack(side="top")
            AddJokeButton4 = tk.Button(RollingButtonFrame, text="Add Joke (4)", font=("Arial", 10, "bold"), width=20, cursor="hand2", command=lambda: [Collections(RollingJoke_df.iloc[3]["Setup"], RollingJoke_df.iloc[3]["Punchline"])]).pack(side="top")
            AddJokeButton5 = tk.Button(RollingButtonFrame, text="Add Joke (5)", font=("Arial", 10, "bold"), width=20, cursor="hand2", command=lambda: [Collections(RollingJoke_df.iloc[4]["Setup"], RollingJoke_df.iloc[4]["Punchline"])]).pack(side="top")

        def DisplayJokes(): # Displays a new Joke, and updates the history
            global JokeAPI, RollingJoke_df
            try:
                JokeAPI = requests.get('https://joke.deno.dev/') # Sets JokeAPI to the JSON file at the end of that link (Is reset each time to get a new joke)
                NewRollingJoke_df = ({'Setup': JokeAPI.json()['setup'], 'Punchline': JokeAPI.json()['punchline']})
                # Creates a new basic dictionary with the same columns as the main Joke and Rolling Joke Dataframe, but a row, filled with the information from the JSON file retrieved from the API file

            except:
                NewRollingJoke_df = ({'Setup': f'Error 404 - API Not Responding', 'Punchline': f'Please use the Non-API Functions'})
                # If the API File doesnt respond, replace the information in the table with the an error code which will be presented to the User
            
            RollingJoke_df = pd.concat([RollingJoke_df.iloc[1:], pd.DataFrame([NewRollingJoke_df])], ignore_index=True)
            # Adds the New dataframe to the end of the old one, removing the first row of the old data frame, then reseting the index

            JokeDisplaySetup.config(text = JokeAPI.json()['setup']) # Used to by - RollingJoke_df.iloc[2]['Setup'], but it would then present jokes that the users discarded from their collection
            JokeDisplayPunchline.config(text = JokeAPI.json()['punchline']) # Used to be - RollingJoke_df.iloc[2]['Punchline']

            JokeDisplaySetup.pack(pady=2) # Displays the new Setup for the joke to the User
            JokeDisplayPunchline.pack(pady=2) # Displays the new Punchline for the joke to the User
            
            try: 
                RollingJokeTable.destroy() # Delets the Old Table
            except:
                pass

            RollingJokeTable = Table(frame3, dataframe=RollingJoke_df, showtoolbar=False, showstatusbar=False, editable=False, enable_menus=False)
            RollingJokeTable.show() # Redraws the table with the Updated Data in it
            
            AddJokeButton() # Replaces the Add Joke Buttons ontop of the Table

        JokeDisplaySetup = tk.Label(frame1, text="", font=("Ariel", 10, "bold"), fg='white', bg=BgColour) # Sets the Joke Display Setup to be changed later with the new jokes
        JokeDisplayPunchline = tk.Label(frame1, text="", font=("Ariel", 10, "bold"), fg='white', bg=BgColour) # Sets the Joke Display Punchline to be changed later with the new jokes
            
        DisplayJokes() # Runs the Display Jokes Program which updates the above Labels with the new jokes, along with preforming the other tasks

        #--- Button Frame ---
        # Creates a new frame to allow the Store joke and Discard Joke to be placed next to eachother
        ButtonFrame = tk.Frame(frame1, bg=BgColour)
        ButtonFrame.pack(pady=10, anchor="center")
        
        # If the Button is Pressed, it Send the Current Joke to the Collections Function, being displayed inside of the newly created button frame
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
        
        # If the Button is Pressed, it runs the 'Get New Joke Button' and discards it to the history, being displayed inside of the newly created button frame
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
        
        tk.Label(frame1, text="---------------------------", bg=BgColour).pack(pady=5) # Divider that Seperates the Joke API function from the Collection Function

        Collection = tk.Label(frame1, text="Collection:", font=("Ariel", 14, "bold"), fg='white', bg=BgColour).pack(pady=5)
        # Displays the Collecion Title

        CollectionDisplaySetup = tk.Label(frame1, text="", font=("Ariel", 10, "bold"), fg='white', bg=BgColour) # Sets the Collection Joke Display Setup to be changed later with the Random Collection Joke Function
        CollectionDisplayPunchline = tk.Label(frame1, text="", font=("Ariel", 10, "bold"), fg='white', bg=BgColour) # Sets the Collection Joke Display Punchline to be changed later with the Random Collection Joke Function

        # Displays the Random Joke From the Collection
        CollectionDisplaySetup.pack(pady=2) 
        CollectionDisplayPunchline.pack(pady=2)

        def RandomCollectionJoke():
            try:
                CollectionJoke_df.iloc[:0] # Resets the 'CollectionJoke_df' to be empty
            except:
                pass
            CollectionJoke_df = Joke_df.sample(n=1) # Gets a random Joke from Joke_df and adds it to CollectionJoke_df

            CollectionDisplaySetup.config(text=CollectionJoke_df.iloc[0,0]) # Sets the Label to the Setup for the Random Joke
            CollectionDisplayPunchline.config(text=CollectionJoke_df.iloc[0,1]) # Sets the Label to the Punchline for the Random Joke

            CollectionDisplaySetup.pack(pady=2) # Displays the Random Joke's Setup
            CollectionDisplayPunchline.pack(pady=2) # Displays the Random Joke's Punchline

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
        # If the Button is Pressed, it runs the Random Collection Joke Function
        CollectionJoke.pack(pady=10) # Displays the Button

        tk.Label(frame1, text="---------------------------", bg=BgColour).pack(pady=5) # Divider that Seperates the Collection function from the Manually add Joke Function

        ManualJoke = tk.Label(frame1, text="Add Joke:", font=("Ariel", 14, "bold"), fg='white', bg=BgColour).pack(pady=5) # Title for Manually Add Jokes to the collection

        SetupInput = tk.Entry(frame1, width=40, fg="grey", font=("Arial", 10, "italic"), justify="center")
        SetupInput.insert(0, "Setup") # Sets the text in the Setup field to be 'Setup'

        SetupInput.bind("<FocusIn>", lambda e: SetupInput.delete(0, tk.END) and SetupInput.config(fg="black") if SetupInput.get() == "Setup" else SetupInput.config(fg="grey"))
        # If the user clicks on the Textbox space, and the text in it is 'Setup', it deletes it, and sets the typing colour to black

        SetupInput.bind("<FocusOut>", lambda e: SetupInput.insert(0, "Setup") and SetupInput.config(fg="grey") if SetupInput.get() == "" else SetupInput.config(fg="black"))
        # If the user leaves the Textbox space, and the text in it is ''(Nothing), it adds 'Setup' back into the box, and sets the colour to grey, indicating its field isn't filled in

        SetupInput.bind("<KeyRelease>", lambda e: SetupInput.config(fg="black") if SetupInput.get() != "Setup" else SetupInput.config(fg="grey"))
        # If the User clicks a key, and the field is not filled in with 'Setup', it sets the colour to black, otherwise it is set to grey, indicating it is not filled in
        SetupInput.pack(pady=2) # Displays the Setup Input field underneath the previous element

        PunchlineInput = tk.Entry(frame1, width=40, fg="grey", font=("Arial", 10, "italic"), justify="center")
        PunchlineInput.insert(0, "Punchline") # Sets the text in the Punchline field to be 'Punchline'

        PunchlineInput.bind("<FocusIn>", lambda e: PunchlineInput.delete(0, tk.END) and PunchlineInput.config(fg="black") if PunchlineInput.get() == "Punchline" else PunchlineInput.config(fg="grey"))
        # If the user clicks on the Textbox space, and the text in it is 'Punchline', it deletes it, and sets the typing colour to black

        PunchlineInput.bind("<FocusOut>", lambda e: PunchlineInput.insert(0, "Punchline") and PunchlineInput.config(fg="grey") if PunchlineInput.get() == "" else PunchlineInput.config(fg="black"))
        # If the user leaves the Textbox space, and the text in it is ''(Nothing), it adds 'Punchline' back into the box, and sets the colour to grey, indicating its field isn't filled in

        PunchlineInput.bind("<KeyRelease>", lambda e: PunchlineInput.config(fg="black") if PunchlineInput.get() != "Punchline" else PunchlineInput.config(fg="grey"))
        # If the User clicks a key, and the field is not filled in with 'Punchline', it sets the colour to black, otherwise it is set to grey, indicating it is not filled in
        PunchlineInput.pack(pady=2) # Displays the Punchline Input field underneath the previous element

        AddJokeButton = tk.Button(frame1, text="Add Joke", font=("Arial", 10, "bold"), width=20, cursor="hand2", command=lambda: [Collections(SetupInput.get(), PunchlineInput.get()), SetupInput.delete(0, tk.END), PunchlineInput.delete(0, tk.END)])
        AddJokeButton.pack(pady=2)

        def Removerow(): # This Function removes a row from the users collection, then it adds the removed row to the histroy, to fix any mistakes later
            global RemoveRow # Globalises RemoveRow
            RemoveRow = tk.Entry(frame2, width = 5) # Entry Widget to Type in the Row Number for deleting
        
            RemoveRow.grid(column=1, row=0, sticky=E, padx=12) 
            # Places the Textbox in the header row, sticking it to the left hand side (Closer to the Button) with 12 pixels of padding.

            RemoveJoke = tk.Button(frame2, # If the Button is clicked, it runs Removerow()
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
            RemoveJoke.grid(column=2, row=0)  # Places the Button on the margins of the Table (Above the scroll bar)

            def Drop_Row(): # This funciton on command removes a selected row
                global Joke_df, RollingJoke_df # Globalises Joke_df and RollingJoke_df
                try:
                    RowNotFound.destroy() # If their is an error message, resets it to blank
                except:
                    pass

                try:
                    NewRollingJoke_df = pd.DataFrame([{
                        'Setup': str(Joke_df.iloc[int(RemoveRow.get()) - 1]['Setup']),
                        'Punchline': str(Joke_df.iloc[int(RemoveRow.get()) - 1]['Punchline'])
                    }]) # Creates a new dataframe with the Joke present in the row about to be removed
                    
                    RollingJoke_df = pd.concat([RollingJoke_df.iloc[1:], NewRollingJoke_df], ignore_index=True)
                    # Adds the removed joke to the Users history, while also removing the oldest joke there

                    RollingJoke_df = RollingJoke_df.reset_index(drop=True) # Resets the index of the History Dataframe

                    Joke_df = Joke_df.drop(index=(int(RemoveRow.get()) - 1)).reset_index(drop=True) # Removes the joke from the Users collection and resets the index
                    try:
                        pt.destroy() # Destroys the Collection Joke Table
                    except:
                        pass
                    pt = Table(frame2, dataframe=Joke_df, showtoolbar=False, showstatusbar=False, editable=False, enable_menus=False)
                    pt.show() # Redraws the Collections table with the updated data

                    try:
                        RollingJokeTable.destroy() # Destroys the History Joke Table
                    except:
                        pass

                    RollingJokeTable = Table(frame3, dataframe=RollingJoke_df, showtoolbar=False, showstatusbar=False, editable=False, enable_menus=False)
                    RollingJokeTable.show() # Redraws the History table with the updated data

                except:
                    RowNotFound = tk.Label(frame2, text="Error - Row Not Found - Please Try Again", fg="Red").place(x=0, y=0)
                    # If their is an issue with removing the Row, prints an error message
                
        Removerow() # Runs Remove row to display the elements setup there

    def Collections(Setup, Punchline): # Adds joke to Collection
        global Joke_df, NewJoke, pt
            
        Setup.join(Setup.splitlines()) # Joins split lines to simplify the storing process

        NewJoke = {
        "Setup": Setup, 
        "Punchline": Punchline
        } # Makes a dictionary with the Joke data from the parameters

        # Inserting the new row
        Joke_df.loc[len(Joke_df)] = NewJoke # Adds the new jokes to the Collection dataframe

        # Reset the index
        Joke_df = Joke_df.reset_index(drop=True) # Resets the collection dataframe index
        
        try:
            pt.destroy() # Destroys the previous Collectionstable
        except:
            pass
        
        pt = Table(frame2, dataframe=Joke_df, showtoolbar=False, showstatusbar=False, editable=False, enable_menus=False)
        pt.show() # Redraws the table
        Removerow() # Redisplays the buttons ontop of the tables
        
    def SaveUpdates(): # Runs this Function instead of closing when pressing the 'X' button
        global JokeWindow, Joke_df, Username
        try: # If filepath exists, store the Collection dataframe at Collection.CSV underneath the user folder
            Joke_df.to_csv(path_or_buf=f'Users\{Username}\Collections.csv', index=False) # Stores file at the User directory

        except: # If filepath doesnt exist, create the filepath, then save it at Collection.CSV underneath the user folder
            Userfolder = f"Users"  # Sets Userfolder as 'Users'
            file_path_user = os.path.join(Userfolder, f"{Username}") # Creates directory combining Userfolder, and 'Username'
            os.makedirs(file_path_user, exist_ok=True) # Makes filepath

            Joke_df.to_csv(path_or_buf=f'Users\{Username}\Collections.csv', index=False) # Stores Collection.csv at the newly created Collection
        
        directory = "Keys"  # This is the folder where keys will be stored
        file_path = os.path.join(directory, f"{Username}.key")  # Define the key directory for the individual user

        os.makedirs(directory, exist_ok=True) # If the directory doesn't exist, makes it, else, it moves on

        with open(file_path, 'rb') as filekey: # Reads the Key and sets key as the Users key
            key = filekey.read()
        
        fernet = Fernet(key) # Defines the key into the Unencryption function

        with open(f'Users\{Username}\Collections.csv', 'rb') as file: # Reads the Users collection file
            original = file.read()
            
        encrypted = fernet.encrypt(original) # Encrypts the Collections files
        
        with open(f'Users\{Username}\Collections.csv', 'wb') as encrypted_file: # Saves the collections File
            encrypted_file.write(encrypted)
            
        try:
            JokeWindow.destroy() # Closes the Joke Program
        except:
            pass
        try:
            top.destroy() # Closes the Login Program
        except:
            pass
        
    JokeWindow.protocol('WM_DELETE_WINDOW', SaveUpdates) # Replaces the 'X' button with the Save Updates function

    JokeCuration() # Runs Joke Curation Program

#----- LOGIN PROGRAM -----
def Login(): # Runs the Entire Login Window
    global Username, UsernameInput, PasswordInput # Sets 3 Variables to be referenced and used throughout the Program
    
    #--- Setup for Window ---
    top.geometry('250x400') # Size of Window -=- In this case, 250 pixels wide, and 400 tall, allowing the entire Controls to be viewed
    top.title('A Funny App Login') # Name of Windows -=- In this case, 'A Funny App Login'
    top.iconbitmap('OtherFiles/AppIcon.ico') # App icon of Window -=- In this case, A laughing face emoji

    HidePassword = tk.BooleanVar(value=True) # Sets the Hide Password 'tKinter Integer' to True, hiding the Password by default
    
    # --- Login Section ---
    tk.Label(top, text="Login", font=("Ariel", 14, "bold"), fg='white', bg=BgColour).pack(pady=(10, 5)) # Displays the Login Title at the Top of the screen with 10 units of padding on the top, and 5 units on the bottom

    ErrorMessage = tk.Label(top, text='', fg="red", bg=BgColour, font=("Arial", 10,)) # Displays a blank error message spot which can be configured to show an error later
    ErrorMessage.place(x=0,y=0) # Places the blank error message at the top left of the screen

    #--- Username Input ---
    UsernameInput = tk.Entry(top, width=25, fg="grey", font=("Arial", 10, "italic"), justify="center") # Displays a textbox for the User to enter their existing username
    UsernameInput.insert(0, "Username") # Sets the text in the Username field to be 'Username'

    UsernameInput.bind("<FocusIn>", lambda e: UsernameInput.delete(0, tk.END) and UsernameInput.config(fg="black") if UsernameInput.get() == "Username" else None) 
    # If the user clicks on the Textbox space, and the text in it is 'Username', it deletes it, and sets the typing colour to black

    UsernameInput.bind("<FocusOut>", lambda e: UsernameInput.insert(0, "Username") and UsernameInput.config(fg="grey") if UsernameInput.get() == "" else None)
    # If the user leaves the Textbox space, and the text in it is ''(Nothing), it adds 'Username' back into the box, and sets the colour to grey, indicating its field isn't filled in

    UsernameInput.bind("<KeyRelease>", lambda e: UsernameInput.config(fg="black") if UsernameInput.get() != "Username" else UsernameInput.config(fg="grey"))
    # If the User clicks a key, and the field is not filled in with 'Username', it sets the colour to black, otherwise it is set to grey, indicating it is not filled in
    UsernameInput.pack(pady=2) # Displays the Username Input field underneath the Title


    PasswordInput = tk.Entry(top, width=25, fg="grey", font=("Arial", 10, "italic"), justify="center", show="*")
    PasswordInput.insert(0, "Password") # Sets the text in the Password field to be 'Password'

    PasswordInput.bind("<FocusIn>", lambda e: (PasswordInput.delete(0, tk.END) and PasswordInput.config(fg="black")) if PasswordInput.get() == "Password" else None, (PasswordInput.config(show='*') if HidePassword.get() else None))
    # If the user clicks on the Textbox space, and the text in it is 'Password', it deletes it, and sets the typing colour to black

    PasswordInput.bind("<FocusOut>", lambda e: (PasswordInput.insert(0, "Password") and PasswordInput.config(fg="grey")) if PasswordInput.get() == "" else None, (PasswordInput.config(show='*') if HidePassword.get() else None))
    # If the user leaves the Textbox space, and the text in it is ''(Nothing), it adds 'Password' back into the box, and sets the colour to grey, indicating its field isn't filled in

    PasswordInput.bind("<KeyRelease>", lambda e: PasswordInput.config(fg="black") if PasswordInput.get() != "Password" else PasswordInput.config(fg="grey"))
    # If the User clicks a key, and the field is not filled in with 'Password', it sets the colour to black, otherwise it is set to grey, indicating it is not filled in
    PasswordInput.pack(pady=2) # Displays the field underneath the previous element

    ShowPassword = tk.Checkbutton(top, text="Hide Password", variable=HidePassword, onvalue=True, offvalue=False, command=lambda: ((PasswordInput.config(show='*') if HidePassword.get() else PasswordInput.config(show='')), (PasswordCreateInput.config(show='*') if HidePassword.get() else PasswordCreateInput.config(show=''))), fg='white', bg=BgColour, selectcolor='Darkslategrey')
    ShowPassword.pack(pady=2) # Displays the field underneath the previous element

    LoginButton = tk.Button(top, text="Login", font=("Arial", 10, "bold"), width=20, bg=AccentColour1, cursor="hand2", command=lambda: [Account(UsernameInput.get(), PasswordInput.get(), False)])
    # Adds a 'Login Button', that sends the data from the Entry Fields to the Account Function, also stating that the data has not yet been processed (Hashed and Condenced) via the 'False' atribute at the end
    LoginButton.pack(pady=2) # Displays the field underneath the previous element
    
    tk.Label(top, text="---------------------------", bg=BgColour).pack(pady=5) # Adds a divider between Login and Create Account

    # --- Create Account Section ---
    tk.Label(top, text="Create Account", font=("Arial", 14, "bold"), fg='white', bg=BgColour).pack(pady=(5, 5))

    UsernameCreateInput = tk.Entry(top, width=25, fg="grey", font=("Arial", 10, "italic"), justify="center")
    UsernameCreateInput.insert(0, "Create Username") # Sets the text in the Create Username field to be 'Create Username'

    UsernameCreateInput.bind("<FocusIn>", lambda e: UsernameCreateInput.delete(0, tk.END) and UsernameCreateInput.config(fg="black") if UsernameCreateInput.get() == "Create Username" else None)
    # If the user clicks on the Textbox space, and the text in it is 'Create Username', it deletes it, and sets the typing colour to black
    
    UsernameCreateInput.bind("<FocusOut>", lambda e: UsernameCreateInput.insert(0, "Create Username") and UsernameCreateInput.config(fg="grey") if UsernameCreateInput.get() == "" else None)
    # If the user leaves the Textbox space, and the text in it is ''(Nothing), it adds 'Create Username' back into the box, and sets the colour to grey, indicating its field isn't filled in
    
    UsernameCreateInput.bind("<KeyRelease>", lambda e: UsernameCreateInput.config(fg="black") if UsernameCreateInput.get() != "Create Username" else UsernameCreateInput.config(fg="grey"))
    # If the User clicks a key, and the field is not filled in with 'Create Username', it sets the colour to black, otherwise it is set to grey, indicating it is not filled in
    UsernameCreateInput.pack(pady=2) # Displays the field underneath the previous element

    PasswordCreateInput = tk.Entry(top, width=25, fg="grey", font=("Arial", 10, "italic"), justify="center", show="*")
    PasswordCreateInput.insert(0, "Create Password") # Sets the text in the Create Password field to be 'Create Password'

    PasswordCreateInput.bind("<FocusIn>", lambda e: (PasswordCreateInput.delete(0, tk.END) and PasswordCreateInput.config(fg="black")) if PasswordCreateInput.get() == "Create Password" else None, (PasswordCreateInput.config(show='*') if HidePassword.get() else None))
    # If the user clicks on the Textbox space, and the text in it is 'Create Password', it deletes it, and sets the typing colour to black

    PasswordCreateInput.bind("<FocusOut>", lambda e: (PasswordCreateInput.insert(0, "Create Password") and PasswordCreateInput.config(fg="grey")) if PasswordCreateInput.get() == "" else None, (PasswordCreateInput.config(show='*') if HidePassword.get() else None))
    # If the user leaves the Textbox space, and the text in it is ''(Nothing), it adds 'Create Password' back into the box, and sets the colour to grey, indicating its field isn't filled in

    PasswordCreateInput.bind("<KeyRelease>", lambda e: PasswordCreateInput.config(fg="black") if PasswordCreateInput.get() != "Create Password" else PasswordCreateInput.config(fg="grey"))
    # If the User clicks a key, and the field is not filled in with 'Create Password', it sets the colour to black, otherwise it is set to grey, indicating it is not filled in
    PasswordCreateInput.pack(pady=2) # Displays the field underneath the previous element

    CreateShowPassword = tk.Checkbutton(top, text="Hide Password", variable=HidePassword, onvalue=True, offvalue=False, command=lambda: ((PasswordInput.config(show='*') if HidePassword.get() else PasswordInput.config(show='')), (PasswordCreateInput.config(show='*') if HidePassword.get() else PasswordCreateInput.config(show=''))), fg='white', bg=BgColour, selectcolor='Darkslategrey')
    CreateShowPassword.pack(pady=2) # Displays the field underneath the previous element

    CreateAccountButton = tk.Button(top, text="Create Account", font=("Arial", 10, "bold"), width=20, bg=AccentColour1, cursor="hand2", command=lambda: [CreateAccount(UsernameCreateInput.get(), PasswordCreateInput.get())])
    CreateAccountButton.pack(pady=2) # Displays the field underneath the previous element
    
    
    def Account(User, Pass, Logedin): # This function handles Logging into the Software
        global Username # Globalises the Username Attribute Accross the program to be used in other functions
        if Logedin == False: # If the data has not been processed
            
            User = User.join(User.splitlines()) # Connects Lines together, removing Line breaks from the inputs
            User = User.replace(" ", "") # Replaces ' ' with '' (Nothing), ensuring their is no future issues with file creating etc
            User = User.replace("/", "") # Replaces '/' with '' (Nothing), ensuring their is no future issues with file creating etc
            User = User.replace("\\", "") # Replaces '\' with '' (Nothing), ensuring their is no future issues with file creating etc
            User = User.replace("*", "") # Replaces '*' with '' (Nothing), ensuring their is no future issues with file creating etc
            User = User.replace('"', "") # Replaces '"' with '' (Nothing), ensuring their is no future issues with file creating etc
            User = User.replace("'", "") # Replaces ''' with '' (Nothing), ensuring their is no future issues with file creating etc
            User = User.replace(":", "") # Replaces ':' with '' (Nothing), ensuring their is no future issues with file creating etc
            User = User.replace('|', "") # Replaces '|' with '' (Nothing), ensuring their is no future issues with file creating etc
            User = User.replace("?", "") # Replaces '?' with '' (Nothing), ensuring their is no future issues with file creating etc
            
            
            Pass = Pass.join(Pass.splitlines()) # Connects Lines together, removing Line breaks from the inputs

            Pass = hashlib.sha256(Pass.encode()).hexdigest() # Converts it to a SHA-256 sting, which cannot be converted back into a password

            # By storing passwords with this level of encryption, it ensures it cannot be converted back into a password, and ultimately, cause someone to log into someone elses account by looking through the files
        
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
        global Login_df # Globalises Login_df to be updated across other Functions
        
        Username = Username.join(Username.splitlines())  # Connects Lines together, removing Line breaks from the inputs

        Username = Username.replace(" ", "")  # Replaces ' ' with '' (Nothing), ensuring their is no future issues with file creating etc
        Username = Username.replace("/", "") # Replaces '/' with '' (Nothing), ensuring their is no future issues with file creating etc
        Username = Username.replace("\\", "") # Replaces '\' with '' (Nothing), ensuring their is no future issues with file creating etc
        Username = Username.replace("*", "") # Replaces '*' with '' (Nothing), ensuring their is no future issues with file creating etc
        Username = Username.replace('"', "") # Replaces '"' with '' (Nothing), ensuring their is no future issues with file creating etc
        Username = Username.replace("'", "") # Replaces ''' with '' (Nothing), ensuring their is no future issues with file creating etc
        Username = Username.replace(":", "") # Replaces ':' with '' (Nothing), ensuring their is no future issues with file creating etc
        Username = Username.replace('|', "") # Replaces '|' with '' (Nothing), ensuring their is no future issues with file creating etc
        Username = Username.replace("?", "") # Replaces '?' with '' (Nothing), ensuring their is no future issues with file creating etc

        Password = Password.join(Password.splitlines()) # Connects Lines together, removing Line breaks from the inputs

        Password = hashlib.sha256(Password.encode()).hexdigest() # Converts it to a SHA-256 sting, which cannot be converted back into a password

        with open('Login.csv', mode='r') as file: # Opens Login.csv in read mode
            reader = csv.reader(file) # Opens the Login in CSV Reader
            for row in reader: # For each row in Login.csv
                User = row[0] # Reads the first column of each row
                if User == Username: # Checks if Username is the same as the stored one
                    UsernameTaken = True # Sets Username taken to True
                    UsernameCreateInput.delete(0, tk.END) # Clears the Username Create
                    PasswordCreateInput.delete(0, tk.END) # Clears the Password Create
                    break # Leaves the Loop
                else:
                    UsernameTaken = False # Sets Username taken to False

        if UsernameTaken == False: # If Username is not taken
        
            NewLogin = {
            "Username": Username, 
            "Password": Password, 
            }
            # Makes a New Dictionary with the Username and Password

            Login_df.loc[len(Login_df)] = NewLogin # Adds the new login information to the Login dataframe

            Login_df = Login_df.reset_index(drop=True) # Resets the Index for the Login Dataframe

            Login_df.to_csv(path_or_buf='Login.csv', index=False) # Adds the New Login to the Login CSV File
            
            Account(Username, Password, True) # Runs the Account Function, Entering in the Username, Password, With the True meaning it is already condenced, filtered, and hashed

        else:
            ErrorMessage.config(text='Error - Username Taken') # Displays a Errormessage that the Username is taken


#----- Saves Updates to Account ---
def SaveUpdatesTop(): # Replaces the 'X' button for the top window with the commands inside of this function
    global JokeWindow, Joke_df
    try: # Try to run these commands, if presented with an error, run except
        JokeWindow.destroy() # Closes JokeWindow Window
    except:
        pass # Move on / Do nothing
    try:
        top.destroy() # Closes Login Window
    except:
        pass # Move on / Do nothing
    
top.protocol('WM_DELETE_WINDOW', SaveUpdatesTop) # Replaces the 'X' button for the top window with the command 'SaveUpdatesTop'

Login() # Runs the Login Function which places the elements/widgets on the login screen
    
top.mainloop() # Starts the GUI by opening the top window