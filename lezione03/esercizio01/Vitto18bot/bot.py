from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# IMPORTANTE: inserire il token fornito dal BotFather nella seguente stringa
with open("token.txt", "r") as f:
    TOKEN = f.read()
    print("Il tuo token è ", TOKEN)

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

async def nuova():
    await pdate.message.reply_text('E\' il migliore')


def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("hello", hello))
    app.add_handler(CommandHandler("maignan", maignan))
    app.run_polling()


if __name__=='__main__':
   main()
