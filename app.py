import telebot
from config import currencies, TOKEN
from extensions import ConversionException, CurrencyConverter

# Create a Telegram bot instance
bot = telebot.TeleBot(TOKEN)


# Handler for the /start and /help commands
@bot.message_handler(commands=['start', 'help'])
def help(message:telebot.types.Message):
    # Provide instructions on how to use the bot
    text = 'To start, enter the command in the following format: \n<what currency you want to convert> \
<what currency you want to convert into>  \
<how much do you want to convert>\nShow all available currencies: /values'
    bot.reply_to(message, text)

# Handler for the /values command
@bot.message_handler(commands=['values'])
def values(message:telebot.types.Message):
    # Display all available currencies
    text = 'Available currencies'
    for currency in currencies.keys():
        text = '\n'.join((text, currency))
    bot.reply_to(message, text)

# Handler for text messages (actual currency conversion)
@bot.message_handler(content_types=['text', ])
def convert(message:telebot.types.Message):
    try:
        # Split the user's input into components
        value = message.text.split(' ')

        if len(value) > 3:
            raise ConversionException('Too many parameters.')
        
        if len(value) < 3:
            raise ConversionException('Not enough parameters are given.')
        
        # Extract base_code, target_code, and amount from user input
        base_code, target_code, amount = value
        conversion_result = CurrencyConverter.get_price(base_code, target_code, amount)

    # Handle conversion-related exceptions and provide user-friendly error messages
    except ConversionException as e:
        bot.reply_to(message, f"Error in request. \n{e}")
    except Exception as e:
         # Handle other unexpected exceptions
         bot.reply_to(message, f"Can't process the request.\n{e}")
    else:
        # Display the conversion result based on the amount provided
        amount = float(value[2])
        if amount == 1:
            text = f"price of {amount} {base_code} in {target_code} is {conversion_result}"
        if amount > 1:
            text = f"price of {amount} {base_code}s in {target_code} is {conversion_result}"
        bot.send_message(message.chat.id, text)
        
# Start the bot and keep it running
bot.polling()