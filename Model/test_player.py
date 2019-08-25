import unittest
from model.player import Player
from unittest import TestCase
from unittest.mock import patch, mock_open
import inspect


class TestPlayer(TestCase):
    """ Unit Tests for the Player Class """

    # This mocks the builtin file open method in python always return '1' for the file data (we don't care
    # since we are mocking the csv reader as well.
    NO_ID = 0
    TEST_F_NAME = 'TEST George'
    TEST_L_NAME = 'TEST Guccino'
    TEST_ADDRESS = 'TEST STREET 2'
    TEST_PHONE = 'TEST 77832132132'
    TEST_PLYR_POSITION = 'TEST MANAGER POSITION 2'
    TEST_JERSEY_NUMBER = 57
    TEST_HOURLY_WAGE = 19.0

    @patch('builtins.open', mock_open(read_data='1'))
    def setUp(self):
        """ Creates a test fixture before each test method is run """
        self.logPoint()
        self.test_player = Player(self.NO_ID, self.TEST_F_NAME, self.TEST_L_NAME, self.TEST_ADDRESS,
                                  self.TEST_PHONE, self.TEST_PLYR_POSITION, self.TEST_JERSEY_NUMBER,
                                  self.TEST_HOURLY_WAGE)

    def test_manager(self):
        """ 010A - Valid Construction of the Player """
        self.assertIsNotNone(self.test_player, "Test readings must be defined")

    def test_invalid_temperature_sensor_parameter(self):
        """ 010B - Invalid Construction of the Player """

        #Must reject an undefined Player parameters

        with self.assertRaises(ValueError):
            Player(None, "Matt", "Lam", "Address", "911", "position", 1, 99999)
        with self.assertRaises(ValueError):
            Player(1, None, "Lam", "Address", "911", "position", 1, 99999)
        with self.assertRaises(ValueError):
            Player(1, "Matt", None, "Address", "911", "position", 1, 99999)
        with self.assertRaises(ValueError):
            Player(1, "Matt", "Lam", None, "911", "position", 1, 99999)
        with self.assertRaises(ValueError):
            Player(1, "Matt", "Lam", "Address", None, "position", 1, 99999)
        with self.assertRaises(ValueError):
            Player(1, "Matt", "Lam", "Address", "911", None, 1, 99999)
        with self.assertRaises(ValueError):
            Player(1, "Matt", "Lam", "Address", "911", "position", None, 99999)
        with self.assertRaises(ValueError):
            Player(1, "Matt", "Lam", "Address", "911", "position", 1, None)

        #Must reject an empty Player parameters

        with self.assertRaises(ValueError):
            Player("", "Matt", "Lam", "Address", "911", "position", 1, 99999)
        with self.assertRaises(ValueError):
            Player(1, "", "Lam", "Address", "911", "position", 1, 99999)
        with self.assertRaises(ValueError):
            Player(1, "Matt", "", "Address", "911", "position", 1, 99999)
        with self.assertRaises(ValueError):
            Player(1, "Matt", "Lam", "", "911", "position", 1, 99999)
        with self.assertRaises(ValueError):
            Player(1, "Matt", "Lam", "Address", "", "position", 1, 99999)
        with self.assertRaises(ValueError):
            Player(1, "Matt", "Lam", "Address", "911", "", 1, 99999)
        with self.assertRaises(ValueError):
            Player(1, "Matt", "Lam", "Address", "911", "position", "", 99999)
        with self.assertRaises(ValueError):
            Player(1, "Matt", "Lam", "Address", "911", "position", 1, "")

    def test_get_id(self):
        """ 020A - Valid Player Id return """
        self.assertEqual(self.test_player.get_id(), self.NO_ID)

    def test_set_id(self):
        """ 030A - Valid Player Id Change """
        test_id = 5
        self.test_player.set_id(test_id)
        self.assertEqual(self.test_player.get_id(), test_id)
        self.test_player.set_id(self.NO_ID)
        self.assertEqual(self.test_player.get_id(), self.NO_ID)

    def test_get_first_name(self):
        """ 040A - Valid Player First Name return """
        self.assertEqual(self.test_player.get_first_name(), self.TEST_F_NAME)

    def test_get_last_name(self):
        """ 050A - Valid Player Last Name return """
        self.assertEqual(self.test_player.get_last_name(), self.TEST_L_NAME)

    def test_get_address(self):
        """ 060A - Valid Player Address return """
        self.assertEqual(self.test_player.get_address(), self.TEST_ADDRESS)

    def test_get_phone(self):
        """ 070A - Valid Player Phone return """
        self.assertEqual(self.test_player.get_phone_number(), self.TEST_PHONE)

    def test_get_player_position(self):
        """ 080A - Valid Player Position return """
        self.assertEqual(self.test_player.get_player_position(), self.TEST_PLYR_POSITION)

    def test_get_jersey_number(self):
        """ 090A - Valid Player Jersey Number return """
        self.assertEqual(self.test_player.get_jersey_number(), self.TEST_JERSEY_NUMBER)

    def test_hourly_wage(self):
        """ 100A - Valid Player Hourly Wage return """
        self.assertEqual(self.test_player.get_hourly_wage(), self.TEST_HOURLY_WAGE)

    def test_to_dict(self):
        """ 11A - Valid Dictionary Return """
        dict = {}
        dict['id'] = self.test_player.get_id()
        dict['f_name'] = self.TEST_F_NAME
        dict['l_name'] = self.TEST_L_NAME
        dict['address'] = self.TEST_ADDRESS
        dict['phone'] = self.TEST_PHONE
        dict['player_position'] = self.TEST_PLYR_POSITION
        dict['hourly_wage'] = self.TEST_HOURLY_WAGE
        dict['jersey_number'] = self.TEST_JERSEY_NUMBER
        dict['type'] = self.test_player.get_type()
        self.assertEqual(dict, self.test_player.to_dict(), 'Manager Dictionary must be the same')

    def tearDown(self):
        """ Prints a log point when test is finished """
        self.logPoint()

    def logPoint(self):
        """ Utility function used for module functions and class methods """
        current_test = self.id().split('.')[-1]
        calling_function = inspect.stack()[1][3]
        print('in %s - %s()' % (current_test, calling_function))


if __name__ == "__main__":
    unittest.main()

