import requests
while True:
    try:
        joke = requests.get(f'https://joke.deno.dev/')
        print(joke.json()['setup'], joke.json()['punchline'])
    except:
        print(f"Error - Joke Not Found")
    input()