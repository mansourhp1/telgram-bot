from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("سلام! من آنلاینم :)")

if _name_ == '__main__':
    main()
    app = ApplicationBuilder().token("8336683539:AAEKR-IcSArq_9trWRSq7uTQAnoka_M696k").build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()
