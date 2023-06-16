from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from telegram.ext import filters, MessageHandler, ApplicationBuilder, CommandHandler, ContextTypes

# IMPORTANTE: inserire il token fornito dal BotFather nella seguente stringa
with open("token.txt", "r") as f:
    TOKEN = f.read()
    print("Il tuo token è ", TOKEN)

"""Il programma simula un'app di creazione di pozioni magiche. 
Ogni pozione ha un nome ( la chiave), un costo e una
lista di ingredienti necessari. Gli utenti possono
visualizzare l'elenco delle pozioni disponibili, 
cercare una pozione per nome e creare una nuova pozione."""
"""while True:
    print("\n=== App Creazione Pozioni        Magiche ===")
    print("1. Mostra elenco delle pozioni")
    print("2. Cerca una pozione")
    print("3. Crea una nuova pozione")
    print("4. Esci")"""
dictionary = {"pozione dell'amore" : [100,  ["Taurina" , "Sterioidi"] ], "pozione delle dimensioni" : [50, ["sindrome di down" , "viagra"]] }
   
async def lista(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global dictionary
    message = ""
    for x in dictionary.keys():
        message = message + x+" "
    await update.message.reply_text(f'La tua lista è {message}')

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    lang = "linguaggio utilizzato: " +update.effective_user.language_code
    await update.message.reply_text(f'Hello {update.effective_user.first_name} {lang}')

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

async def caps(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text_caps = ' '.join(context.args).upper()
    await context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)

async def cerca(update: Update, context: ContextTypes.DEFAULT_TYPE):
    lang = "linguaggio utilizzato: " +update.effective_user.language_code
    await update.message.reply_text(f'Hello {update.effective_user.first_name} {lang}')
    
def main():

    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("hello", hello))
    app.add_handler(CommandHandler('caps', caps))
    app.add_handler(CommandHandler('lista', lista))
    app.add_handler(CommandHandler('cerca', cerca))
    app.run_polling()


if __name__=='__main__':
   main()


