from telegram.ext import Updater
updater=Updater(token='1634806032:AAGTbHGWYYzcbF7PAHWZMK3fmt9RS2Sm8SI', use_context=True)
dispatcher=updater.dispatcher
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot!")

def stop(update, context):
    updater.idle()

from telegram.ext import CommandHandler
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
stop_handler = CommandHandler('stop', stop)
dispatcher.add_handler(stop_handler)

def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

from telegram.ext import MessageHandler, Filters
echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
dispatcher.add_handler(echo_handler)

updater.start_polling()