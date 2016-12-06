# -*- coding: utf-8 -*-
import array
import telebot
from datetime import date, time
import urllib.request as urllib2
import const
from telebot import types
import logging
import time
import eventlet
import requests
from time import sleep

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


# -*- coding: utf-8 -*-



# Каждый раз получаем по 10 последних записей со стены
URL_VK = 'https://api.vk.com/method/wall.get?domain=c.music&count=10&filter=owner'
FILENAME_VK = 'last_known_id.txt'
BASE_POST_URL = 'https://vk.com/wall-39270586_'

BOT_TOKEN = 'токен бота, постящего в канал'
CHANNEL_NAME = '@канал'

# Если True, предполагается использование cron для запуска скрипта
# Если False, процесс запускается и постоянно висит запущенный
SINGLE_RUN = False

bot = telebot.TeleBot(BOT_TOKEN)


def get_data():
    timeout = eventlet.Timeout(10)
    try:
        feed = requests.get(URL_VK)
        return feed.json()
    except eventlet.timeout.Timeout:
        logging.warning('Got Timeout while retrieving VK JSON data. Cancelling...')
        return None
    finally:
        timeout.cancel()


def send_new_posts(items, last_id):
    for item in items:
        if item['id'] <= last_id:
            break
        link = '{!s}{!s}'.format(BASE_POST_URL, item['id'])
        bot.send_message(CHANNEL_NAME, link)
        # Спим секунду, чтобы избежать разного рода ошибок и ограничений (на всякий случай!)
        time.sleep(1)
    return


def check_new_posts_vk():
    # Пишем текущее время начала
    logging.info('[VK] Started scanning for new posts')
    with open(FILENAME_VK, 'rt') as file:
        last_id = int(file.read())
        if last_id is None:
            logging.error('Could not read from storage. Skipped iteration.')
            return
        logging.info('Previous last_id is {!s}'.format(last_id))
    try:
        feed = get_data()
        # Если ранее случился таймаут, пропускаем итерацию. Если всё нормально - парсим посты.
        if feed is not None:
            # 0 - это какое-то число, так что начинаем с 1
            entries = feed['response'][1:]
            try:
                # Если пост был закреплен, пропускаем его
                tmp = entries[0]['is_pinned']
                send_new_posts(entries[1:], last_id)
            except KeyError:
                send_new_posts(entries, last_id)
            # Записываем новую "верхушку" группы, чтобы не повторяться
            with open(FILENAME_VK, 'wt') as file:
                try:
                    tmp = entries[0]['is_pinned']
                    # Если первый пост - закрепленный, то сохраняем ID второго
                    file.write(str(entries[1]['id']))
                    logging.info('New last_id (VK) is {!s}'.format((entries[1]['id'])))
                except KeyError:
                    file.write(str(entries[0]['id']))
                    logging.info('New last_id (VK) is {!s}'.format((entries[0]['id'])))
    except Exception as ex:
        logging.error('Exception of type {!s} in check_new_post(): {!s}'.format(type(ex).__name__, str(ex)))
        pass
    logging.info('[VK] Finished scanning')
    return


if __name__ == '__main__':
    # Избавляемся от спама в логах от библиотеки requests
    logging.getLogger('requests').setLevel(logging.CRITICAL)
    # Настраиваем наш логгер
    logging.basicConfig(format='[%(asctime)s] %(filename)s:%(lineno)d %(levelname)s - %(message)s', level=logging.INFO,
                        filename='bot_log.log', datefmt='%d.%m.%Y %H:%M:%S')
    if not SINGLE_RUN:
        while True:
            check_new_posts_vk()
            # Пауза в 4 минуты перед повторной проверкой
            logging.info('[App] Script went to sleep.')
            time.sleep(60 * 4)
    else:
        check_new_posts_vk()
    logging.info('[App] Script exited.\n')


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
    poz = int

    while str(call.data) == "ИНБ" or "ПИН":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=call.data)
        const.kod = call.data

        poz = (poz, "a")


    while str(call.data) == "2016" or "2015":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=call.data)
        const.god = call.data
        poz = (poz, "a")

    while str(call.data) == "1" or "2":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=call.data)
        const.groop = call.data
        poz = (poz, "a")

    if int(poz) == 'aaa':
        sum = (const.kod, const.god, const.groop)
        bot.send_message(call.chat.id, sum)






@bot.message_handler(commands=["lol"])
def sumcod(sum):
    sum = (const.kod, const.god, const.groop)
    bot.send_message(sum.chat.id, sum)


if __name__ == '__main__':
    bot.polling(none_stop=True)
