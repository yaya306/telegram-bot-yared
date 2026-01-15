import os
import logging
from dotenv import load_dotenv
from telegram.ext import Application, CommandHandler, MessageHandler, filters

# Load token
load_dotenv()
TOKEN = os.getenv('BOT_TOKEN')

# Setup logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Commands
async def start(update, context):
    await update.message.reply_text("✅ Bot is working! Hello from Render!")

async def help(update, context):
    await update.message.reply_text("Commands: /start, /help")

async def echo(update, context):
    if context.args:
        text = ' '.join(context.args)
        await update.message.reply_text(f"Echo: {text}")
    else:
        await update.message.reply_text("Usage: /echo your text")

async def handle_message(update, context):
    await update.message.reply_text(f"You said: {update.message.text}")

def main():
    print("🤖 Starting Telegram Bot on Render...")
    
    if not TOKEN:
        print("❌ ERROR: No BOT_TOKEN found!")
        return
    
    app = Application.builder().token(TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help))
    app.add_handler(CommandHandler("echo", echo))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    print("✅ Bot started successfully!")
    print("📱 Test on Telegram with /start")
    
    app.run_polling()

if __name__ == '__main__':
    main()