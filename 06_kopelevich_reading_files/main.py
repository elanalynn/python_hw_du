# Import required Python libraries
import datetime

# Import required application modules
from Investor import Investor
from Bond import Bond
from Portfolio import Portfolio
from Report import Report
from DataReader import DataReader


def main():
    # Get stock and bond data
    dataReader = DataReader()
    stockData = dataReader.getStockData()
    bondData = dataReader.getBondData()
    # Initialize an investor named Bob Smith
    investor = Investor(
        "Bob", "Smith", "123 Colarado Blvd, Denver, CO 80221", "303.777.1234"
    )

    # Initialize a portfolio
    portfolio = Portfolio(investor)
    # Initialize each stock and add it to the portfolio
    portfolio.addStocks(stockData)
    # Add the bond to the portfolio
    portfolio.addBonds(bondData)
    # Initialize a Report
    report = Report(portfolio)
    # Print the stock and bond report
    report.print()


main()
