import telebot
from telebot import types
import os

api = os.environ.get("BOT_TOKEN")
sumdoo = os.environ.get("SUDO_USER").split()
NAME = os.environ.get("OWNER_USERNAME")
reply_txt = os.environ.get("REPLY_TEXT")
bot = telebot.TeleBot(api, False)
SUDO_USER = [1842894003,1822062027]
sumdo = [int(i) for i in sumdoo]
opp = []
lop = '1. /start --> to check bot ALIVE or NOT\n2. /add <YOUR TEXT> --> To Add Poll\n3. /do --> Starting bot poll\n4. /clean --> To clear polls options\n5. /see --> To see avalable poll option\n6. /stopbot --> to stop the poll\nOWNER OF BOT: '

get_chat = set()
my_dit = []
semxy_list = set()


@bot.message_handler(commands=['start'])
def keybo(message):
    bot.reply_to(message, 'BOT IS WORKING FINE')
    bot.reply_to(message, lop + NAME)


@bot.message_handler(commands=['do'])
def hkeybo(message):
    name = message.from_user.id
    if name in sumdo:
        markop = types.ReplyKeyboardMarkup()
        for i in opp:
            markop.row(i)
        bot.send_message(message.chat.id, reply_txt, reply_markup=markop)
    else:
        bot.reply_to(message, 'CONTACT MY OWNER FOR SUDO: ' + NAME)


@bot.message_handler(commands=['add'])
def add_gu(message):
    name = message.from_user.id
    if name in sumdo:
        txt = message.text[5:]
        bot.send_message(message.chat.id, 'DONE, WANNA ADD MORE IF YES TYPE "/add your  words"')
        try:
            opp.append(txt)
        except:
            pass
    else:
        bot.reply_to(message, 'CONTACT MY OWNER FOR SUDO: ' + NAME)


@bot.message_handler(commands=['clean'])
def cler(message):
    name = message.from_user.id
    if name in sumdo:
        opp.clear()
        bot.send_message(
            message.chat.id,
            'List is clear'
        )
    else:
        bot.reply_to(message, 'CONTACT MY OWNER FOR SUDO: ' + NAME)


@bot.message_handler(commands=['see'])
def dekho(message):
    name = message.from_user.id
    if name in sumdo:
        if len(opp) == 0:
            bot.send_message(message.chat.id,'poll is empty!')
        else:
            for i in opp:
                 mess = f"Available option {i}\n"
            bot.reply_to(message, mess)
    else:
        bot.reply_to(message, 'CONTACT MY OWNER FOR SUDO: ' + NAME)


@bot.message_handler(commands=['stopbot'])
def ending(message):
    name = message.from_user.id
    if name in sumdo:
        try:
            if message.text == '/stopbot':
                markup = types.ReplyKeyboardRemove(selective=False)
                bot.send_message(message.chat.id, 'thanks for using', reply_markup=markup)
        except:
            pass
    else:
        bot.reply_to(message, 'CONTACT MY OWNER FOR SUDO: ' + NAME)




@bot.message_handler(commands=['sudolist'])
def lemt(message):
    name = message.from_user.id
    if name in sumdo:
        for i in sumdo:
            bot.send_message(message.chat.id, f"list of sudo user: {i}")
            print(i)


print('bot is starting...')
bot.polling(none_stop=True)

# JUST FAK OF
