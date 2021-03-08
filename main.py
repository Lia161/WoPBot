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


def json_write(datta, filename='WoP.json'):
    with open(filename, 'w') as f:
        json.dump(datta, f, indent=4)


while True:
    with open('WoP.json') as file:
        data = json.load(file)


    @bot.message_handler(commands=['start'])
    def start(message):
        bot.reply_to(message, "Hi, ich bin der Wahrheit oder Pflicht Bot")


    @bot.message_handler(commands=['help'])
    def help_message(message):
        bot.reply_to(message,
                     "Ich bin ein Wahrheit oder Pflicht - Bot. Mit folgenden Befehlen wählt ihr die verschiedenen Fragen/Aufgabentypen aus:\n\n"
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
                     f"Es gibt insgesamt:\n{str(len(data['Tasks']['Truth']))} Wahrheitsfragen,\n{len(data['Tasks']['Dare'])} Pflicht-Aufgaben, \n{len(data['Tasks']['Never'])} Ich hab noch nie Fragen, \n{len(data['Tasks']['Rather'])} Wer würde eher Fragen, \n{len(data['Tasks']['Room'])} Wer im Raum Fragen.\n"
                     f"Insgesamt also {len(data['Tasks']['Truth']) + len(data['Tasks']['Dare']) + len(data['Tasks']['Never']) + len(data['Tasks']['Rather']) + len(data['Tasks']['Room'])} Fragen.")


    # Wahrheit
    @bot.message_handler(commands=['wahrheit'])
    def send_truth_message(message):
        w = data["Tasks"]["Truth"]
        rand = randint(0, len(w) - 1)
        truth = w[rand]
        bot.reply_to(message, truth)


    # Pflicht
    @bot.message_handler(commands=['pflicht'])
    def send_dutie(message):
        w = data["Tasks"]["Dare"]
        rand = randint(0, len(w) - 1)
        dutie = w[rand]
        bot.reply_to(message, dutie)


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
        bot.reply_to(message, rather)


    @bot.message_handler(commands=['wop', 'WoP'])
    def next_one(message):
        bot.reply_to(message, data["Categories"][randint(0, len(data["Categories"]) - 1)])


    # Add Questions and Duties
    @bot.message_handler(commands=['add_truth'])
    def add_truth(message):
        try:
            text = message.reply_to_message.text
            for i in data["Tasks"]:
                if text not in i["Truth"]:
                    i["Truth"].append(text)
                    bot.reply_to(message, "Erfolgreich hinzugefügt ✅")
                else:
                    bot.reply_to(message, "Text schon hinzugefügt!")
        except AttributeError:
            try:
                command = len(message.text.split()[0]) + 1
                text = message.text[command:]
                for i in data["Tasks"]:
                    if text not in i["Truth"]:
                        i["Truth"].append(text)
                        bot.reply_to(message, "Erfolgreich hinzugefügt ✅")
                    else:
                        bot.reply_to(message, "Text schon hinzugefügt!")
            except ValueError:
                bot.reply_to(message, "Du musst einen Text angeben oder auf eine Nachricht antworten!")
            except Exception as e:
                bot.reply_to(message, "Irgendwas ist schiefgelaufen.")
                print(e)
        json_write(data)


    @bot.message_handler(commands=['add_dutie', 'add_dare'])
    def add_dutie(message):
        try:
            text = message.reply_to_message.text
            for i in data["Tasks"]:
                if text not in i["Dare"]:
                    i["Dare"].append(text)
                    bot.reply_to(message, "Erfolgreich hinzugefügt ✅")
                else:
                    bot.reply_to(message, "Text schon hinzugefügt!")
        except AttributeError:
            try:
                command = len(message.text.split()[0]) + 1
                text = message.text[command:]
                for i in data["Tasks"]:
                    if text not in i["Dare"]:
                        i["Dare"].append(text)
                        bot.reply_to(message, "Erfolgreich hinzugefügt ✅")
                    else:
                        bot.reply_to(message, "Text schon hinzugefügt!")
            except ValueError:
                bot.reply_to(message, "Du musst einen Text angeben oder auf eine Nachricht antworten!")
            except Exception as e:
                bot.reply_to(message, "Irgendwas ist schiefgelaufen.")
                print(e)
        json_write(data)


    @bot.message_handler(commands=['add_room'])
    def add_room(message):
        try:
            text = message.reply_to_message.text
            for i in data["Tasks"]:
                if text not in i["Room"]:
                    i["Room"].append(text)
                    bot.reply_to(message, "Erfolgreich hinzugefügt ✅")
                else:
                    bot.reply_to(message, "Text schon hinzugefügt!")
        except AttributeError:
            try:
                command = len(message.text.split()[0]) + 1
                text = message.text[command:]
                for i in data["Tasks"]:
                    if text not in i["Room"]:
                        i["Room"].append(text)
                        bot.reply_to(message, "Erfolgreich hinzugefügt ✅")
                    else:
                        bot.reply_to(message, "Text schon hinzugefügt!")
            except ValueError:
                bot.reply_to(message, "Du musst einen Text angeben oder auf eine Nachricht antworten!")
            except Exception as e:
                bot.reply_to(message, "Irgendwas ist schiefgelaufen.")
                print(e)
        json_write(data)


    @bot.message_handler(commands=['add_rather'])
    def add_rather(message):
        try:
            text = message.reply_to_message.text
            for i in data["Tasks"]:
                if text not in i["Rather"]:
                    i["Rather"].append(text)
                    bot.reply_to(message, "Erfolgreich hinzugefügt ✅")
                else:
                    bot.reply_to(message, "Text schon hinzugefügt!")
        except AttributeError:
            try:
                command = len(message.text.split()[0]) + 1
                text = message.text[command:]
                for i in data["Tasks"]:
                    if text not in i["Rather"]:
                        i["Rather"].append(text)
                        bot.reply_to(message, "Erfolgreich hinzugefügt ✅")
                    else:
                        bot.reply_to(message, "Text schon hinzugefügt!")
            except ValueError:
                bot.reply_to(message, "Du musst einen Text angeben oder auf eine Nachricht antworten!")
            except Exception as e:
                bot.reply_to(message, "Irgendwas ist schiefgelaufen.")
                print(e)
        json_write(data)


    @bot.message_handler(commands=['add_never'])
    def add_never(message):
        try:
            text = message.reply_to_message.text
            for i in data["Tasks"]:
                for t in i["Never"]:
                    if t == text:
                        bot.reply_to(message, "Text schon hinzugefügt!")
                    else:
                        i["Never"].append(text)
                        bot.reply_to(message, "Erfolgreich hinzugefügt ✅")
        except AttributeError:
            try:
                command = len(message.text.split()[0]) + 1
                text = message.text[command:]
                for i in data["Tasks"]:
                    for t in i["Never"]:
                        if t == text:
                            bot.reply_to(message, "Text schon hinzugefügt!")
                        else:
                            i["Never"].append(text)
                            bot.reply_to(message, "Erfolgreich hinzugefügt ✅")
            except ValueError:
                bot.reply_to(message, "Du musst einen Text angeben oder auf eine Nachricht antworten!")
            except Exception as e:
                bot.reply_to(message, "Irgendwas ist schiefgelaufen.")
                print(e)
        json_write(data)


    try:
        print("Start Polling     " + str(datetime.now()))
        bot.polling()
    except Exception as e:
        print("Error, retry in 1s ..." + str(e) + '     ' + str(datetime.now()))
        time.sleep(1)
