# Elana Kopelevich
# April 6, 2019
# This program uses existing lists to generate a report about stock earnings/losses on multiple stocks.
# As input, it takes various lists, and for output, it prints a formatted report.

# Initial data as sorted lists - this is a pretty fragile approach.
# I imagine we'll be using dictionaries in a future version of this!
stockSymbols = ["GOOGL", "MSFT", "RDS-A", "AIG", "FB"]
quantities = [125, 85, 400, 235, 150]
purchasePrices = [772.88, 56.60, 49.58, 54.21, 124.31]
currentPrices = [941.53, 73.04, 55.74, 65.27, 172.45]

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
def generateStockReport(customerName, symbols, quans, purchasePrices, currentPrices):
    # Set initial index to 0 so that it can be incremented to move through the entire list.
    index = 0

    print("\n")
    print(f"Stock ownership for {customerName}")
    print("-" * 60)
    # The length of the empty spaces are equal to 20 less the length of the previous item.
    print("STOCK" + " " * 15 + "SHARE" + " " * 15 + "EARNINGS/LOSS")
    print("-" * 60)

    for stock in symbols:
        earningsLoss = calculateEarningsOrLoss(
            currentPrices[index], purchasePrices[index], quans[index]
        )
        # The length of the offsets are equal to 20 less the length of the previous item.
        offset1 = 20 - len(stock)
        offset2 = 20 - len(str(quans[index]))
        # Print the line item
        print(
            f"{stock}"
            + " " * offset1
            + f"{quans[index]}"
            + " " * offset2
            + f"{formatUSD(earningsLoss)}"
        )
        # Increase the index value by one for the next loop
        index = index + 1


# Call the the report method.
generateStockReport(
    "Bob Smith", stockSymbols, quantities, purchasePrices, currentPrices
)
