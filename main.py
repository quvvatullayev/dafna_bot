from telegram.ext import (
    CallbackQueryHandler,
    CommandHandler,
    MessageHandler,
    Filters,
    Updater,
)

from home import (
    start,
)
from handler import(
    katalog,
    prodouct_type,
    prodouct,
    next_prodouct
)
TOKEN = "5567524975:AAHzn2G8Ws6IgE_XRjuW3LTGv2eUtsiXL8E"
updater = Updater(token=TOKEN, use_context=True)

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(MessageHandler(Filters.text("🛍Katalog"), katalog))
updater.dispatcher.add_handler(CallbackQueryHandler(prodouct_type, pattern="katalog_"))
updater.dispatcher.add_handler(CallbackQueryHandler(prodouct, pattern='product_type_'))
updater.dispatcher.add_handler(CallbackQueryHandler(next_prodouct, pattern='next_'))
updater.start_polling()
updater.idle()