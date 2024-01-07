import requests
import json
from config import currencies

# Custom exception class for currency conversion errors
class ConversionException(Exception):
    pass

# Class responsible for handling currency conversion using an external API
class CurrencyConverter:
    @staticmethod
    def get_price(base_code, target_code, amount):
        # Check if the base and target currencies are the same
        if base_code == target_code:
            raise ConversionException(f"Can't convert the same currencies {base_code}. Please try again.")
        
        # Convert human-readable currency names to their respective currency codes
        try:
            base = currencies[base_code]
        except KeyError:
            raise ConversionException(f"Can't exchange the currency {base_code}. Use currency from /values.")
        
        try:
            target = currencies[target_code]
        except KeyError:
            raise ConversionException(f"Can't exchange the currency {target_code}. Use currency from /values.")
        
        # Ensure the provided amount is a valid number
        try:
            amount = float(amount)
        except ValueError:
            raise ConversionException(f"Can't exchange the amount {amount}. Amount should be int or float type.")
        
        # Make a request to the external API for currency conversion
        response = requests.get(f"https://v6.exchangerate-api.com/v6/cdc51f437c9dab6b8968db19/pair/{base}/{target}/{amount}")

        # Parse the response and extract the conversion result
        conversion_result = json.loads(response.content)['conversion_result']
       
        return conversion_result
    