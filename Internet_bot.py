from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

# Replace 'YOUR_BOT_TOKEN_HERE' with the token you got from BotFather
TOKEN = 'YOUR_BOT_TOKEN_HERE'

# Start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello! I can check your internet connections.')

# Command to check Wi-Fi connections
async def check_wifi(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # This command lists devices connected to your local Wi-Fi
    response = os.popen('arp -a').read()
    await update.message.reply_text(f"Connected Devices:\n{response}")

# Create the bot application
app = ApplicationBuilder().token(TOKEN).build()

# Add handlers for commands
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("wifi", check_wifi))

print("Bot is running...")

# Start polling for updates
app.run_polling()
