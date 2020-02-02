import sys
import slack
import time
import urllib.request
import json

#Takes in a message.
def echo(message, chan):
    #Check what type it read
    command = '!echo'
    cLen = len(command)
    if message.get('type') == 'message':
        text = message.get('text')
        if text[0:cLen] == command and len(text) > cLen:
            #Echo to chat
            client.chat_postMessage(channel = chan, text = text[cLen:])

def weather(message, chan, wToken):
    #Check what type it read
    command = '!weather'
    cLen = len(command)
    weatherAPI = 'https://api.openweathermap.org/data/2.5/weather?q='
    if message.get('type') == 'message':
        text = message.get('text')
        if text[0:cLen] == command and len(text) > cLen:
            inputs = text[cLen:].split()
            if len(inputs) == 1:
                city = inputs[0]
                wData = urllib.request.urlopen(weatherAPI + city + '&APPID=' + wToken)
                print(wData)
            client.chat_postMessage(channel = chan, text = 'big test')

#Read file
f = open('token.txt', 'r')
token = f.read()
f.close()

f = open('weather.txt', 'r')
wToken = f.read()
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
    echo(latest, '#general')
    weather(latest, '#general', wToken)
    #STOP SPAMMING THE SERVER HARD!
    time.sleep(2)
