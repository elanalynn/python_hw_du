# Elana Kopelevich
# April 14, 2019
# This program uses disctionaries to generate a report about stock earnings/losses on multiple stocks.
# The main method (generateStockReport) takes a list of dictionaries as an input and outputs a formatted report.

# Initial data is a list of dictionaries
stocks = [
    {
        "symbol": "GOOGL",
        "quantity": 125,
        "purchasePrice": 772.88,
        "currentPrice": 941.53,
    },
    {"symbol": "MSFT", "quantity": 85, "purchasePrice": 56.60, "currentPrice": 73.04},
    {"symbol": "RDS-A", "quantity": 400, "purchasePrice": 49.58, "currentPrice": 55.74},
    {"symbol": "AIG", "quantity": 235, "purchasePrice": 54.21, "currentPrice": 65.27},
    {"symbol": "FB", "quantity": 150, "purchasePrice": 124.31, "currentPrice": 172.45},
]

# Although none of the data in the example returned losses, this function ensures that the formatting
# of the final currency is standard. Rather than formatting the currency as $-1.000 for negative numbers,
# this method format negative values like this: -$1,000. It also adds commas and rounds to two decimal places.
def formatUSD(amount):
    if amount >= 0:
        return "${:,.2f}".format(amount)
    else:
        return "-${:,.2f}".format(-amount)


# Calculates the earnings or loss for each stock symbol provided.
def calculateEarningsOrLoss(currentPrice, purchasePrice, quantity):
    return (currentPrice - purchasePrice) * quantity


# Generates the formatted report
def generateStockReport(customerName, stocks):
    print("\n")
    print(f"Stock ownership for {customerName}")
    print("-" * 60)
    # The length of the empty spaces are equal to 20 less the length of the previous item.
    print("STOCK" + " " * 15 + "SHARE" + " " * 15 + "EARNINGS/LOSS")
    print("-" * 60)

    for stock in stocks:
        earningsLoss = calculateEarningsOrLoss(
            stock['currentPrice'], stock['purchasePrice'], stock['quantity']
        )
        # The length of the offsets are equal to 20 less the length of the previous item.
        offset1 = 20 - len(stock['symbol'])
        offset2 = 20 - len(str(stock['quantity']))
        # Print the line item
        print(
            f"{stock['symbol']}"
            + " " * offset1
            + f"{stock['quantity']}"
            + " " * offset2
            + f"{formatUSD(earningsLoss)}"
        )


# Call the the report method.
generateStockReport("Bob Smith", stocks)
