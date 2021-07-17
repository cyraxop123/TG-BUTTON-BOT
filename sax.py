import telebot
from telebot import types
import os

api = os.environ.get("BOT_TOKEN")
sumdoo = os.environ.get("SUDO_USER").split()
# sumdoo = "1842894003 1875503588".split()
#api = "1725327883:AAElGwHLQnHHFPBQN7WB6KxUXd7RpF2xFns"
bot = telebot.TeleBot(api, False)
SUDO_USER = [1842894003,1822062027]
sumdo = [int(i) for i in sumdoo]
opp = []
lop = '1. /start --> to check bot ALIVE or NOT\n2. /add <YOUR TEXT> --> To Add Poll\n3. /fuk --> Starting bot poll\n4. /clean --> To clear polls options\n5. /see --> To see avalable poll option\n6. /addsudo <USER ID> --> to give access to other user\n7. /removesudo <USER ID> -- Remove user from sudo\n8. /stopbot --> to stop the bot\n9. /sudolist --> List of sudo user\n\n10.\n11. /repo --> TO SEE REPO\n\nOWNER OF BOT:  @VENOMxEzz'
get_chat = set()
my_dit = []
semxy_list = set()


@bot.message_handler(commands=['start'])
def keybo(message):
    bot.reply_to(message, 'BOT IS WORKING FINE')
    bot.reply_to(message, lop)


@bot.message_handler(commands=['fuk'])
def hkeybo(message):
    name = message.from_user.id
    if name in sumdo:
        markop = types.ReplyKeyboardMarkup()
        for i in opp:
            markop.row(i)
        bot.send_message(message.chat.id, '@KHURANA_OP SAR HI PAMPA HAI', reply_markup=markop)
    else:
        bot.reply_to(message, 'SORRY YOU DONT HAVE ACCESS OF THIS BOT')


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
        bot.reply_to(message, 'SORRY YOU DONT HAVE ACCESS OF THIS BOT')


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
        bot.reply_to(message, 'CONTACT MY OWNER FOR SUDO: @VENOMxEzz')


@bot.message_handler(commands=['see'])
def dekho(message):
    name = message.from_user.id
    if name in sumdo:
        for i in opp:
            if i == None or i == 0:
                bot.send_message('poll is empty!')
            else:
                bot.reply_to(
                    message,
                    f"AVAILABLE POLL OPTION: {i}"
                )
    else:
        bot.reply_to(message, 'CONTACT MY OWNER FOR SUDO: @VENOMxEzz')


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
        bot.reply_to(message, 'CONTACT MY OWNER FOR SUDO: @VENOMxEzz')




@bot.message_handler(commands=['sudolist'])
def lemt(message):
    name = message.from_user.id
    if name in sumdo:
        for i in sumdo:
            bot.send_message(message.chat.id, f"list of sudo user: {i}")
            print(i)


print('nice')

bot.polling(none_stop=True)
