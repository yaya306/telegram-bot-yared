import os
import logging
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Load environment variables
load_dotenv()

# Get bot token
BOT_TOKEN = os.getenv('BOT_TOKEN')

# Setup logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Command: /start
def start(update: Update, context: CallbackContext) -> None:
    user = update.effective_user
    update.message.reply_text(
        f"👋 Hi {user.first_name}!\n\n"
        f"I'm your 24/7 Telegram Bot!\n"
        f"Type /help to see available commands."
    )

# Command: /help
def help_command(update: Update, context: CallbackContext) -> None:
    help_text = """
📋 Available Commands:

/start - Start conversation
/help - Show this help
/echo [text] - Repeat your text

💡 Just send me any message!
I'll reply to anything you say.
    """
    update.message.reply_text(help_text)

# Command: /echo
def echo(update: Update, context: CallbackContext) -> None:
    if context.args:
        text = ' '.join(context.args)
        update.message.reply_text(f"🔊 Echo: {text}")
    else:
        update.message.reply_text("Please add text: /echo Hello World!")

# Handle regular messages
def handle_message(update: Update, context: CallbackContext) -> None:
    user_msg = update.message.text
    reply = f"📝 You said: {user_msg}\n\nNice to chat with you! 😊"
    update.message.reply_text(reply)

def main():
    """Start the bot"""
    # Check token
    if not BOT_TOKEN:
        logger.error("❌ Bot token not found in .env file!")
        return
    
    # Create updater
    updater = Updater(BOT_TOKEN, use_context=True)
    
    # Get dispatcher
    dispatcher = updater.dispatcher
    
    # Add handlers
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(CommandHandler("echo", echo))
    
    # Handle text messages
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))
    
    # Start bot
    logger.info("🤖 Bot is starting...")
    print("\n" + "="*50)
    print("✅ BOT IS RUNNING!")
    print("="*50)
    print("Go to Telegram and chat with your bot")
    print("Commands: /start, /help, /echo")
    print("Press Ctrl+C to stop\n")
    
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()