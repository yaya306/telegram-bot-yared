import os
from dotenv import load_dotenv
from telegram.ext import Application, CommandHandler, MessageHandler, filters

# Load token
load_dotenv()
TOKEN = os.getenv('BOT_TOKEN')

if not TOKEN:
    print("❌ ERROR: No token in .env file!")
    exit()

# Commands
async def start(update, context):
    await update.message.reply_text("🎉 Hello! I'm yared ")

async def help(update, context):
    await update.message.reply_text("Commands:\n/start - Start\n/help - Help\nSend any message to chat!")

async def echo(update, context):
    if context.args:
        text = ' '.join(context.args)
        await update.message.reply_text(f"📢 {text}")
    else:
        await update.message.reply_text("Type: /echo Hello")

async def chat(update, context):
    user_text = update.message.text
    await update.message.reply_text(f"You said: {user_text}")

def main():
    print("=" * 50)
    print("🤖 TELEGRAM BOT STARTING")
    print("=" * 50)
    
    app = Application.builder().token(TOKEN).build()
    
    # Add commands
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help))
    app.add_handler(CommandHandler("echo", echo))
    
    # Handle normal messages
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, chat))
    
    print("✅ Bot is running!")
    print("📱 Go to Telegram and test your bot")
    print("🔴 Press Ctrl+C to stop")
    print("=" * 50)
    
    app.run_polling()

if __name__ == '__main__':
    main()