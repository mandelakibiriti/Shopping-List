import unittest

from shopping_list import ShoppingList

class ShoppingListTestCase(unittest.TestCase):
    def setUp(self):
        self.shop_list_yangu = ShoppingList()

    def test_add_item(self):
        self.shop_list_yangu.add('shoe')
        self.shop_list_yangu.add('pen')
        self.shop_list_yangu.add('book')
        self.assertEqual(len(self.shop_list_yangu.items), 3, msg = "Invalid")

        def test_remove_item(self):
            self.shop_list_yangu.remove('shoe')
            self.assertEqual(len(self.shop_list_yangu.items), 2, msg = "Invalid")