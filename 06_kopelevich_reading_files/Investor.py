from Id import Id


# Create an Investor class with address and phone number attributes
class Investor:
    def __init__(self, first_name, last_name, address, phoneNumber):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.phoneNumber = phoneNumber
        self.investorId = Id().id

    def getFirstName(self):
        return self.first_name

    def getLastName(self):
        return self.last_name

    def getAddress(self):
        return self.address

    def getPhoneNumber(self):
        return self.phoneNumber

    def getInvestorId(self):
        return self.investorId
