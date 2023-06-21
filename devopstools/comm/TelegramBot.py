# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import telebot

bot = telebot.TeleBot(
    "<Token>", parse_mode=None)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.reply_to(message, "Howdy, how are you doing?")


@bot.message_handler(commands=['help'])
def help_message(message):
    bot.reply_to(message, "What do you want me to do?")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)


bot.infinity_polling()
