from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext

WEB_APP_URL = "https://your-webapp-url.vercel.app/"

def start(update: Update, context: CallbackContext):
    keyboard = [
        [InlineKeyboardButton("Open Form", web_app={"url": WEB_APP_URL})]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text("Welcome", reply_markup=reply_markup)

updater = Updater("7511089847:AAE6Gdq7v4jqlFiYiwVzY0XkhLAwWWBnUQo", use_context=True)
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.start_polling()

