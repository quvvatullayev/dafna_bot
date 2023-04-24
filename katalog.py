from telegram import (
    InlineKeyboardButton, 
    InlineKeyboardMarkup, 
    ReplyKeyboardMarkup, 
    ReplyKeyboardRemove,
    KeyboardButton,
    Update,
    )
from telegram.ext import (
    CallbackQueryHandler,
    CommandHandler,
    MessageHandler,
    Filters,
    Updater,
)
from telegram.ext import (
    CallbackContext,
)
from db import DB
db = DB()

def katalog(update:Update, callback:CallbackContext):
    id = update.effective_chat.id
    bot = callback.bot
    data:dict = db.katalog()
    keyboard = []
    for i in data['katalogs']:
        keyboard.append([InlineKeyboardButton(text=i['name'],callback_data=f"product_{i['id']}")])
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    bot.send_message(
        chat_id=id,
        text="Katalogdan mahsulot tanlang",
        reply_markup=reply_markup,
    )