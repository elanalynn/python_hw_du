import pygal
from pygal import Config
from pygal.style import LightSolarizedStyle
import datetime


class Report:
    def __init__(self, data):
        self.data = data

    def print(self):
        self.__renderLineGraph__()
        self.__renderPieChart__()

    def __renderPieChart__(self):
        # Get a list of stocks values sorted by closing value
        sortedValues = self.__sortClosingValues__()

        # Initalize pie chart
        chart = pygal.Pie()
        chart.title = "Closing Value Distribution of Stocks in the Portfolio"

        counts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        for value in sortedValues:
            if value < 100:
                counts[0] += 1
            elif value < 200:
                counts[1] += 1
            elif value < 300:
                counts[2] += 1
            elif value < 400:
                counts[3] += 1
            elif value < 500:
                counts[4] += 1
            elif value < 600:
                counts[5] += 1
            elif value < 700:
                counts[6] += 1
            elif value < 800:
                counts[7] += 1
            elif value < 900:
                counts[8] += 1
            else:
                counts[9] += 1

        for i, count in enumerate(counts):
            chart.add(f"${i}00 - ${i+1}00", count)

        chart.render_to_file("pieDistribution.svg")

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

    def __sortClosingValues__(self):
        closingValues = []

        for stock in self.data:
            closingValues.append(float(stock["Close"]))

        closingValues.sort()

        return closingValues

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
