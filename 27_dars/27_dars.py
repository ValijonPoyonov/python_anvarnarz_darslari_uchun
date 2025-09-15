import telebot
from transliterate import to_cyrillic,to_latin
TOKEN = "7859684527:AAFkawGFz2h_hm01abNqeeg926q_ouoKXg8"
bot = telebot.TeleBot(TOKEN,parse_mode=None)

@bot.message_handler(func=lambda message: True)
def reaction(message):
    answer = "Assalom alaykum, xush kelibsiz! "
    answer += "Istalgan matn kiriting, matn lotincha bo'lsa kirilchaga, "
    answer += "kirilcha bo'lsa lotinchaga o'girib beraman."
    xabar = message.text
    if xabar.isascii():
        answer1 = to_cyrillic(xabar)
    else:
        answer1 = to_latin(xabar)
    bot.reply_to(message, answer1)
bot.polling()