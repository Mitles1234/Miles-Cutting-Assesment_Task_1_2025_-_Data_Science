import requests


RollingJoke = [
            ['',''],
            ['',''],
            ['',''],
            ['',''],
            ['','']
        ]

for i in range(0,5):
    try:
        JokeAPI = requests.get('https://joke.deno.dev/')
        RollingJoke[i][0] = JokeAPI.json()['setup']
        RollingJoke[i][1] = JokeAPI.json()['punchline']
    except:
        RollingJoke[i][0] = f'Error 404 - API Not Responding'
        RollingJoke[i][1] = f'Please use the Non-API Functions'

print(RollingJoke)
def DisplayJokes():
    global JokeAPI
    JokeAPI = requests.get('https://joke.deno.dev/')
    try:
        JokeAPI = requests.get('https://joke.deno.dev/')
        RollingJoke.append([{JokeAPI.json()['setup']}, {JokeAPI.json()['punchline']}])
    except:
        RollingJoke.append([f'Error 404 - API Not Responding', f'Please use the Non-API Functions'])
    
    RollingJoke.pop(0)

    print(RollingJoke[2][0])
    print(RollingJoke[2][1])

DisplayJokes()