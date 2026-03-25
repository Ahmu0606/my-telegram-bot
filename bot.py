import os
import logging
import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# 1. ቶክን መቀበያ
TOKEN = os.getenv('BOT_TOKEN')

# 2. ሎጊንግ
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# 3. የ /start ትዕዛዝ
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_name = update.effective_user.first_name
    await context.bot.send_message(
        chat_id=update.effective_chat.id, 
        text=f"ሰላም {user_name}! እንኳን ወደ አህመድ ቦት በሰላም መጣህ።"
    )

# 4. ዋናው የማስነሻ ክፍል
async def main():
    if not TOKEN:
        print("ስህተት: BOT_TOKEN አልተገኘም!")
        return

    # እዚህ ጋር 'application' በትክክል ተለይቷል
    application = ApplicationBuilder().token(TOKEN).build()
    application.add_handler(CommandHandler('start', start))

    await application.initialize()
    await application.updater.start_polling()
    
    print("ቦቱ ስራ ጀምሯል...")
    while True:
        await asyncio.sleep(1)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        pass
