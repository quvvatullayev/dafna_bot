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
from pprint import pprint
db = DB()

def katalog(update:Update, callback:CallbackContext):
    id = update.effective_chat.id
    bot = callback.bot
    data:dict = db.katalog()
    keyboard = []
    for i in data['katalogs']:
        keyboard.append([InlineKeyboardButton(text=i['name'],callback_data=f"katalog_{i['id']}")])
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    bot.send_message(
        chat_id=id,
        text="Katalogdan mahsulot tanlang",
        reply_markup=reply_markup,
    )

def prodouct_type(update:Update, callback:CallbackContext):
    query = update.callback_query
    product_id = query.data.split("_")[1]
    data:dict = db.get_prodouct_type(product_id)

    keyboard = []
    for i in data[0]["prodouct_typt"]:
        keyboard.append([InlineKeyboardButton(text=i['name'],callback_data=f"product_type_{i['id']}")])

    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text='Mahsulot turlaridan brini tanlang',
        reply_markup=reply_markup
    )

def prodouct(update:Update, callback:CallbackContext):
    query = update.callback_query
    id = query.data.split("_")[2]
    bot = callback.bot
    data:dict = db.get_product(id)

    db.count = list(range(len(data[0]["prodouct_type"]["prodoucts"])))
    data = data[0]["prodouct_type"]["prodoucts"][db.count[0]]
    
    bot.sendPhoto(
            chat_id=query.message.chat_id,
            photo = "https://ogabek007.pythonanywhere.com" + data['img_url'],
            caption = f"name:{data['name']} \n price:{data['price']} \n discrpition:{data['discrpition']}\n color:{data['color']}\n manufacturer:{data['manufacturer']}\n material:{data['material']}",
            reply_markup=InlineKeyboardMarkup([
                            [InlineKeyboardButton(text="Orqaga⏮", callback_data="back"),
                            InlineKeyboardButton(text="Buyurtma🛒", callback_data=f"buyurtma_{data['id']}"), 
                            InlineKeyboardButton(text="Oldnga⏭", callback_data=f"next_{data['id']}_{id}")
                            ]])
            )

    l = db.count
    if len(l) >= 1:
        db.count = l[1:]

  
def next_prodouct(update:Update, callback:CallbackContext):
    query = update.callback_query
    id = query.data.split("_")[2]
    bot = callback.bot
    data:dict = db.get_product(id)

    data = data[0]["prodouct_type"]["prodoucts"][db.count[0]]   
    bot.sendPhoto(
            chat_id=query.message.chat_id,
            photo = "https://ogabek007.pythonanywhere.com" + data['img_url'],
            caption = f"name:{data['name']} \n price:{data['price']} \n discrpition:{data['discrpition']}\n color:{data['color']}\n manufacturer:{data['manufacturer']}\n material:{data['material']}",
            reply_markup=InlineKeyboardMarkup([
                            [InlineKeyboardButton(text="Orqaga⏮", callback_data="back"),
                            InlineKeyboardButton(text="Buyurtma🛒", callback_data=f"buyurtma_{data['id']}"), 
                            InlineKeyboardButton(text="Oldnga⏭", callback_data=f"next_{data['id']}_{id}")
                            ]])
            )

    l = db.count
    if len(l) >= 1:
        db.count = l[1:]
