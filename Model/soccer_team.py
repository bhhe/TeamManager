from Model.player import Player
from Model.manager import Manager
from Model.abstract_member import AbstractMember
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Model.base import Base

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Model.base import Base

class SoccerTeam:
    """ Creates an object that holds a list of AbstractMember objects """

    def __init__(self, db_filename):
        """ Initialize SoccerTeam with based id 1 and empty list of members """
        if db_filename is None or db_filename == "":
            raise ValueError("Invalid Database File")

        self._id_count = 1
        engine = create_engine('sqlite:///' + db_filename)
        Base.metadata.bind = engine
        self._db_session = sessionmaker(bind=engine)

    def add_member(self, member):
        """ Adds an abstract member object to list """
        self._validate_member_input("Member", member)

        session = self._db_session()
        session.add(member)
        session.commit()

        member_id = member.member_id

        session.close()
        return member_id

    def get_member(self, member_id):
        """ Returns the member object that matches the given ID """
        Player._validate_int_input('Member Id', member_id)

        session = self._db_session()

        existing_member = session.query(Player).filter(Player.member_id == member_id).first()
        existing_member2 = session.query(Manager).filter(Manager.member_id == member_id).first()
        print(existing_member)
        print(existing_member2)

        session.close()
        if existing_member is None and existing_member2 is None:
            raise ValueError('Member does not exist')

        if existing_member.type == 'player':
            return existing_member
        elif existing_member2.type == 'manager':
            return existing_member2
        else:
            raise ValueError('Member does not exist')

    def get_team_members(self):
        """ Returns a list of all members in database """
        session = self._db_session()
        query1 = session.query(Player).filter(Player.type == 'player').all()
        query2 = session.query(Manager).filter(Manager.type == 'manager').all()
        existing_member = query1 + query2

        session.close()
        existing_member.sort(key=lambda x: x.member_id)
        return existing_member

    def get_member_by_type(self, member_type):
        """ Returns a list of all members of an AbstractMember type """
        type_members = []
        all = self.get_team_members()
        for member in all:
            if member.type == member_type:
                type_members.append(member)

        return type_members

    def update(self, new_member):
        """ Changes the object in the members list to a new object """

        SoccerTeam._validate_member_input('Member', new_member)
        session = self._db_session()

        existing_member = None

        if isinstance(new_member, Player):
            existing_member = session.query(Player).filter(Player.member_id == new_member.member_id).first()
        if isinstance(new_member, Manager):
            existing_member = session.query(Manager).filter(Manager.member_id == new_member.member_id).first()

        if existing_member is None:
            raise ValueError('Member does not exist')

        existing_member.copy(new_member)

        session.commit()
        session.close()

    def delete(self, member_id):
        """ Deletes a member from the database if the ID matches """

        if member_id is None or type(member_id) != int:
            raise ValueError('Invalid Member Id')

        session = self._db_session()

        existing_member = session.query(AbstractMember).filter(AbstractMember.member_id == member_id).first()
        if existing_member is None:
            raise ValueError('Member does not exist')

        session.delete(existing_member)
        session.commit()
        session.close()


    @staticmethod
    def _validate_member_input(display_name, member):
        """ Private helper to validate string values """
        print(member)
        if member is None or not isinstance(member, Player):
            if member is None or not isinstance(member, Manager):
                raise ValueError("Invalid %s Object" %(display_name))

