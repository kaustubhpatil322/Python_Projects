
class MenuItem:
    """Models Each Menu Item - defines the structure of Menu Item"""
    def __init__(self, name , water , milk , coffee , cost):
        self.name = name
        self.cost = cost
        self.ingredients = {
            "water" : water,
            "milk" : milk ,
            "coffee" : coffee,
        }

class Menu:
    """provides the drinks to the menu """
    def __init__(self ):
        self.menu = [
            MenuItem(name="latte" , water =200 ,milk = 150, coffee =24 , cost =2.5 ),
            MenuItem(name="espresso", water=50, milk=0, coffee=18, cost=1.5),
            MenuItem(name="cappuccino", water=250, milk=50, coffee=24, cost=3),
        ]
    def get_items(self):
        """return all the names of the available Menu"""
        option=""
        for items in self.menu:
            option +=  f"{items.name} / "
        return option

    def find_drink(self , order_name):
        """return  the specified drink in parameter"""
        for item in self.menu:
            if item.name == order_name:
                return item
        print("Sorry , Item is not available")

    def find_cost(self, order_name):
        for drink in self.menu:
            if drink.name == order_name:
                return drink.cost





