import telebot
import os

API_TOKEN = os.environ.get("BOT_TOKEN")

if not API_TOKEN:
    raise ValueError("BOT_TOKEN not set!")

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Bot Live on Render 🚀")

@bot.message_handler(func=lambda message: True)
def echo(message):
    bot.reply_to(message, "You said: " + message.text)

print("Bot Started...")
bot.infinity_polling()
