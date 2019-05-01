# Import required Python libraries
import datetime

# Import required application modules
from Investor import Investor
from Bond import Bond
from Portfolio import Portfolio
from Report import Report
from stockData import stockData


def main():
    # Initialize an investor named Bob Smith
    investor = Investor(
        "Bob", "Smith", "123 Colarado Blvd, Denver, CO 80221", "303.777.1234"
    )
    # Initialize a purchase date
    purchaseDate = datetime.date(2017, 8, 1)
    # Initialize a bond
    bond = Bond("GT2:GOV", 100.02, 100.05, 200, 1.38, 1.35, purchaseDate)
    # Initialize a portfolio
    portfolio = Portfolio(investor)
    # Initialize each stock and add it to the portfolio
    portfolio.addStocks(stockData)
    # Add the bond to the portfolio
    portfolio.addBond(bond)
    # Initialize a Report
    report = Report(portfolio)
    # Print the stock and bond report
    report.print()


main()
