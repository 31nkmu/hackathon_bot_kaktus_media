import telebot
import csv
from MyToken import token
from telebot import types
from parsing import *


bot = telebot.TeleBot(token)
choice = types.InlineKeyboardMarkup()
btn1 = types.InlineKeyboardButton('Description', callback_data='description')
btn2 = types.InlineKeyboardButton('Photo', callback_data='photo')
btn3 = types.InlineKeyboardButton('quit', callback_data='quit')
choice.add(btn1, btn2, btn3)
num_of_new = 0


@bot.message_handler(commands=['start'])
def start(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, 'Hello, I\'m bot for news')


@bot.message_handler(content_types=['text'])
def list_news(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, get_list_news())
    msg = bot.send_message(chat_id, 'Выберите номер новости')
    bot.register_next_step_handler(msg, new)


def new(c):
    global num_of_new
    chat_id = c.chat.id
    num_of_new = int(c.text)
    bot.send_message(chat_id, 'Some title news you can see Description of this news and Photo', reply_markup=choice)


@bot.callback_query_handler(func=lambda c: True)
def get_description_or_photo(c):
    chat_id = c.message.chat.id
    if c.data == 'description':
        bot.send_message(chat_id, get_one_new(num_of_new))
    elif c.data == 'photo':
        bot.send_message(chat_id, get_photo(num_of_new))
    elif c.data == 'quit':
        bot.send_message(chat_id, 'До свидания')


bot.polling()
