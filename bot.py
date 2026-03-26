import os
import logging
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# 1. ቶክን መቀበያ
TOKEN = os.getenv('BOT_TOKEN')

# 2. ሎጊንግ
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# 3. የጀምር (Start) ትዕዛዝ
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [['🆔 መታወቂያ ቀይር (PDF)', '💰 ሂሳቤን እይ'], ['💵 ብር አስገባ', '🤖 AI አነጋግር']]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text('ሰላም BOSS! እንኳን ደህና መጡ። መታወቂያ ለመቀየር PDF ፋይሉን ይላኩ።', reply_markup=reply_markup)

# 4. ሰላምታ እና አዝራሮችን ማስተናገጃ
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if text.lower() in ["ሀይ", "hi", "ሰላም"]:
        await update.message.reply_text("ሰላም BOSS! እንዴት ነህ? ዛሬ ምን እንስራ?")
    elif text == "🆔 መታወቂያ ቀይር (PDF)":
        await update.message.reply_text("እሺ BOSS! እባክህ የመታወቂያውን PDF ፋይል አሁን ላክልኝ።")
    else:
        await update.message.reply_text(f"ተቀብያለሁ BOSS! '{text}' ብለኸኛል።")

# 5. PDF ፋይል መቀበያ
async def handle_pdf(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("PDF ፋይሉ ደርሶኛል! ወደ ምስል (ID Card) ለመቀየር በሂደት ላይ ነው...")

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler('start', start))
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))
    app.add_handler(MessageHandler(filters.Document.PDF, handle_pdf))
    app.run_polling()
