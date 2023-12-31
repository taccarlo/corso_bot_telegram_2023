"""
Il programma simula un'app di creazione di pozioni magiche. 
Ogni pozione ha un nome ( la chiave), un costo e una
lista di ingredienti necessari. Gli utenti possono
visualizzare l'elenco delle pozioni disponibili, 
cercare una pozione per nome e creare una nuova pozione.

# Menu principale
while True:
    print("\n=== App Creazione Pozioni        Magiche ===")
    print("1. Mostra elenco delle pozioni")
    print("2. Cerca una pozione")
    print("3. Crea una nuova pozione")
    print("4. Esci")
"""

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from telegram.ext import filters, MessageHandler, ApplicationBuilder, CommandHandler, ContextTypes


pozioni = {
        "Pozione dell'amore":[5.9,["Taurina","Steroidi"]],
        "pozione felicità":[9.1,["montenegro","tren"]],
        "pozione forza":[10, ["panca piana", "bilancere","sudore del gym bro"]] 
        }

# IMPORTANTE: inserire il token fornito dal BotFather nella seguente stringa
with open("token.txt", "r") as f:
    TOKEN = f.read()
    print("Il tuo token è ", TOKEN)

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    lang = "linguaggio utilizzato: "+update.effective_user.language_code
    await update.message.reply_text(f'Hello {update.effective_user.first_name}! {lang}')

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

async def caps(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text_caps = ' '.join(context.args).upper()
    await context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)

async def lista(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global pozioni
    message = ""
    for x in pozioni.keys():
        message = message+x+" "
    await update.message.reply_text(f'La tua lista è {message}' )

async def cerca(update: Update, context : ContextTypes.DEFAULT_TYPE):
    risposta = "il prezzo è "+str(pozioni["Pozione dell'amore"][0])
    await update.message.reply_text(risposta)

async def crea(update: Update, context : ContextTypes.DEFAULT_TYPE):
    print("ho ricevuto: ", context.args)
    query = context.args[0]
    lista = query.split(',')
    nomepozione = lista[0]
    prezzopozione = lista[1]
    global pozioni
    pozioni[nomepozione]=[prezzopozione,["ingrediente1","ingrediente2"]]
    await update.message.reply_text("pozione aggiunta con successo")

def main():

    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("hello", hello))
    app.add_handler(CommandHandler("echo", echo))
    app.add_handler(CommandHandler('caps', caps))
    app.add_handler(CommandHandler("lista",lista))
    app.add_handler(CommandHandler("cerca",cerca))
    app.add_handler(CommandHandler("crea",crea))
    app.add_handler(echo_handler)
    app.run_polling()


if __name__=='__main__':
   main()
