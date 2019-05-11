class Report:
    def __init__(self, portfolio):
        self.portfolio = portfolio

    # Generates the formatted report with stock section and bond section
    def print(self):
        investor = self.portfolio.getInvestor()

        f = open("report.txt", "w")
        f.write(
            "\n"
            f"Portfolio Report for {investor.getFirstName()} {investor.getLastName()}\n"
            f"{investor.getPhoneNumber()}\n"
            f"{investor.getAddress()}\n"
        )

        f.write("\n Stocks \n")
        f.write("-" * 90 + "\n")
        f.write(
            "SYMBOL"
            + " " * 15
            + "SHARE"
            + " " * 15
            + "EARNINGS/LOSS"
            + " " * 15
            + "YEARLY EARNING/LOSS \n"
        )
        f.write("-" * 90 + "\n")

        for stock in self.portfolio.getStocks():
            # The length of the offsets are equal to 20 less the length of the previous stock.
            offset1 = 20 - len(stock.getSymbol())
            offset2 = 20 - len(str(stock.getQuantity()))
            offset3 = 28 - len(str(self.__formatUSD__(stock.calculateEarningsOrLoss())))
            # Print the line item
            f.write(
                f"{stock.getSymbol()}"
                + " " * offset1
                + f"{stock.getQuantity()}"
                + " " * offset2
                + f"{self.__formatUSD__(stock.calculateEarningsOrLoss())}"
                + " " * offset3
                + f"{round(stock.calculateYearlyEarningsOrLoss(), 2)}% \n"
            )

        f.write("\n\n\n")
        f.write("Bonds\n")
        f.write("-" * 110 + "\n")
        # The length of the empty spaces are equal to 20 less the length of the previous item.
        f.write(
            "STOCK"
            + " " * 10
            + "SHARE"
            + " " * 10
            + "EARNINGS/LOSS"
            + " " * 10
            + "YEARLY EARNING/LOSS"
            + " " * 10
            + "COUPON"
            + " " * 10
            + "YIELD\n"
        )
        f.write("-" * 110 + "\n")

        for bond in self.portfolio.getBonds():
            # The length of the offsets are equal to 20 less the length of the previous stock.
            offset1 = 15 - len(bond.getSymbol())
            offset2 = 15 - len(str(bond.getQuantity()))
            offset3 = 23 - len(str(self.__formatUSD__(bond.calculateEarningsOrLoss())))
            offset4 = 44 - len(str(bond.calculateYearlyEarningsOrLoss()))
            offset5 = 16 - len(str(bond.getCoupon()))
            # Print the line item
            f.write(
                f"{bond.getSymbol()}"
                + " " * offset1
                + f"{bond.getQuantity()}"
                + " " * offset2
                + f"{self.__formatUSD__(bond.calculateEarningsOrLoss())}"
                + " " * offset3
                + f"{round(bond.calculateYearlyEarningsOrLoss(), 2)}%"
                + " " * offset4
                + f"{bond.getCoupon()}"
                + " " * offset5
                + f"{bond.getyieldAmount()}% \n"
            )
        f.close()

    # This function ensures that the formatting of the final currency is standard. Rather than formatting the
    # currency as $-1.000 for negative numbers, this method format negative values like this: -$1,000.
    # It also adds commas and rounds to two decimal places.
    def __formatUSD__(self, amount):
        if amount >= 0:
            return "${:,.2f}".format(amount)
        else:
            return "-${:,.2f}".format(-amount)

