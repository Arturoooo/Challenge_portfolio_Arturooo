import unittest

from unittest.loader import makeSuite

from test_cases.framework import Test
from test_cases.login_to_the_system import TestLoginPage
from test_cases.Add_a_Playerr import TestAddAPlayer
from test_cases.Add_a_real_player import testAddARealPlayer
from test_cases.Add_Language import TestAddLanguage
from test_cases.add_player_only_name import TestAddAPlayerOnlyName
from test_cases.drop_down_list import testDropdownList
from test_cases.Trash_button import testRemoveLanguageButton
def full_suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(makeSuite(TestLoginPage))
    test_suite.addTest(makeSuite(testAddARealPlayer))
    return test_suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(full_suite())