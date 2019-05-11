from Id import Id
from Stock import Stock
from Bond import Bond


# Create a Portfolio class
class Portfolio:
    def __init__(self, investor, stocks=[], bonds=[]):
        self.investor = investor
        self.stocks = stocks
        self.bonds = bonds
        self.portfolioId = Id().id

    def getInvestor(self):
        return self.investor

    def getStocks(self):
        return self.stocks

    def getBonds(self):
        return self.bonds

    def getPortfolioId(self):
        return self.portfolioId

    # Create stocks from raw stock data
    def addStocks(self, stockData):
        for stock in stockData:
            stockObject = Stock(
                stock["symbol"],
                stock["purchasePrice"],
                stock["currentPrice"],
                stock["quantity"],
                stock["purchaseDate"],
            )

            self.addStock(stockObject)

    # Add a single stock to the list of stocks
    def addStock(self, stock):
        self.stocks.append(stock)

    # Create stocks from raw stock data
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

            self.addBond(bondObject)

    # Create bonds from raw bond data
    # Not used in this exercise, but included for consistency
    def addBond(self, bondData):
        print(bondData)
        for bond in bondData:
            bondObject = bond(
                bond["symbol"],
                bond["purchasePrice"],
                bond["currentPrice"],
                bond["quantity"],
                bond["purchaseDate"],
                bond["coupon"],
                bond["yield"],
            )

            self.addBond(bondObject)

    # Add a single bond to the list of stocbondsks
    def addBond(self, bond):
        self.bonds.append(bond)

