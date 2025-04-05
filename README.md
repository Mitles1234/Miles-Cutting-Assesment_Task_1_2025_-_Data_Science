# Joke Program

This Python program allows you to retrieve a Joke from a external API, then allowing the user to store, remove, or manually add jokes to their private collection. The program recieves data from either the API, which is retrieved through the `requests` libary, or jokes entered by the user. This data is entered into dataframes through the `pandas` module, which keeps it accessible while the program is running. Then it uses `tkinter` and `pandastable` to display the infomation to the user. While this is happening, `os` and `csv`, work to convert the data into formats that will stay accross sessions of the program, with `hashlib` and `Fernet` ensuring that while they are stored, they remain private to the user.

## Features
- Retrieves a range of Joke's from a External API, with lots of varience, providing hundreds of fun times and laughs.
- Allows you to easily and effectively sort through the Jokes from the Joke API for later use.
- Stores the Jokes in secured collections file, allowing for them to be viewed at anytime, only by you.
- Hear a Hilarious Joke? Think of a Funny Joke? Add your own custom jokes to your collection.
- Get random jokes from your collection so you can make sure the joke you get will be funny.

## Requirements
To run this program, you need to install the following dependencies:

- `requests` to make HTTP requests to the joke API.
- `pandas` to store the joke data entered by the user and from the API.
- `tkinter` to create a visually appealing GUI that makes it faster, and simpler to interact with the program.
- `pandastable` to visualise the stored data from pandas, in the tkinter GUI.
- `hashlib` to secure the login information for every account, ensuring maximum security.
- `csv` to convert data into a long term storage type, ensuring data transfers from one session to another.
- `os` is used to make the program better interact with the system as a whole.
- `Fernet` is used to encrypt all the data tied to each user, ensuring that it remains secure, and protected.

### Install dependencies
To install the required dependencies, you can run:

```bash
pip install -r requirements.txt