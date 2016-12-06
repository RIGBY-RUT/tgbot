# -*- coding: utf-8 -*-
import array
import telebot
from datetime import date, time
import urllib.request as urllib2
import const
from telebot import types
import logging

global poz, kod, god, groop
bot = telebot.TeleBot(const.token)  # poluchenie tokena

print(bot.get_me())  # vivod informacii o bote

# настройки для журнала
logger = logging.getLogger('log')
logger.setLevel(logging.INFO)
fh = logging.FileHandler('someTestBot.log')
fh.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s | %(levelname)-7s | %(message)s")
fh.setFormatter(formatter)
logger.addHandler(fh)


@bot.message_handler(commands=['start', 'help'])  # privetstvie
def send_welcome(start):
    bot.send_message(start.chat.id, const.helo_text)



@bot.message_handler(commands=["table_offline"])  # Офлайн расписание
def table_offline(message):
    keyboard = types.InlineKeyboardMarkup()
    url = const.url_pic_download
    urllib2.urlretrieve(url, )
    img = open(const.name_pic_download, 'rb')
    bot.send_chat_action(message.from_user.id, 'upload_photo')
    bot.send_photo(message.from_user.id, img)
    img.close()
    url_button = types.InlineKeyboardButton(text="Расписание офлайн",
                                            url=const.url_exel)
    keyboard.add(url_button)
    bot.send_message(message.chat.id, "Нажми на кнопку и скачай ", reply_markup=keyboard)


@bot.message_handler(commands=["table"])  # выбокра
def callback_data(message0):
    keyboard = types.InlineKeyboardMarkup()
    button = types.InlineKeyboardButton(text="ИНБ", callback_data="ИНБ")
    button1 = types.InlineKeyboardButton(text="ПИН", callback_data="ПИН")
    keyboard.add(button, button1)
    bot.send_message(message0.chat.id, "Привет! Нажми на кнопку и... ИДИ НАХУЙ, ПИДР", reply_markup=keyboard)

    keyboard1 = types.InlineKeyboardMarkup()
    button = types.InlineKeyboardButton(text="2016", callback_data="2016")
    button1 = types.InlineKeyboardButton(text="2015", callback_data="2015")
    keyboard1.add(button, button1)
    bot.send_message(message0.chat.id, "Привет! Нажми на кнопку и... ИДИ НАХУЙ, ПИДР", reply_markup=keyboard1)

    keyboard2 = types.InlineKeyboardMarkup()
    button = types.InlineKeyboardButton(text="1", callback_data="1")
    button1 = types.InlineKeyboardButton(text="2", callback_data="2")
    keyboard2.add(button, button1)
    bot.send_message(message0.chat.id, "Привет! Нажми на кнопку и... ИДИ НАХУЙ, ПИДР", reply_markup=keyboard2)



@bot.callback_query_handler(func=lambda call: True)
def callback_1(call):
    global kod, god, groop
    poz = int

    while str(call.data) == "ИНБ" or "ПИН":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=call.data)
        kod = call.data

        poz = (poz, "a")


    while str(call.data) == "2016" or "2015":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=call.data)
        god = call.data
        poz = (poz, "a")

    while str(call.data) == "1" or "2":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=call.data)
        groop = call.data
        poz = (poz, "a")

    if int(poz) == 'aaa':
        sum = (kod, god, groop)
        bot.send_message(call.chat.id, sum)






#@bot.message_handler(commands=["lol"])
#def sumcod(sum):
#    sum = (kod, god, groop)
#    bot.send_message(sum.chat.id, sum)


if __name__ == '__main__':
    bot.polling(none_stop=True)
