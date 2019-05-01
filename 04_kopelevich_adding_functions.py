# Elana Kopelevich
# April 25, 2019
# The assignment calls for refactoring the previous assignment to use functions. Since I already use
# functions, not much is changing here in terms of structure. I have added the yearlyEarningsLoss function
# and included the output in the results table. The data has also been modified to include a purchase date.

# import the datetime module
import datetime

# Initial data is a list of dictionaries
stocks = [
    {
        "symbol": "GOOGL",
        "quantity": 125,
        "purchasePrice": 772.88,
        "currentPrice": 941.53,
        "purchaseDate": datetime.date(2015, 8, 1),
    },
    {
        "symbol": "MSFT",
        "quantity": 85,
        "purchasePrice": 56.60,
        "currentPrice": 73.04,
        "purchaseDate": datetime.date(2015, 8, 1),
    },
    {
        "symbol": "RDS-A",
        "quantity": 400,
        "purchasePrice": 49.58,
        "currentPrice": 55.74,
        "purchaseDate": datetime.date(2015, 8, 1),
    },
    {
        "symbol": "AIG",
        "quantity": 235,
        "purchasePrice": 54.21,
        "currentPrice": 65.27,
        "purchaseDate": datetime.date(2015, 8, 1),
    },
    {
        "symbol": "FB",
        "quantity": 150,
        "purchasePrice": 124.31,
        "currentPrice": 172.45,
        "purchaseDate": datetime.date(2015, 8, 1),
    },
    {
        "symbol": "M",
        "quantity": 425,
        "purchasePrice": 30.30,
        "currentPrice": 23.98,
        "purchaseDate": datetime.date(2017, 1, 10),
    },
    {
        "symbol": "F",
        "quantity": 85,
        "purchasePrice": 12.58,
        "currentPrice": 10.95,
        "purchaseDate": datetime.date(2017, 2, 17),
    },
    {
        "symbol": "IBM",
        "quantity": 80,
        "purchasePrice": 150.37,
        "currentPrice": 145.30,
        "purchaseDate": datetime.date(2017, 5, 12),
    },
]

# This function ensures that the formatting of the final currency is standard. Rather than formatting the
# currency as $-1.000 for negative numbers, this method format negative values like this: -$1,000. It also adds
# commas and rounds to two decimal places.
def formatUSD(amount):
    if amount >= 0:
        return "${:,.2f}".format(amount)
    else:
        return "-${:,.2f}".format(-amount)


# Calculates the earnings or loss for each stock symbol provided.
def calculateEarningsOrLoss(currentPrice, purchasePrice, quantity):
    return (currentPrice - purchasePrice) * quantity


# Calculates the percentage earned or loss for each year
def calculateYearlyEarningsOrLoss(
    currentValue, purchaseValue, currentDate, purchaseDate
):
    priceDiff = currentValue - purchaseValue
    dayDiff = (currentDate - purchaseDate).days
    yearDiff = dayDiff / 365

    return (((priceDiff / purchaseValue)) / yearDiff) * 100


# Generates the formatted report
def generateStockReport(customerName, stocks):
    print("\n")
    print(f"Stock ownership for {customerName}")
    print("-" * 100)
    # The length of the empty spaces are equal to 20 less the length of the previous item.
    print(
        "STOCK"
        + " " * 15
        + "SHARE"
        + " " * 15
        + "EARNINGS/LOSS"
        + " " * 15
        + "YEARLY EARNING/LOSS"
    )
    print("-" * 100)

    for stock in stocks:
        earningsLoss = calculateEarningsOrLoss(
            stock["currentPrice"], stock["purchasePrice"], stock["quantity"]
        )

        yearlyEarningsLoss = calculateYearlyEarningsOrLoss(
            stock["currentPrice"],
            stock["purchasePrice"],
            datetime.date.today(),
            stock["purchaseDate"],
        )
        # The length of the offsets are equal to 20 less the length of the previous item.
        offset1 = 20 - len(stock["symbol"])
        offset2 = 20 - len(str(stock["quantity"]))
        offset3 = 28 - len(str(formatUSD(earningsLoss)))
        # Print the line item
        print(
            f"{stock['symbol']}"
            + " " * offset1
            + f"{stock['quantity']}"
            + " " * offset2
            + f"{formatUSD(earningsLoss)}"
            + " " * offset3
            + f"{round(yearlyEarningsLoss, 2)}%"
        )


# Call the the report method.
generateStockReport("Bob Smith", stocks)
