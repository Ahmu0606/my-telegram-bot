import os
import logging
import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

# ለደህንነት ሲባል ቶከኑን ከሰርቨሩ እናነባለን
TOKEN = os.getenv('BOT_TOKEN')

# ሎጊንግ (ስህተቶችን ለማየት)
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# የ /start ትዕዛዝ ሲሰጥ የሚመልሰው
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_name = update.effective_user.first_name
    await context.bot.send_message(
        chat_id=update.effective_chat.id, 
        text=f"ሰላም {user_name}! እንኳን ወደ አህመድ ታዋቂ ቦት በሰላም መጣህ። ይህ ቦት በሰርቨር ላይ 24/7 እየሰራ ነው። 🚀"
    )

# የ /help ትዕዛዝ ሲሰጥ የሚመልሰው
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id, 
        text="እርዳታ ከፈለጉ ዋናውን ባለቤት አህመድን @Ahmu060 ብለው ያግኙት።"
    )


if __name__ == '__main__':
    # ቦቱን ማዘጋጀት
    application = ApplicationBuilder().token(TOKEN).build()
    
    # ትዕዛዞችን መመዝገብ
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('help', help_command))

    async def main():
        # ቦቱን ለማስነሳት
        await application.initialize()
        await application.updater.start_polling()
        # ቦቱ እንዳይጠፋ
        while True:
            await asyncio.sleep(1)

    # ቦቱን ማስጀመር
    import asyncio
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        pass
