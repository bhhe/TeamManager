import unittest
from Model.manager import Manager
from unittest import TestCase
from unittest.mock import patch, mock_open
import inspect


class TestManager(TestCase):
    """ Unit Tests for the Manager Class """

    # This mocks the builtin file open method in python always return '1' for the file data (we don't care
    # since we are mocking the csv reader as well.
    NO_ID = 0
    TEST_F_NAME = 'TEST BOB'
    TEST_L_NAME = 'TEST SMITH'
    TEST_ADDRESS = 'TEST STREET'
    TEST_PHONE = 'TEST 6041234521'
    TEST_MNGR_POSITION = 'TEST MANAGER POSITION'
    TEST_SALARY = 50000

    @patch('builtins.open', mock_open(read_data='1'))
    def setUp(self):
        """ Creates a test fixture before each test method is run """
        self.logPoint()
        self.test_manager = Manager(self.NO_ID, self.TEST_F_NAME, self.TEST_L_NAME, self.TEST_ADDRESS,
                                    self.TEST_PHONE, self.TEST_MNGR_POSITION, self.TEST_SALARY)

    def test_manager(self):
        """ 010A - Valid Construction of the manager """
        self.assertIsNotNone(self.test_manager, "Test readings must be defined")

    def test_invalid_temperature_sensor_parameter(self):
        """ 010B - Invalid Construction of the manager """

        #Must reject an undefined Manager parameters

        with self.assertRaises(ValueError):
            Manager(None, "Matt", "Lam", "Address", "911", "position", 99999)
        with self.assertRaises(ValueError):
            Manager(1, None, "Lam", "Address", "911", "position", 99999)
        with self.assertRaises(ValueError):
            Manager(1, "Matt", None, "Address", "911", "position", 99999)
        with self.assertRaises(ValueError):
            Manager(1, "Matt", "Lam", None, "911", "position", 99999)
        with self.assertRaises(ValueError):
            Manager(1, "Matt", "Lam", "Address", None, "position", 99999)
        with self.assertRaises(ValueError):
            Manager(1, "Matt", "Lam", "Address", "911", None, 99999)
        with self.assertRaises(ValueError):
            Manager(1, "Matt", "Lam", "Address", "911", "position", None)

        #Must reject an empty Manager parameters

        with self.assertRaises(ValueError):
            Manager("", "Matt", "Lam", "Address", "911", "position", 99999)
        with self.assertRaises(ValueError):
            Manager(1, "", "Lam", "Address", "911", "position", 99999)
        with self.assertRaises(ValueError):
            Manager(1, "Matt", "", "Address", "911", "position", 99999)
        with self.assertRaises(ValueError):
            Manager(1, "Matt", "Lam", "", "911", "position", 99999)
        with self.assertRaises(ValueError):
            Manager(1, "Matt", "Lam", "Address", "", "position", 99999)
        with self.assertRaises(ValueError):
            Manager(1, "Matt", "Lam", "Address", "911", "", 99999)
        with self.assertRaises(ValueError):
            Manager(1, "Matt", "Lam", "Address", "911", "position", "")

    def test_get_id(self):
        """ 020A - Valid Manager Id return """
        self.assertEqual(self.test_manager.get_id(), self.NO_ID)

    def test_set_id(self):
        """ 030A - Valid Manager Id Change """
        test_id = 5
        self.test_manager.set_id(test_id)
        self.assertEqual(self.test_manager.get_id(), test_id)
        self.test_manager.set_id(self.NO_ID)
        self.assertEqual(self.test_manager.get_id(), self.NO_ID)

    def test_get_first_name(self):
        """ 040A - Valid Manager First Name return """
        self.assertEqual(self.test_manager.get_first_name(), self.TEST_F_NAME)

    def test_get_last_name(self):
        """ 050A - Valid Manager Last Name return """
        self.assertEqual(self.test_manager.get_last_name(), self.TEST_L_NAME)

    def test_get_address(self):
        """ 060A - Valid Manager Address return """
        self.assertEqual(self.test_manager.get_address(), self.TEST_ADDRESS)

    def test_get_phone_number(self):
        """ 070A - Valid Manager Phone return """
        self.assertEqual(self.test_manager.get_phone_number(), self.TEST_PHONE)

    def test_get_manager_position(self):
        """ 080A - Valid Manager Position return """
        self.assertEqual(self.test_manager.get_manager_position(), self.TEST_MNGR_POSITION)

    def test_salary(self):
        """ 090A - Valid Manager Salary return """
        self.assertEqual(self.test_manager.get_salary(), self.TEST_SALARY)

    def test_to_dict(self):
        """ 10A - Valid Dictionary Return """
        dict = {}
        dict['id'] = self.test_manager.get_id()
        dict['f_name'] = self.TEST_F_NAME
        dict['l_name'] = self.TEST_L_NAME
        dict['address'] = self.TEST_ADDRESS
        dict['phone'] = self.TEST_PHONE
        dict['manager_position'] = self.TEST_MNGR_POSITION
        dict['salary'] = self.TEST_SALARY
        dict['type'] = self.test_manager.get_type()

        self.assertEqual(dict, self.test_manager.to_dict(), 'Manager Dictionary must be the same')

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


