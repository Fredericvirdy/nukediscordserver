import requests
from read import read

count = 0
invite = input("Enter the server's invite link: ")

tokens = read("tokens.txt").split()
for line in tokens:
    currtok = tokens[count]
    headers = {
        'authorization':currtok,
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
    }
    r = requests.post(f"htpps://discordapp.com/api/v6/invites/{invite}", headers=headers)
    count = count + 1