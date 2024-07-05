from currency_converter import CurrencyConverter

c=CurrencyConverter()

amount = input('Enter he amount:')
from_currency = input('From Currency').upper()
To_currency = input('To Currency').upper()


result = c.convert(amount,from_currency,to_currency)
print(result)
