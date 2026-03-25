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
    if not TOKEN:
        print("ስህተት፡ BOT_TOKEN አልተገኘም!")
    else:
        application = ApplicationBuilder().token(TOKEN).build()
        
        # ትዕዛዞችን መመዝገብ
        application.add_handler(CommandHandler('start', start))
        application.add_handler(CommandHandler('help', help_command))
        
        print("ቦቱ ስራ ጀምሯል...")
        import asyncio

async def main():
    await updater.initialize()
    await updater.start_polling()
    while True:
        await asyncio.sleep(1)

if __name__ == '__main__':
    asyncio.run(main())

