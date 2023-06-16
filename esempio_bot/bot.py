
# IMPORTO LE LIBRERIE CHE MI SERVONO PER OPERARE CON IL BOT TELEGRAM
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, filters, MessageHandler, ApplicationBuilder, ContextTypes


# Installing
# You can install or upgrade python-telegram-bot via
# pip install python-telegram-bot --upgrade

# QUI LEGGIAMO DAL FILE TOKEN.txt IL TOKEN DEL BOT
with open("token.txt", "r") as f:
    TOKEN = f.read()
    print("Il tuo token è ", TOKEN)

# QUESTA FUNZIONE PRENDE LA LINGUA DELL'UTENTE (ITALIANO, INGLESE) 
# E IL SUO NOME NELLA STRUTTURA update.effective_user
async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    lang = "linguaggio utilizzato: " +update.effective_user.language_code
    await update.message.reply_text(f'Hello {update.effective_user.first_name} {lang}')

# QUESTA FUNZIONE PRENDE OGNI COSA CHE SCRIVIAMO SUL BOT
# CHE NON SIA UN COMANDO E LO RISCRIVE A SCHERMO
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

# QUESTA FUNZIONE PRENDE L'INPUT DELL'UTENTE (context.args) E LO 
# RESTITUISCE ALL'UTENTE
async def caps(update: Update, context: ContextTypes.DEFAULT_TYPE):
    received_input = context.args
    text_caps = ' '.join(received_input).upper()
    await context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)
    
# IL MAIN CONTIENE TUTTI I COMANDI CHE L'UTENTE PUò ESEGUIRE
def main():
    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("hello", hello))
    app.add_handler(CommandHandler("echo", echo))
    app.add_handler(CommandHandler('caps', caps))
    app.add_handler(echo_handler)
    app.run_polling()


if __name__=='__main__':
   main()
