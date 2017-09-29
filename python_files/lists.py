class Lists (object):
    def __init__(self, shoplists = list()):
        self.shoplists = shoplists

    #Method to add a shopping list
    def add(self, shoplist):
        self.shoplists.append(shoplist)
        return self.shoplists

    #Method to remove a shopping list
    def remove(self,shoplist):
        self.shoplists.remove(shoplist)
        return self.shoplists
