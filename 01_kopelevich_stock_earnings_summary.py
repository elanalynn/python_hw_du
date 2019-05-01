# Elana Kopelevich
# April 1, 2019
# This program prompts the user to enter information about a particular stock,
# and calcualtes the earnings or loss incurred. It provides a detailed summary.

import re

# Simple validation functions

# Name validation checks that the value contains only letters.
def validateName(name):
    if not any(c.isalpha() for c in name):
        print("Your input may not contain numbers or special characters.")
        return requestName()
    else:
        return name

# Number validation checks that the value contains only digits.
def validateNumbers(input, func, arg):
    if re.findall(r"\D\.", input):
        print("Your input must be a number.")
        return func(arg)
    else:
        return float(input)


# "request<attribute>" functions that follow are all called by getInformation

# Prompts user for name, validates input, and converts to title case
def requestName():
    return validateName(input("What is your name? ")).title()


# Prompts user for stock symbol, validates, and converts to uppercase
def requestSymbol(name):
    return validateName(
        input(
            f"Hi {name}. What is the stock symbol you would like to calculate earnings/losses on? "
        ).upper()
    )


# Prompts user for quantity of shares, validates, and uses symbol value in prompt
def requestQuantity(symbol):
    quan = input(f"How many shares of {symbol} do you own? ")
    return validateNumbers(quan, requestQuantity, symbol)


# Prompts user for purchase price per share, validates, and uses symbol value in prompt
def requestPurchasePrice(symbol):
    price = input(f"What was the purchase price of {symbol}? ")
    return validateNumbers(price, requestPurchasePrice, symbol)


# Prompts user for current price per share, validates, and uses symbol value in prompt
def requestCurrentPrice(symbol):
    price = input(f"What was the current price of {symbol}? ")
    return validateNumbers(price, requestCurrentPrice, symbol)


# Calculates earnings or loss on stock and prints summary
def calculateAndPrintResults(name, symbol, quan, pp, cp):
    earningsOrLoss = quan * (cp - pp)

    message = (
        f"Stock ownership for {name}\n"
        f"----------------------------------------------------\n"
        f"{symbol}: {quan} shares\n"
        f"Purchase Price:  ${pp}\n"
        f"Current Price per Share: ${cp}\n"
        f"Earnings/Loss to-date: ${earningsOrLoss}\n"
    )

    print("\n\n\n")
    print(message)


# Calls all requests for information and calls method to calculate and print results
def getInformation():
    name = requestName()
    symbol = requestSymbol(name)
    quantity = requestQuantity(symbol)
    purchasePrice = requestPurchasePrice(symbol)
    currentPrice = requestCurrentPrice(symbol)

    calculateAndPrintResults(name, symbol, quantity, purchasePrice, currentPrice)


getInformation()
