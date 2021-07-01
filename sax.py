import os
import time
import asyncio
import telebot
from telebot import types


api = os.environ.get("BOT_TOKEN")
#api = "1853760827:AAH1twATlAeuN96f65BFtD6cqWkBDLuo8JM"

bot = telebot.TeleBot(api, False)
SUDO_USER = [1842894003, 1367789652, 1197931344]
opp = []
lop = '1. /start --> to check bot ALIVE or NOT\n2. /add <YOUR TEXT> --> To Add Poll\n3. /fuk --> Starting bot poll\n4. /clean --> To clear polls options\n5. /see --> To see avalable poll option\n6. /addsudo <USER ID> --> to give access to other user\n7. /removesudo <USER ID> -- Remove user from sudo\n8. /stopbot --> to stop the bot\n9. /sudolist --> List of sudo user\n10. /gcast <YOUR TEXT> --> brodcast the message'
type_chat = set()

@bot.message_handler(commands=['start'])
def keybo(message):
    type_chat.add(message.chat.id)
    bot.reply_to(message, 'Bot Is working!\nMy Pero Master: @ArshXxD')
    bot.reply_to(message, lop)


@bot.message_handler(commands=['fuk'])
def hkeybo(message):
    name = message.from_user.id
    if name in SUDO_USER:
        markop = types.ReplyKeyboardMarkup()
        for i in opp:
            markop.row(i)
        bot.send_message(message.chat.id, 'wow bhaiya kese kia', reply_markup=markop)
    else:
        bot.reply_to(message, 'SORRY YOU DONT HAVE ACCESS OF THIS BOT')


@bot.message_handler(commands=['add'])
def add_gu(message):
    name = message.from_user.id
    if name in SUDO_USER:
        txt = message.text[5:]
        bot.send_message(message.chat.id, 'DONE, WANNA ADD MORE IF YES TYPE "/add your  words"')
        try:
            opp.append(txt)
        except:
            pass
    else:
        bot.reply_to(message, 'SORRY YOU DONT HAVE ACCESS OF THIS BOT')


@bot.message_handler(commands=['clean'])
def cler(message):
    name = message.from_user.id
    if name in SUDO_USER:
        opp.clear()
        bot.send_message(
            message.chat.id,
            'List is clear'
        )
    else:
        bot.reply_to(message, 'SORRY YOU DONT HAVE ACCESS OF THIS BOT')


@bot.message_handler(commands=['see'])
def dekho(message):
    for i in opp:
        if i == None or i == 0:
            bot.send_message('poll is empty!')
        else:
            bot.reply_to(
                message,
                f"AVAILABLE POLL OPTION: {i}"
            )


@bot.message_handler(commands=['stopbot'])
def ending(message):
    name = message.from_user.id
    if name in SUDO_USER:
        try:
           if message.text == '/stopbot':
               markup = types.ReplyKeyboardRemove(selective=False)
               bot.send_message(message.chat.id, 'thanks for using', reply_markup=markup)
        except:
            pass
    else:
        bot.reply_to(message, 'SORRY YOU DONT HAVE ACCESS OF THIS BOT')


@bot.message_handler(commands=['addsudo'])
def remo(message):
    name = message.from_user.id
    if name in SUDO_USER:
        try:
            sexy = int(message.text[9:])
            SUDO_USER.append(sexy)
            bot.send_message(message.chat.id, 'done')
        except Exception as e:
            bot.reply_to(message, 'please input only numbers')
    else:
        bot.reply_to(message, 'SORRY YOU DONT HAVE ACCESS OF THIS BOT')


@bot.message_handler(commands=['removesudo'])
def adem(message):
    name = message.from_user.id
    if name in SUDO_USER:
        rxm = int(message.text[12:])
        try:
            SUDO_USER.remove(rxm)
            bot.reply_to(message, 'remove done')
        except Exception as e:
            bot.reply_to(message, 'please input only numbers!')
    else:
        bot.reply_to(message, 'SORRY YOU DONT HAVE ACCESS OF THIS BOT')


@bot.message_handler(commands=['sudolist'])
def lemt(message):
    name = message.from_user.id
    if name in SUDO_USER:
        for i in SUDO_USER:
            bot.reply_to(message, f"list of sudo user: {i}")


@bot.message_handler(commands=['gcast'])
def opppp(message):
    txt = message.text[7:]
    name = message.from_user.id
    if name in SUDO_USER:
        try:
            for i in type_chat:
                bot.send_message(i, txt)
                semx =+ 1
                bot.reply_to(message, f"sending to this chat {i}")
        except Exception as e:
            pass

@bot.message_handler(commands=['showg'])
def pppj(message):
    for i in type_chat:
        bot.reply_to(message, f"BOT ACTIVE IN: {i}")
        print(i)


print(type_chat)
print('nice')
bot.polling(none_stop=True)
