"""
WOP Bot - Soll fragen oder Pflichten stellen, später auch selbst aufnehmen können
"""

import pickle
import time
import telebot
from datetime import datetime
from random import *
zzahl = randint(1, 300)

bot_token = '1649275793:AAEyRgLK_GNFHoSO9ww82yuFAXc1OcQMXgk'

bot = telebot.TeleBot(bot_token)

bot.can_join_groups = True

truths=dict()
duties=dict()
rooms=dict()
rathers=dict()
i_have_nevers=dict()

class Categories:
    categories = ['/wahrheit', '/pflicht', '/i_have_never', '/who', '/who_would_rather']

    a_truth = 0
    b_duties = 0
    c_i_have = 0
    d_who = 0
    w = 0
    c = 0

auf = Categories()

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
    w = list(truths.keys())
    # debug
    # print(w)
    rand = randint(0, len(w) - 1)
    truth = w[rand]
    bot.reply_to(message,truth)


# Pflicht

@bot.message_handler(commands=['pflicht'])
def send_dutie(message):
    w = list(duties.keys())
    # debug
    # print(w)
    rand = randint(0, len(w) - 1)
    dutie = w[rand]
    bot.reply_to(message,dutie)

# Ich habe noch nie

@bot.message_handler(commands=['i_have_never'])
def send_i_have_never(message):
    w = list(i_have_nevers.keys())
    # debug
    # print(w)
    rand = randint(0, len(w) - 1)
    never = w[rand]
    bot.reply_to(message, never)

# Wer im Raum?

@bot.message_handler(commands=['who'])
def send_who_in_the_room(message):
    w = list(rooms.keys())
    # debug
    # print(w)
    rand = randint(0, len(w) - 1)
    room = w[rand]
    bot.reply_to(message, room)


# Wer würde eher...?

@bot.message_handler(commands=['who_would_rather'])
def who_would_rather(message):
    w = list(rathers.keys())
    # debug
    # print(w)
    rand = randint(0, len(w) - 1)
    rather = w[rand]
    bot.reply_to(message,rather)

@bot.message_handler(commands=['wop', 'WoP'])
def next_one(message):
    bot.reply_to(message, auf.categories[randint(0, len(auf.categories)-1)])

# Add Questions and Duties

@bot.message_handler(commands=['add_truth'])
def add_truth(message):
    try:
        try_out = str(message.text.split()[0])
        if not try_out == '/add_truth@WahrheitOP_bot':
            truth2 = str(message.text[11:])
            if truth2 in truths:
                bot.reply_to(message, 'Frage ist schon gespeichert!')
            elif truth2 == '':
                bot.reply_to(message,'Du musst eine Frage angeben!')
            else:
                num = 1
                truths[truth2] = 'Truth'+str(num)
                num = num+1
                with open('Wahrheiten.pkl','wb') as f:
                    pickle.dump(truths,f,pickle.HIGHEST_PROTOCOL)
                bot.send_message(message.chat.id, "Erfolgreich hinzugefügt ✅")
                return num
        else:
            truth2 = str(message.text[26:])
            if truth2 in truths:
                bot.reply_to(message, 'Frage ist schon gespeichert!')
            elif truth2 == '':
                bot.reply_to(message, 'Du musst eine Frage angeben!')
            else:
                num = 1
                truths[truth2] = 'Truth' + str(num)
                num = num + 1
                with open('Wahrheiten.pkl', 'wb') as f:
                    pickle.dump(truths, f, pickle.HIGHEST_PROTOCOL)
                bot.send_message(message.chat.id, "Erfolgreich hinzugefügt ✅")
                return num
    except Exception as e:
        bot.reply_to(message, 'Fehler: ' + str(e))

@bot.message_handler(commands=['add_dutie'])
def add_truth(message):
    try:
        try_out = str(message.text.split()[0])
        if not try_out == '/add_dutie@WahrheitOP_bot':
            dutie2 = str(message.text[11:])
            if dutie2 in duties:
                bot.reply_to(message, 'Frage ist schon gespeichert!')
            elif dutie2 == '':
                bot.reply_to(message,'Du musst eine Frage angeben!')
            else:
                num = 1
                duties[dutie2] = 'Truth'+str(num)
                num = num+1
                with open('Pflichten.pkl','wb') as f:
                    pickle.dump(duties,f,pickle.HIGHEST_PROTOCOL)
                bot.send_message(message.chat.id, "Erfolgreich hinzugefügt ✅")
                return num
        else:
            dutie2 = str(message.text[26:])
            if dutie2 in duties:
                bot.reply_to(message, 'Frage ist schon gespeichert!')
            elif dutie2 == '':
                bot.reply_to(message, 'Du musst eine Frage angeben!')
            else:
                num = 1
                duties[dutie2] = 'Truth' + str(num)
                num = num + 1
                with open('Pflichten.pkl', 'wb') as f:
                    pickle.dump(duties, f, pickle.HIGHEST_PROTOCOL)
                bot.send_message(message.chat.id, "Erfolgreich hinzugefügt ✅")
                return num
    except Exception as e:
        bot.reply_to(message, 'Fehler: ' + str(e))

@bot.message_handler(commands=['add_room'])
def add_truth(message):
    try:
        try_out = str(message.text.split()[0])
        if not try_out == '/add_room@WahrheitOP_bot':
            room2 = str(message.text[10:])
            if room2 in rooms:
                bot.reply_to(message, 'Frage ist schon gespeichert!')
            elif room2 == '':
                bot.reply_to(message,'Du musst eine Frage angeben!')
            else:
                num = 1
                rooms[room2] = 'Truth'+str(num)
                num = num+1
                with open('Rooms.pkl','wb') as f:
                    pickle.dump(rooms,f,pickle.HIGHEST_PROTOCOL)
                bot.send_message(message.chat.id, "Erfolgreich hinzugefügt ✅")
                return num
        else:
            room2 = str(message.text[25:])
            if room2 in rooms:
                bot.reply_to(message, 'Frage ist schon gespeichert!')
            elif room2 == '':
                bot.reply_to(message, 'Du musst eine Frage angeben!')
            else:
                num = 1
                rooms[room2] = 'Truth' + str(num)
                num = num + 1
                with open('Rooms.pkl', 'wb') as f:
                    pickle.dump(rooms, f, pickle.HIGHEST_PROTOCOL)
                bot.send_message(message.chat.id, "Erfolgreich hinzugefügt ✅")
                return num
    except Exception as e:
        bot.reply_to(message, 'Fehler: ' + str(e))

@bot.message_handler(commands=['add_rather'])
def add_truth(message):
    try:
        try_out = str(message.text.split()[0])
        if not try_out == '/add_rather@WahrheitOP_bot':
            rather2 = str(message.text[12:])
            if rather2 in rathers:
                bot.reply_to(message, 'Frage ist schon gespeichert!')
            elif rather2 == '':
                bot.reply_to(message,'Du musst eine Frage angeben!')
            else:
                num = 1
                rathers[rather2] = 'Truth'+str(num)
                num = num+1
                with open('Rathers.pkl','wb') as f:
                    pickle.dump(rathers,f,pickle.HIGHEST_PROTOCOL)
                bot.send_message(message.chat.id, "Erfolgreich hinzugefügt ✅")
                return num
        else:
            rather2 = str(message.text[27:])
            if rather2 in rathers:
                bot.reply_to(message, 'Frage ist schon gespeichert!')
            elif rather2 == '':
                bot.reply_to(message, 'Du musst eine Frage angeben!')
            else:
                num = 1
                rathers[rather2] = 'Truth' + str(num)
                num = num + 1
                with open('Rathers.pkl', 'wb') as f:
                    pickle.dump(rathers, f, pickle.HIGHEST_PROTOCOL)
                bot.send_message(message.chat.id, "Erfolgreich hinzugefügt ✅")
                return num
    except Exception as e:
        bot.reply_to(message, 'Fehler: ' + str(e))

@bot.message_handler(commands=['add_never'])
def add_truth(message):
    try:
        try_out = str(message.text.split()[0])
        if not try_out == '/add_never@WahrheitOP_bot':
            never2 = str(message.text[11:])
            if never2 in i_have_nevers:
                bot.reply_to(message, 'Frage ist schon gespeichert!')
            elif never2 == '':
                bot.reply_to(message,'Du musst eine Frage angeben!')
            else:
                num = 1
                i_have_nevers[never2] = 'Truth'+str(num)
                num = num+1
                with open('ich_hab_noch_nie.pkl','wb') as f:
                    pickle.dump(i_have_nevers,f,pickle.HIGHEST_PROTOCOL)
                bot.send_message(message.chat.id, "Erfolgreich hinzugefügt ✅")
                return num
        else:
            never2 = str(message.text[26:])
            if never2 in i_have_nevers:
                bot.reply_to(message, 'Frage ist schon gespeichert!')
            elif never2 == '':
                bot.reply_to(message, 'Du musst eine Frage angeben!')
            else:
                num = 1
                i_have_nevers[never2] = 'Truth' + str(num)
                num = num + 1
                with open('ich_hab_noch_nie.pkl', 'wb') as f:
                    pickle.dump(i_have_nevers, f, pickle.HIGHEST_PROTOCOL)
                bot.send_message(message.chat.id, "Erfolgreich hinzugefügt ✅")
                return num
    except Exception as e:
        bot.reply_to(message, 'Fehler: ' + str(e))

# Tests^^

@bot.message_handler(commands=['print_last_truth'])
def print_last_truth(message):
    bot.reply_to(message, truths[-1])

with open('Wahrheiten.pkl', 'rb') as f:
    truths = pickle.load(f)
with open('Pflichten.pkl', 'rb') as f:
    duties = pickle.load(f)
with open('ich_hab_noch_nie.pkl', 'rb') as f:
    i_have_nevers = pickle.load(f)
with open('Rooms.pkl', 'rb') as f:
    rooms = pickle.load(f)
with open('Rathers.pkl', 'rb') as f:
    rathers = pickle.load(f)

while True:
    try:
        print("Start Polling     "+str(datetime.now()))
        bot.polling()
    except Exception as e:
        print("Error, retry in 5s ..." + str(e)+'     '+str(datetime.now()))
        time.sleep(5)
