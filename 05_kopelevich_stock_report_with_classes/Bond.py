from Stock import Stock
from Id import Id


# Create a Bond class that inherits from the Stock class and adds coupon and yield attributes
class Bond(Stock):
    def __init__(
        self,
        symbol,
        purchasePrice,
        currentPrice,
        quantity,
        coupon,
        yieldAmount,
        purchaseDate,
    ):
        Stock.__init__(
            self, symbol, purchasePrice, currentPrice, quantity, purchaseDate
        )
        self.coupon = coupon
        self.yieldAmount = yieldAmount

    def getCoupon(self):
        return self.coupon

    def getYieldAmount(self):
        return self.yieldAmount
