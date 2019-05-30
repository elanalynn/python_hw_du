# Import required Python libraries
import datetime
import json


class DataReader:
    def __init__(self, file):
        self.file = file

    def getData(self):
        filename = self.file
        with open(self.file) as all_stocks:
            data = json.load(all_stocks)
        return data
