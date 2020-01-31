import sys
import slack
import json

token = 'xoxb-925857114054-931679321232-4fE6ypn8lLr3h7IaFqJewRhX'

general = 'CT5KL1G3X'
botId = 'UTDKZ9F6U'

client = slack.WebClient(token)

history = client.conversations_history(channel = 'CT5KL1G3X')

messages = history.get('messages')

latest = messages[0]

if latest.get('type') == 'message':
    text = latest.get('text')
    if text[0:6] == '!echo':
        client.chat_postMessage(channel = '#general', text = 'lol')
