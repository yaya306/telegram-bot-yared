import os
import logging
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

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
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    await update.message.reply_text(
        f"👋 Hi {user.first_name}!\n\n"
        f"I'm your 24/7 Telegram Bot!\n"
        f"Type /help to see available commands."
    )

# Command: /help
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    help_text = """
📋 Available Commands:

/start - Start conversation
/help - Show this help
/echo [text] - Repeat your text

💡 Just send me any message!
I'll reply to anything you say.
    """
    await update.message.reply_text(help_text)

# Command: /echo
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if context.args:
        text = ' '.join(context.args)
        await update.message.reply_text(f"🔊 Echo: {text}")
    else:
        await update.message.reply_text("Please add text: /echo Hello World!")

# Handle regular messages
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_msg = update.message.text
    reply = f"📝 You said: {user_msg}\n\nNice to chat with you! 😊"
    await update.message.reply_text(reply)

def main():
    """Start the bot"""
    # Check token
    if not BOT_TOKEN:
        logger.error("❌ Bot token not found in .env file!")
        return
    
    # Create application
    application = Application.builder().token(BOT_TOKEN).build()
    
    # Add handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("echo", echo))
    
    # Handle text messages
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    # Start bot
    logger.info("🤖 Bot is starting...")
    print("\n" + "="*50)
    print("✅ BOT IS RUNNING!")
    print("="*50)
    print("Go to Telegram and chat with your bot")
    print("Commands: /start, /help, /echo")
    print("Press Ctrl+C to stop\n")
    
    application.run_polling()

if __name__ == '__main__':
    main()