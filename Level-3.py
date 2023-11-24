from datetime import date
import re

# Task 10: Number of Days Between Two Dates
def days_between(date1, date2):
    return abs((date2 - date1).days)

# Task 11: Temperature Converter
class TempConverter:
    def __init__(self):
        print("Use convert_to_fahrenheit() for Celsius to Fahrenheit conversion.")
        print("Use convert_to_celsius() for Fahrenheit to Celsius conversion.")

    @staticmethod
    def convert_to_fahrenheit(celsius):
        return celsius * 9 / 5 + 32, 'F'
    
    @staticmethod
    def convert_to_celsius(fahrenheit):
        return (fahrenheit - 32) * 5 / 9, 'C'

# Task 12: Email Validator and Splitter
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

def validate_email(email):
    if re.fullmatch(email_pattern, email):
        return email
    else:
        raise ValueError("Invalid Email")
            
def split_email(email):
    username, domain = validate_email(email).split('@')
    return f"username: {username}, domain: {domain}"

# Task 13: Currency Converter
class CurrencyConv:
    def __init__(self):
        print("Use DollarToEgyptPound() for USD to EGP conversion.")
        print("Use EgyptPoundToDollar() for EGP to USD conversion.")
        print("Use AutoDetect() to convert between USD and EGP.")

    @staticmethod
    def raise_error():
        raise Exception("Error: Conversion not supported.")

    @staticmethod
    def dollar_to_egypt_pound(amount):
        return f"{amount * 30.9} LE"
    
    @staticmethod
    def egypt_pound_to_dollar(amount):
        return f"{amount / 30.9} $"
    
    def auto_detect(self, amount, from_currency, to_currency):
        if from_currency == '$' and to_currency == 'LE':
            return self.dollar_to_egypt_pound(amount)
        elif from_currency == 'LE' and to_currency == '$':
            return self.egypt_pound_to_dollar(amount)
        else:
            self.raise_error()

# Example usage
if __name__ == "__main__":
    # Task 10 Example
    start_date = date(2018, 12, 13)
    end_date = date(2015, 2, 25)
    print(days_between(start_date, end_date), "days")

    # Task 11 Example
    converter = TempConverter()
    print(converter.convert_to_fahrenheit(50))
    print(converter.convert_to_celsius(50))

    # Task 12 Example
    print(split_email('test123456789@test.com'))

    # Task 13 Example
    currency_converter = CurrencyConv()
    print(currency_converter.dollar_to_egypt_pound(1000))
    print(currency_converter.egypt_pound_to_dollar(30900))
    print(currency_converter.auto_detect(1000, '$', 'LE'))
    print(currency_converter.auto_detect(30900, 'LE', '$'))
    try:
        print(currency_converter.auto_detect(5000, '$', '$'))
    except Exception as e:
        print(e)
