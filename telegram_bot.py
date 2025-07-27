from telegram import Bot

TELEGRAM_TOKEN = "your_token_here"
CHAT_ID = "your_chat_id_here"

def send_telegram_alert(signal):
    bot = Bot(token=TELEGRAM_TOKEN)
    message = f"🚨 Signal Alert 🚨\nType: {signal['type']}\nSymbol: {signal['symbol']}\nReason: {signal['reason']}\nConfidence: {signal['confidence']}%"
    bot.send_message(chat_id=CHAT_ID, text=message)
