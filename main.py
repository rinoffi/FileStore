from bot import Bot
import pyrogram.utils

pyrogram.utils.MIN_CHANNEL_ID = -1009147483647

if name == "main":
    Bot().run()
    application.run_polling()
    
    # or for Pyrogram
    # app.run()
