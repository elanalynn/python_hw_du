# import the random library
import random


# Create an Id to genereate random Ids - not a real world solution as it is possible to generate duplicates this way. Since we don't have persitance, using this method as a rough solution.
class Id:
    def __init__(self):
        self.id = random.randint(1, 1000000000)
