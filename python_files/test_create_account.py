import unittest

from create_account import CreateAccount

class NewAccountTestCase(unittest.TestCase):
    def setUp(self):
        self.account_Mandela = CreateAccount()

    def test_account_name(self):
        self.assertEqual(self.account_Mandela.account_name, "Mandela", msg='Account name invalid')
