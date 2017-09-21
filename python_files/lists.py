class Lists (object):
    def __init__(self):
        self.shoplists = [] 

    #Method to add a shopping list
    def add(self, shoplist):
        self.shoplists.append(shoplist)

    #Method to remove a shopping list
    def remove(self,shoplist):
        self.shoplists.remove(shoplist)
