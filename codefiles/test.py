import commentjson
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Чтение конфигурации
with open('config.jsonc', 'r') as config_file:
    config = commentjson.load(config_file)

TOKEN = config['telegram']['token']
DB_NAME = config['database']['name']

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Привет! Я бот для отслеживания прогресса тренировок.')

def main() -> None:
    application = ApplicationBuilder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))

    application.run_polling()

if __name__ == '__main__':
    main()
