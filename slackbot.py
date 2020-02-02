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
            #Grab that city!
            if len(inputs) == 1:
                #Grab the json returned
                city = inputs[0]
                try:
                    wData = urllib.request.urlopen(weatherAPI + city + '&units=metric&APPID=' + wToken)
                    wData = json.loads(wData.read())
                    weather = wData.get('weather')
                    main = wData.get('main')
                    #Useful data
                    condition = weather[0].get('main')
                    current = str(main.get('temp'))
                    feelsLike = str(main.get('feels_like'))
                    tMin = str(main.get('temp_min'))
                    tMax = str(main.get('temp_max'))
                    #Stringifying
                    condition = 'The current conditions: ' + condition + '\n'
                    current = 'The current temperature: ' + current + '\n'
                    feelsLike = 'It current feels like: ' + feelsLike + '\n'
                    tMin = 'The min temperature will be: ' + tMin + '\n'
                    tMax = 'The max temperature will be: ' + tMax + '\n'
                    reply = condition + current + feelsLike + tMin + tMax
                    client.chat_postMessage(channel = chan, text = reply)
                except:
                    client.chat_postMessage(channel = chan, text = 'Bad city name.')
            else:
                client.chat_postMessage(channel = chan, text = 'Invalid parameter number!')
        elif text[0:cLen] == command:
            client.chat_postMessage(channel = chan, text = 'Please give me the name of the city!')

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
