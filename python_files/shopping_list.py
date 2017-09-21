class ShoppingList(object):
    def __init__(self):
        self.items = []

    #Method to add item
    def add(self,item):
        self.items.append(item)

    #Method to remove item
    def remove(self,item):
        self.items.remove(item)


