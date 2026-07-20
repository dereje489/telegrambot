from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN = "8603365705:AAFwH7y4a_2ACUfw36ZoOQl9R_Te41xp59M"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Nagaan dhuftan!\n\nMaqaa, bilbila, code digit 10 ykn kebele naaf ergi."
    )

async def search(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    await update.message.reply_text(f"Barbaacha: {text}")

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, search))

print("Bot started...")
app.run_polling()