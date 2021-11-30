import requests
from telebot import types

import telebot

token = '1963961669:AAHnA3c_lPfoqWi_4Q4nboJhC7Ct6KCIYN0' # توكن
sudo = 1688598446 # ايدي
bot = telebot.TeleBot(token)

def ex_id(id):
    result = False
    file = open('users.txt', 'r')
    for line in file:
        if line.strip() == id:
            result = True
    file.close()
    return result
@bot.message_handler(commands=['ch'])
def start(message):
    first = message.from_user.first_name
    bot.send_message(message.chat.id, text=f"*Welcome {first}To My Bot 😃\nCH: @NUMNUMH \nBot : @SajadToolsBot \nMaler Bot : @MakerToolsBot *",parse_mode="markdown")

@bot.message_handler(commands=['start'])
def start(message):
    file = open('users.txt', 'r')
    li = len(file.readlines())
    file.close()
    if message.chat.type == 'private':
        idu = message.from_user.id
        f = open('users.txt', 'a')
        if (not ex_id(str(idu))):
            f.write(f"{idu}\n")
            f.close()
    file = open('users.txt', 'r')
    markup_inline = types.InlineKeyboardMarkup()
    sendfile = types.InlineKeyboardButton(text='Send List 📁', callback_data='file')
    brod = types.InlineKeyboardButton(text='Broadcast 📢', callback_data='brod')
    count = types.InlineKeyboardButton(text=f'Count users {li}', callback_data='count')
    emt = types.InlineKeyboardButton(text=f'', callback_data='emt')
    sendmm = types.InlineKeyboardButton(text=f'Send Message to some one 📩', callback_data='smo')
    markup_inline.row_width = 2
    markup_inline.add(sendfile, brod, count, emt, sendmm)
    li = len(file.readlines())
    idd = message.from_user.id

    if idd == sudo:
        bot.send_message(sudo, text='Hi boss\n\n'
                         , parse_mode='markdown', reply_markup=markup_inline)

    first = message.from_user.first_name
    bot.send_message(message.chat.id, text='*Hi  🚀\nsend a message*\n/ch\n'
                f'`The bot programmed Python`'
                     , parse_mode='markdown')


@bot.callback_query_handler(func=lambda call: True)
def answer(call):
    if call.data == 'file':
        files(call.message)

    elif call.data == 'brod':
        mesgg = bot.send_message(call.message.chat.id, text='*Send Message 📢 :*', parse_mode='markdown')
        bot.register_next_step_handler(mesgg, broddd)
    elif call.data == 'smo':
        mesgg = bot.send_message(call.message.chat.id, text='*Send ID :*', parse_mode='markdown')
        bot.register_next_step_handler(mesgg, iddd)


def iddd(message):
    iddd = message.text
    length = bot.send_message(message.chat.id, text='🔢 Send Message 📩 :')
    bot.register_next_step_handler(length, smo, iddd)


def smo(message, iddd):
    msg = message.text
    bot.send_message(iddd, text=f'*{msg}*', parse_mode='markdown')
    bot.send_message(sudo, text=f'*تم ارسال الرساله بنجاح ✅*', parse_mode='markdown')


def broddd(message):
    mes = message.text
    readd = open('users.txt', 'r')
    for idu in readd:
        bot.send_message(idu, text=f'*{mes}*', parse_mode='markdown')
    bot.send_message(sudo, text=f'*تم عمل اذاعة بنجاح ✅*', parse_mode='markdown')


def files(message):
    file = open('users.txt', 'rb')
    bot.send_document(message.chat.id, file)


@bot.message_handler(func=lambda m: True)
def check(message):
    username = message.from_user.username
    msg = message.text
    idd = message.from_user.id
    bot.forward_message(sudo, message.chat.id, message.message_id)
    bot.send_message(sudo, text='*{}*'.format(msg), parse_mode='markdown')
    bot.send_message(sudo, text=f'*Text : {msg}\n\n*'
                                f'*Username : @{username}*\n\n'
                                f'ID : `{idd}`', parse_mode='markdown')
    bot.send_message(message.chat.id, text=f'*تم ارسال الرساله بنجاح ✅*', parse_mode='markdown')


while True:
    try:
        bot.polling(none_stop=True)
    except Exception as ex:
        telebot.logger.error(ex)
