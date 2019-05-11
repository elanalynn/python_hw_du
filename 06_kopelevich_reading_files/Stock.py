import datetime
from Id import Id


# Create a Stock class with required attributes
class Stock:
    def __init__(self, symbol, purchasePrice, currentPrice, quantity, purchaseDate):
        self.symbol = symbol
        self.purchasePrice = purchasePrice
        self.currentPrice = currentPrice
        self.quantity = quantity
        self.purchaseDate = purchaseDate
        self.purchaseId = Id().id

    def getSymbol(self):
        return self.symbol

    def getPurchasePrice(self):
        return self.purchasePrice

    def getCurrentPrice(self):
        return self.currentPrice

    def getQuantity(self):
        return self.quantity

    def getPurchaseDate(self):
        return self.purchaseDate

    def getPurchaseId(self):
        return self.purchaseId

    # Calculates the earnings or loss for each stock symbol provided.
    def calculateEarningsOrLoss(self):
        return (self.currentPrice - self.purchasePrice) * self.quantity

    # Calculates the percentage earned or loss for each year
    def calculateYearlyEarningsOrLoss(self):
        priceDiff = self.getCurrentPrice() - self.getPurchasePrice()
        daysDiff = (datetime.date.today() - self.getPurchaseDate()).days
        yearDiff = daysDiff / 365

        return (((priceDiff / self.getPurchasePrice())) / yearDiff) * 100
