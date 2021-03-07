"""
WOP Bot - Soll fragen oder Pflichten stellen, später auch selbst aufnehmen können
"""

import json
import time
import telebot
from datetime import datetime
from random import *
zzahl = randint(1, 300)

bot_token = '1649275793:AAEyRgLK_GNFHoSO9ww82yuFAXc1OcQMXgk'

bot = telebot.TeleBot(bot_token)

bot.can_join_groups = True

while True:
    def json_write(datta, filename='WoP.json'):
        with open(filename) as f:
            json.dump(datta, f, indent=4)
    with open('WoP.json') as file:
        data = json.load(file)

    @bot.message_handler(commands=['start'])
    def start(message):
        bot.reply_to(message, "Hi, ich bin der Wahrheit oder Pflicht Bot")

    @bot.message_handler(commands=['help'])
    def help_message(message):
        bot.reply_to(message, "Ich bin ein Wahrheit oder Pflicht - Bot. Mit folgenden Befehlen wählt ihr die verschiedenen Fragen/Aufgabentypen aus:\n\n"
                              "mit /wahrheit wird eine zufällige Wahrheits-Frage ausgewählt. Wenn du einen Username angibst geht die Frage direkt an die Person.\n"
                              "mit /pflicht wird eine zufällige Pflicht-Aufgabe ausgewählt (Hinweis: Die meisten sind nicht während Corona machbar).Wenn du einen Username angibst geht die Frage direkt an die Person.\n"
                              "mit /i_have_never wird eine zufällige 'Ich hab noch nie'-Frage ausgewählt.\n"
                              "mit /who wird eine zufällige 'Wer im Raum...?'-Frage ausgewählt.\n"
                              "mit /who_would_rather wird eine zufällige 'Wer würde eher...?'-Frage ausgewählt.\n"
                              "mit /next wird eine zufällige Kategorie der oben aufgezählten Kategorien genannt.\n\n"
                              "Wenn ihr mehr Fragen habt, könnt ihr die mit folgenden Befehlen hinzufügen:\n\n"
                              "/add_truth - Wahrheit hinzufügen\n"
                              "/add_dutie - Pflicht hinzufügen\n"
                              "/add_never - 'Ich hab noch nie' hinzufügen\n"
                              "/add_room - 'Wer im Raum' hinzufügen\n"
                              "/add_rather - 'Wer würde eher' hinzufügen\n"
                              "Viel Spaß!\n\n" 
                              "Es gibt insgesamt:\n" + str(len(truths)) + " Wahrheitsfragen,\n" + str(len(duties)) + " Pflicht-Aufgaben,\n" + str(len(rooms)) + " Wer im Raum...?-Fragen,\n" + str(len(i_have_nevers)) + " Ich hab noch nie... - Fragen,\n" + str(len(rathers)) + " Wer würde eher...?-Fragen.")

    # Wahrheit
    @bot.message_handler(commands=['wahrheit'])
    def send_truth_message(message):
        w = data["Tasks"]["Truth"]
        rand = randint(0, len(w) - 1)
        truth = w[rand]
        bot.reply_to(message,truth)

    # Pflicht
    @bot.message_handler(commands=['pflicht'])
    def send_dutie(message):
        w = data["Tasks"]["Dare"]
        rand = randint(0,len(w)-1)
        dutie = w[rand]
        bot.reply_to(message,dutie)

    # Ich habe noch nie
    @bot.message_handler(commands=['i_have_never'])
    def send_i_have_never(message):
        w = data["Tasks"]["Never"]
        rand = randint(0, len(w) - 1)
        never = w[rand]
        bot.reply_to(message, never)

    # Wer im Raum?
    @bot.message_handler(commands=['who'])
    def send_who_in_the_room(message):
        w = data["Tasks"]["Room"]
        rand = randint(0, len(w) - 1)
        room = w[rand]
        bot.reply_to(message, room)

    # Wer würde eher...?
    @bot.message_handler(commands=['who_would_rather'])
    def who_would_rather(message):
        w = data["Tasks"]["Rather"]
        rand = randint(0, len(w) - 1)
        rather = w[rand]
        bot.reply_to(message,rather)

    @bot.message_handler(commands=['wop', 'WoP'])
    def next_one(message):
        bot.reply_to(message, data["Categories"][randint(0, len(data["Categories"])-1)])

    # Add Questions and Duties
    @bot.message_handler(commands=['add_truth'])
    def add_truth(message):
        try:
            text = message.reply_to_message.text
            data["Tasks"]["Truth"].append(text)
        except AttributeError:
            try:
                command = message.text.split()[0]+1
                text = message.text[command:]
                data["Tasks"]["Truth"].append(text)
            except Exception as e:
                bot.reply_to(message, "Irgendwas ist schiefgelaufen.")
                print(e)
        json_write(data)

    @bot.message_handler(commands=['add_dutie'])
    def add_dutie(message):
        try:
            text = message.reply_to_message.text
            data["Tasks"]["Dare"].append(text)
        except AttributeError:
            try:
                command = message.text.split()[0] + 1
                text = message.text[command:]
                data["Tasks"]["Dare"].append(text)
            except Exception as e:
                bot.reply_to(message, "Irgendwas ist schiefgelaufen.")
                print(e)
        json_write(data)

    @bot.message_handler(commands=['add_room'])
    def add_room(message):
        try:
            text = message.reply_to_message.text
            data["Tasks"]["Never"].append(text)
        except AttributeError:
            try:
                command = message.text.split()[0] + 1
                text = message.text[command:]
                data["Tasks"]["Never"].append(text)
            except Exception as e:
                bot.reply_to(message, "Irgendwas ist schiefgelaufen.")
                print(e)
        json_write(data)

    @bot.message_handler(commands=['add_rather'])
    def add_rather(message):
        try:
            text = message.reply_to_message.text
            data["Tasks"]["Rather"].append(text)
        except AttributeError:
            try:
                command = message.text.split()[0] + 1
                text = message.text[command:]
                data["Tasks"]["Rather"].append(text)
            except Exception as e:
                bot.reply_to(message, "Irgendwas ist schiefgelaufen.")
                print(e)
        json_write(data)

    @bot.message_handler(commands=['add_never'])
    def add_never(message):
        try:
            text = message.reply_to_message.text
            data["Tasks"]["Room"].append(text)
        except AttributeError:
            try:
                command = message.text.split()[0] + 1
                text = message.text[command:]
                data["Tasks"]["Room"].append(text)
            except Exception as e:
                bot.reply_to(message, "Irgendwas ist schiefgelaufen.")
                print(e)
        json_write(data)

    try:
        print("Start Polling     "+str(datetime.now()))
        bot.polling()
    except Exception as e:
        print("Error, retry in 5s ..." + str(e)+'     '+str(datetime.now()))
        time.sleep(5)
