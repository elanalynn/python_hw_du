from Report import Report
from DataReader import DataReader


def main():
    # Get data path
    filename = "allStocks.json"

    # Initialize dataReader and get data
    dataReader = DataReader(filename)
    data = dataReader.getData()

    # Initialize a report and call print
    report = Report(data)
    report.print()


main()
