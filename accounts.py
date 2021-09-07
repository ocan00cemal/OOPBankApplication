class Accounts():

    account_list = []
    account_dict = {}

    def __init__(self, name, pin, card_no, balance = 0):
        self.name = name
        self.pin = pin
        self.balance = balance
        self.card_no = card_no
        self.add_list()
        self.add_dict()

    def add_list(self):
        self.account_list.append(self)

    def add_dict(self):
        self.account_dict[self.name] = self
