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

def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    id = update.effective_chat.id
    bot = context.bot

    bot.sendMessage(
        chat_id= id,
        text= "Hello, I'm a bot. Please talk to me!",
    )