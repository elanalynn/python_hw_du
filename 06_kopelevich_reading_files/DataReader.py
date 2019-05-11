# Import required Python libraries
import datetime
import csv


class DataReader:
    def getStockData(self):
        filename = "data_stocks.csv"
        stockData = list()
        with open(filename, newline="") as f:
            reader = csv.DictReader(
                f,
                [
                    "SYMBOL",
                    "NO_SHARES",
                    "PURCHASE_PRICE",
                    "CURRENT_VALUE",
                    "PURCHASE_DATE",
                ],
            )
            try:
                iterReader = iter(reader)
                next(iterReader)
                for row in reader:
                    stock = {
                        "symbol": row["SYMBOL"],
                        "quantity": int(row["NO_SHARES"]),
                        "purchasePrice": float(row["PURCHASE_PRICE"]),
                        "currentPrice": float(row["CURRENT_VALUE"]),
                        "purchaseDate": self.__getPurchaseDate__(row["PURCHASE_DATE"]),
                    }
                    stockData.append(stock)
            except:
                pass

        return stockData

    def getBondData(self):
        filename = "data_bonds.csv"
        bondData = list()
        with open(filename, newline="") as f:
            reader = csv.DictReader(
                f,
                [
                    "SYMBOL",
                    "NO_SHARES",
                    "PURCHASE_PRICE",
                    "CURRENT_VALUE",
                    "PURCHASE_DATE",
                    "Coupon",
                    "Yield",
                ],
            )
            try:
                iterReader = iter(reader)
                next(iterReader)
                for row in reader:
                    bond = {
                        "symbol": row["SYMBOL"],
                        "quantity": int(row["NO_SHARES"]),
                        "purchasePrice": float(row["PURCHASE_PRICE"]),
                        "currentPrice": float(row["CURRENT_VALUE"]),
                        "purchaseDate": self.__getPurchaseDate__(row["PURCHASE_DATE"]),
                        "coupon": float(row["Coupon"]),
                        "yield": float(row["Yield"]),
                    }
                    bondData.append(bond)
            except:
                pass

        return bondData

    def __getPurchaseDate__(self, purchaseDateString):
        split = purchaseDateString.split("/")
        return datetime.date(int(split[2]), int(split[0]), int(split[1]))
