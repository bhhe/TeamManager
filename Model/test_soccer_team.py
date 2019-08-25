import unittest
from Model.soccer_team import SoccerTeam
from Model.manager import Manager
from Model.player import Player
import inspect
import os

from sqlalchemy import create_engine
from Model.base import Base


class TestSoccerTeam(unittest.TestCase):
    """ Unit Tests for the Soccer Team Class """

    def setUp(self):
        """ Creates a test fixture before each test method is run """

        engine = create_engine('sqlite:///test_members.sqlite')

        # Creates all the tables
        Base.metadata.create_all(engine)
        Base.metadata.bind = engine

        self.member_mgr = SoccerTeam('test_members.sqlite')

        self.logPoint()

    def tearDown(self):
        os.remove('test_members.sqlite')
        self.logPoint()

    def logPoint(self):
        currentTest = self.id().split('.')[-1]
        callingFunction = inspect.stack()[1][3]
        print('in %s - %s()' % (currentTest, callingFunction))

    def test_constructor_valid(self):
        """ 010A - Valid Construction """
        engine = create_engine('sqlite:///test_members.sqlite')

        # Creates all the tables
        Base.metadata.create_all(engine)
        Base.metadata.bind = engine
        self.assertTrue(isinstance(self.member_mgr, SoccerTeam))

    def test_constructor_invalid(self):
        """ 010B - Invalid Construction """
        self.assertRaisesRegex(ValueError, "Invalid Database File", SoccerTeam, "")
        self.assertRaisesRegex(ValueError, "Invalid Database File", SoccerTeam, None)

    def test_add_member(self):
        """ 020A - Successfully add member to soccer team """

        manager = Manager('M2.F NAME', 'M2.L NAME', 'M2.ADDR', 'M2.PHONE', 'M2.POSITION', 60000, "manager")
        player = Player('P1.F NAME', 'P1.L NAME', 'P1.ADDR', 'P1.PHONE', 'P1.POSITION', 41, 50.1, 'player')

        self.member_mgr.add_member(manager)
        all_points = self.member_mgr.get_team_members()
        self.assertEqual(len(all_points), 1)

        self.member_mgr.add_member(player)
        all_points = self.member_mgr.get_team_members()
        self.assertEqual(len(all_points), 2)

    def test_add_student_invalid(self):
        """ 020B - Invalid Add student parameters """

        self.assertRaisesRegex(ValueError, "Invalid Member Object", self.member_mgr.add_member, None)
        self.assertRaisesRegex(ValueError, "Invalid Member Object", self.member_mgr.add_member, [])
        self.assertRaisesRegex(ValueError, "Invalid Member Object", self.member_mgr.add_member, "")

    def test_get_member(self):
        """ 030A - valid Soccer Team member return by id """
        manager = Manager('M2.F NAME', 'M2.L NAME', 'M2.ADDR', 'M2.PHONE', 'M2.POSITION', 60000, "manager")
        player = Player('P1.F NAME', 'P1.L NAME', 'P1.ADDR', 'P1.PHONE', 'P1.POSITION', 41, 50.1, 'player')

        id = self.member_mgr.add_member(manager)
        temp_student = self.member_mgr.get_member(id)
        self.assertEqual(manager.member_id, temp_student.member_id)

        id = self.member_mgr.add_member(player)
        temp_student = self.member_mgr.get_member(id)
        self.assertEqual(player.member_id, temp_student.member_id)

    def test_get_member_fail(self):
        """ 030B - Failed member retrieval by id"""

        self.assertRaisesRegex(ValueError, "Member does not exist", self.member_mgr.get_member, 99)

    def test_get_team_members(self):
        """ 040A - Successful Soccer Team List Member Retrieval """

        manager = Manager('M2.F NAME', 'M2.L NAME', 'M2.ADDR', 'M2.PHONE', 'M2.POSITION', 60000, "manager")
        player = Player('P1.F NAME', 'P1.L NAME', 'P1.ADDR', 'P1.PHONE', 'P1.POSITION', 41, 50.1, 'player')

        members = self.member_mgr.get_team_members()
        self.assertEqual(len(members), 0)

        self.member_mgr.add_member(manager)
        self.member_mgr.add_member(player)

        students = self.member_mgr.get_team_members()
        self.assertEqual(len(students), 2)

    def test_get_members_by_type(self):
        """ 050A - Successful Soccer Team List Member Retrieval Type """

        manager = Manager('M2.F NAME', 'M2.L NAME', 'M2.ADDR', 'M2.PHONE', 'M2.POSITION', 60000, "manager")
        player = Player('P1.F NAME', 'P1.L NAME', 'P1.ADDR', 'P1.PHONE', 'P1.POSITION', 41, 50.1, 'player')

        members = self.member_mgr.get_team_members()
        self.assertEqual(len(members), 0)

        self.member_mgr.add_member(manager)
        self.member_mgr.add_member(player)

        students1 = self.member_mgr.get_member_by_type("player")
        self.assertEqual(len(students1), 1)

        students2 = self.member_mgr.get_member_by_type("manager")
        self.assertEqual(len(students2), 1)

    def test_update_member(self):
        """ 060A - Successfully update to member in soccer team """
        manager = Manager('M1.F NAME', 'M2.L NAME', 'M2.ADDR', 'M2.PHONE', 'M2.POSITION', 60000, "manager")
        manager2 = Manager('M2.F NAME', 'M2.L NAME', 'M2.ADDR', 'M2.PHONE', 'M2.POSITION', 60000, "manager")
        manager2.member_id = 1

        self.assertEqual(len(self.member_mgr.get_team_members()), 0, "There should be no members in the list")
        id_m = self.member_mgr.add_member(manager)
        initial_details = manager.get_details()

        self.assertEqual(self.member_mgr.get_member(id_m).get_details(), initial_details,
                         "Member details should match")
        self.member_mgr.update(manager2)
        self.assertNotEqual(self.member_mgr.get_member(1).get_details(), initial_details,
                            "Member details should match")
        self.assertEqual(self.member_mgr.get_member(1).get_details(), manager2.get_details(),
                         "Member details should match")

    def test_update_member_none(self):
        """ 060B - Fail Update non integer number"""
        self.assertRaises(ValueError, self.member_mgr.delete, "1")


    def test_delete_member(self):
        """ 070A - Successfully delete member in soccer team"""
        manager = Manager('M2.F NAME', 'M2.L NAME', 'M2.ADDR', 'M2.PHONE', 'M2.POSITION', 60000, "manager")
        player = Player('P1.F NAME', 'P1.L NAME', 'P1.ADDR', 'P1.PHONE', 'P1.POSITION', 41, 50.1, 'player')

        self.assertEqual(len(self.member_mgr.get_team_members()), 0, "There should be no members in the list")
        self.member_mgr.add_member(player)

        self.assertEqual(len(self.member_mgr.get_team_members()), 1, "There should be 1 member in the list")
        self.member_mgr.delete(player.member_id)

        self.assertEqual(len(self.member_mgr.get_team_members()), 0, "There should be no members in the list")

        """ Manager delete """
        self.assertEqual(len(self.member_mgr.get_team_members()), 0, "There should be no members in the list")
        self.member_mgr.add_member(manager)

        self.assertEqual(len(self.member_mgr.get_team_members()), 1, "There should be 1 member in the list")
        self.member_mgr.delete(manager.member_id)

        self.assertEqual(len(self.member_mgr.get_team_members()), 0, "There should be no members in the list")

    def test_delete_member_invalid(self):
        """ 070B - Invalid Delete student parameters """

        self.assertRaisesRegex(ValueError, "Invalid Member Id", self.member_mgr.delete,
                               "")
        self.assertRaisesRegex(ValueError, "Invalid Member Id", self.member_mgr.delete,
                               None)


if __name__ == "__main__":
    unittest.main()


