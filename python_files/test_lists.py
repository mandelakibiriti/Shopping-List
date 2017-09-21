import unittest

from lists import Lists

class ListsTestCase(unittest.TestCase):
    def setUp(self):
        self.list_yangu = Lists()

    def test_add_list(self):
        self.list_yangu.add('shopping list 1')
        self.list_yangu.add('shopping list 2')
        self.list_yangu.add('shopping list 3')
        self.assertEqual(len(self.list_yangu.shoplists), 3, msg = "Invalid")

        def test_remove_item(self):
            self.list_yangu.remove('shopping list 1')
            self.assertEqual(len(self.list_yangu.shoplists), 2, msg = "Invalid")