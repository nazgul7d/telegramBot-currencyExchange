# Currency Converter Telegram Bot
This Telegram bot allows users to retrieve the price of a specific amount of currency (euro, dollar, canadian dollar or tenge) converted to another currency. The bot utilizes the pytelegrambotapi library for Telegram bot functionality and makes use of Requests and JSON libraries for handling currency conversion API requests.
# How to Use
To interact with the bot, send a message in the following format: ```base_currency target_currency amount```  
For example: euro dollar 100

# Commands
- /start or /help: Get instructions on how to use the bot.
- /values: Display information about all available currencies.

# Implementation Details
- The bot is built using the Telebot library (pytelegrambotapi).
- The extensions.py file contains classes for handling currency conversion, exceptions, and API requests.
- The CurrencyConverter class in extensions.py includes a static method get_price() for obtaining the currency conversion.
- The bot handles user input errors, such as incorrect or non-existent currencies or improperly entered numbers, by raising a custom ConversionException with explanatory error messages.

# Configuration
To run the bot, you need to provide a Telegram bot token and configure the list of available currencies. Store the bot token in a separate config.py file.

# config.py
TOKEN = "your_telegram_bot_token"

currencies = {
            'dollar': 'USD',
            'canadian_dollar': 'CAD',
            'tenge': 'KZT',
            'euro': 'EUR',
}

# Dependencies
Ensure you have the necessary dependencies installed by running:
```pip install pytelegrambotapi requests```

# Getting Started
1. Install dependencies.
2. Set up your Telegram bot and obtain the token.
3. Configure the bot token and available currencies in config.py.
4. Run the script.

