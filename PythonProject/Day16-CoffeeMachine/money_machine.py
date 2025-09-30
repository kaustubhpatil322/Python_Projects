
class MoneyMachine:
    CURRENCY = '$'
    COIN_VALUES = {
        "penny" : 0.01,
        "nickel": 0.05,
        "dime": 0.10,
        "quarter":0.25,
    }

    def __init__(self):
        self.profit  = 0
        self.money_received = 0
    def report(self):
        print(f"Profit = {self.CURRENCY}{self.profit}")

    def process_coins(self):
        print("please enter the coins as follows:")

        for coin in self.COIN_VALUES:
            self.money_received += int(input(f"How many {coin}?\n")) * self.COIN_VALUES[coin]
        return self.money_received

    def make_payment(self,cost):
        """Deduct the price of an order from the money_received and return the change"""
        self.process_coins()
        if self.money_received < cost:
            print(f"The amount {self.CURRENCY}{cost} is insufficient to process your Order,")
            print("Your money is to be refunded back in a moment")
            self.money_received = 0
            return False
        else:
            self.profit += cost
            change = round((self.money_received - cost)*100)/100
            print(f"Here is your change: {self.CURRENCY}{change}")
            self.money_received = 0
            return True


