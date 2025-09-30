class CoffeeMaker:
    def __init__(self):
        self.resources = {
            "water" : 1000,
            "milk" : 600,
            "coffee" : 300,
        }

    def report(self):
        """Print Report of All Resources"""
        print(f"Milk = {self.resources["milk"]}ml")
        print(f"Water = {self.resources["water"]}ml")
        print(f"Coffee = {self.resources["coffee"]}g")

    def is_resources_sufficient(self , drink):
        for item in drink.ingredients:
            if self.resources[item] < drink.ingredients[item]:
                return False
        return True
    def make_coffee(self , drink):
        """deduct ingredients amount from the resources"""
        for item in drink.ingredients:
            self.resources[item] -= drink.ingredients[item]
        print(f"Here is your {drink.name} , Enjoy.")


