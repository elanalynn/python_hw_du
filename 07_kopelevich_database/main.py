# Import required Python libraries
import datetime
import os

# Import required application modules
from Investor import Investor
from Bond import Bond
from Portfolio import Portfolio
from Report import Report
from DataReader import DataReader


def main():
    # Delete portfolio.db if it exists
    os.remove("portfolio.db")
    print("portfolio.db removed successfully")

    # Get data paths
    stock_filename = "data_stocks.csv"
    bond_filename = "data_bonds.csv"

    # Initialize dataReader
    dataReader = DataReader(stock_filename, bond_filename)

    # Get stock and bond data
    stockData = dataReader.getStockData()
    bondData = dataReader.getBondData()

    # Initialize an investor
    investor = Investor("Bob", "Smith", "123 Fake St, Denver, CO 80221", "303.777.1234")

    # Initialize a portfolio
    portfolio = Portfolio(investor)

    # Add the stocks and bonds to the portfolio
    portfolio.addStocks(stockData)
    portfolio.addBonds(bondData)

    # Initialize a report
    report = Report(portfolio)

    # Print the report
    report.print()


main()
