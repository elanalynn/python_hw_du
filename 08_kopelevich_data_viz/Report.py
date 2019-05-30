import pygal
from pygal import Config
from pygal.style import LightSolarizedStyle
import datetime


class Report:
    def __init__(self, data):
        self.data = data

    def print(self):
        self.__renderLineGraph__()

    def __renderLineGraph__(self):
        # Get a dictionary of stocks with lists of closing values
        stocksBySymbol = self.__sortStocksBySymbol__()

        # Initalize line chart
        chart = pygal.Line(
            title="Closing Prices of Stocks",
            x_title="Time",
            y_title="US Dollars",
            x_label_rotation=45,
        )

        chart.x_labels = [
            datetime.date(2015, 8, 1),
            datetime.date(2015, 12, 1),
            datetime.date(2016, 4, 1),
            datetime.date(2016, 8, 1),
            datetime.date(2016, 12, 1),
            datetime.date(2017, 4, 1),
            datetime.date(2017, 8, 1),
            datetime.date(2017, 12, 1),
        ]

        # Iterate over stock/value list to create a line for each stock
        for k, v in stocksBySymbol.items():
            # Initialize an empty list to store prices in for each stock
            prices = []

            # Iterate over each closing value
            for price in v:
                # Access the price from the item tuple and
                # convert it to a float so that Pygal can interpret it
                floatPrice = self.__formatValues__(price)
                # Add each price to the list of prices for this stock
                prices.append((floatPrice))

            # Add the line for a stock to the chart
            chart.add(k, prices, allow_interruptions=True)

        # Create the final SVG of the line chart
        chart.render_to_file("AllStocks.svg")

    def __sortStocksBySymbol__(self):
        stocksBySymbol = {}
        for stock in self.data:
            symbol = stock["Symbol"]
            if symbol not in stocksBySymbol.keys():
                stocksBySymbol[symbol] = []
            # Create and append a tuple with the date and close price to the symbol list
            stocksBySymbol[symbol].append(stock["Close"])

        # reverse the values because the json file has them in reverse order
        for v in stocksBySymbol.values():
            v.reverse()

        return stocksBySymbol

    def __formatValues__(self, value):
        try:
            formatted = float(value)
        except:
            print(f'Replacing "{value}" with None type.')
            formatted = None
        return formatted
