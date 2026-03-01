import os
import random
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.getenv("TOKEN")

phrases = [
    "Фраза 1",
    "Фраза 2",
    "Фраза 3",
    "Фраза 4"
]

async def fact(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(random.choice(phrases))

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("fact", fact))

app.run_polling()
