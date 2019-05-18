from Id import Id
from Stock import Stock
from Bond import Bond
import sqlite3
import random


# Create a Portfolio class
class Portfolio:
    def __init__(self, investor, stocks=[], bonds=[]):
        self.investor = investor
        self.portfolioId = Id().id
        self.createStockTable()
        self.createBondTable()

    def getInvestor(self):
        return self.investor

    def getStocks(self):
        stocks = []

        conn = sqlite3.connect("portfolio.db")
        print("Opened database successfully")

        cursor = conn.execute("SELECT *  FROM stocks")

        for row in cursor:
            stockAsList = list(row)
            stockAsList.pop(0)
            stock = Stock(*stockAsList)
            stocks.append(stock)

        print("Read database successfully")
        conn.close()

        return stocks

    def getBonds(self):
        bonds = []

        conn = sqlite3.connect("portfolio.db")
        print("Opened database successfully")

        cursor = conn.execute("SELECT *  FROM bonds")

        for row in cursor:
            bondAsList = list(row)
            bondAsList.pop(0)
            bond = Bond(*bondAsList)
            bonds.append(bond)

        print("Read database successfully")
        conn.close()

        return bonds

    def getPortfolioId(self):
        return self.portfolioId

    def createStockTable(self):
        conn = sqlite3.connect("portfolio.db")
        print("Opened database successfully")

        conn.execute(
            """CREATE TABLE stocks(
            id              INT         PRIMARY KEY     NOT NULL,
            symbol          TEXT                        NOT NULL,
            no_shares       INT                         NOT NULL,
            purchase_price  REAL                        NOT NULL,
            current_price   REAL                        NOT NULL,
            purchase_date   TEXT                        NOT NULL
        );"""
        )

        print("Table created successfully")

        conn.close()

    def createBondTable(self):
        conn = sqlite3.connect("portfolio.db")
        print("Opened database successfully")

        conn.execute(
            """CREATE TABLE bonds(
            id              INT         PRIMARY KEY     NOT NULL,
            symbol          TEXT                        NOT NULL,
            no_shares       INT                         NOT NULL,
            purchase_price  REAL                        NOT NULL,
            current_price   REAL                        NOT NULL,
            purchase_date   TEXT                        NOT NULL,
            coupon          REAL                        NOT NULL,
            yieldAmount     REAL                        NOT NULL
        );"""
        )

        print("Table created successfully")

        conn.close()

    # Create stocks from raw data
    def addStocks(self, stockData):
        for stock in stockData:
            stockObject = Stock(
                stock["symbol"],
                stock["purchasePrice"],
                stock["currentPrice"],
                stock["quantity"],
                stock["purchaseDate"],
            )

            self.__saveStock__(stockObject)
    
    # Create bonds from raw data
    def addBonds(self, bondData):
        for bond in bondData:
            bondObject = Bond(
                bond["symbol"],
                bond["purchasePrice"],
                bond["currentPrice"],
                bond["quantity"],
                bond["purchaseDate"],
                bond["coupon"],
                bond["yield"],
            )

            self.__saveBond__(bondObject)

    # Save a stock to the database
    def __saveStock__(self, stock):

        conn = sqlite3.connect("portfolio.db")
        print("Opened database successfully")

        conn.execute("INSERT INTO stocks (id, symbol, purchase_price, current_price, no_shares, purchase_date) \
            VALUES (?, ?, ?, ?, ?, ?)", (
                stock.getPurchaseId(),
                stock.getSymbol(),
                stock.getPurchasePrice(),
                stock.getCurrentPrice(),
                stock.getQuantity(),
                stock.getPurchaseDate())
            )

        conn.commit()
        print("Records created successfully")

        conn.close()

    # Save a bond to the database
    def __saveBond__(self, bond):
        conn = sqlite3.connect("portfolio.db")
        print("Opened database successfully")

        conn.execute(
            "INSERT INTO bonds (id, symbol, purchase_price, current_price, no_shares, purchase_date, coupon, yieldAmount) \
              VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
            (
                bond.getPurchaseId(),
                bond.getSymbol(),
                bond.getPurchasePrice(),
                bond.getCurrentPrice(),
                bond.getQuantity(),
                bond.getPurchaseDate(),
                bond.getCoupon(),
                bond.getYieldAmount(),
            )
        )

        conn.commit()
        print("Records created successfully")

        conn.close()
