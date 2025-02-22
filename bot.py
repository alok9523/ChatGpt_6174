from telegram.ext import Updater, MessageHandler, Filters
import openai

# Initialize OpenAI API
openai.api_key = 'ddc-0D0phWHsoLGsNgnEJ0U1HTm2W0wZF01hkI1wKBS3ih8KK7EENC'

# Function to handle messages
def handle_message(update, context):
    user_message = update.message.text
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=user_message,
        max_tokens=150
    )
    bot_reply = response.choices[0].text.strip()
    update.message.reply_text(bot_reply)

# Set up the bot
updater = Updater('6044696246:AAFbr9ewoPfuGf6RCFYq66HlVaYBH5x_tkM', use_context=True)
dp = updater.dispatcher
dp.add_handler(MessageHandler(Filters.text, handle_message))

# Start the bot
updater.start_polling()
updater.idle()
