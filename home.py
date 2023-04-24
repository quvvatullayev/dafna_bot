from telegram import (
    InlineKeyboardButton, 
    InlineKeyboardMarkup, 
    ReplyKeyboardMarkup, 
    ReplyKeyboardRemove,
    KeyboardButton,
    Update,
    )
from telegram.ext import (
    CallbackContext,
)

from db import DB

db = DB()

def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    id = update.effective_chat.id
    bot = context.bot

    reply_markup = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="🛍Katalog"),KeyboardButton(text="Kontakt📲")]
        ],
        resize_keyboard=True,
    )
    bot.send_message(
        chat_id=id,
        text="Assalomu alaykum, sizga qanday yordam bera olaman?",
        reply_markup=reply_markup,
    )