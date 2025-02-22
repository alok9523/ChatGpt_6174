from telegram.ext import Application, MessageHandler, filters
import openai

# Initialize OpenAI API
openai.api_key = 'ddc-0D0phWHsoLGsNgnEJ0U1HTm2W0wZF01hkI1wKBS3ih8KK7EENC'

# Function to handle messages
async def handle_message(update, context):
    user_message = update.message.text
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=user_message,
        max_tokens=150
    )
    bot_reply = response.choices[0].text.strip()
    await update.message.reply_text(bot_reply)

# Set up the bot
application = Application.builder().token('6044696246:AAFbr9ewoPfuGf6RCFYq66HlVaYBH5x_tkM').build()

# Add handler
application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

# Start the bot
application.run_polling()
