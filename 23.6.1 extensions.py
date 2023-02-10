import json
import requests
from config import CURRENCY_API, val


class APIException(Exception):
    pass

class SameCurrencyException(APIException):
    def __str__(self):
        return 'Вы ввели одинаковые валюты, попробуйте заново.'

class WrongMessageException(APIException):
    def __str__(self):
        return 'Команда не соответствует заданной форме, попробуйте заново.'

class WrongCurrencyException(APIException):
    def __str__(self):
        return 'Вы ввели неккоректную валюту, попробуйте заново.'

class WrongNumberException(APIException):
    def __str__(self):
        return 'Вы ввели неверное число, попробуйте заново.'

class ExceptionAnalyzer():
    @staticmethod
    def exception_check(base, quote, amount):
        try:
            amount = float(amount)
        except ValueError:
            raise WrongNumberException
            
        try:
            RequestAPI.get_price(val[base], val[quote], amount)
        except KeyError:
            raise WrongCurrencyException

        if base == quote:
            raise SameCurrencyException
    

class RequestAPI:
    @staticmethod
    def get_price(base, quote, amount):
        r = requests.get(f'http://api.exchangeratesapi.io/v1/latest?access_key={CURRENCY_API}&symbols=USD,EUR,RUB').content
        values = json.loads(r)['rates']
        return round(float(amount)/values[base] * values[quote], 2)
