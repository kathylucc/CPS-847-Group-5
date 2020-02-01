import sys
import slack

#Read file
f = open('token.txt', 'r')
token = f.read()
f.close()

#General server and bot ID
general = 'CT5KL1G3X'
botId = 'UTDKZ9F6U'

#Connect to server
client = slack.WebClient(token)

while True:
    #Fetch history of general chat
    history = client.conversations_history(channel = 'CT5KL1G3X')
    messages = history.get('messages')
    latest = messages[0]

    if latest.get('type') == 'message':
        text = latest.get('text')
        if text[0:5] == '!echo' and len(text) > 6:
            client.chat_postMessage(channel = '#general', text = text[5:])
