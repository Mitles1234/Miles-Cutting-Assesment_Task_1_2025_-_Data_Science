import requests

joke = requests.get('https://joke.deno.dev/type/')

print(joke.json()['setup'], joke.json()['punchline'])