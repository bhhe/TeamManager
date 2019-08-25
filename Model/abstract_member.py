from sqlalchemy import Column, Integer, String
from Model.base import Base


class AbstractMember(Base):
    """ Creates an AbstractMember object """
    __tablename__ = 'members'

    member_id = Column(Integer, primary_key=True)
    f_name = Column(String(250), nullable=False)
    l_name = Column(String(250), nullable=False)
    address = Column(String(100), nullable=False)
    phone = Column(String(20), nullable=False)
    type = Column(String(20), nullable=False)

    def __init__(self, f_name, l_name, address, phone, type):
        """ Initialize Abstract Member with parameter values """


        AbstractMember._validate_string_input('First Name', f_name)
        AbstractMember._validate_string_input('Last Name', l_name)
        AbstractMember._validate_string_input('Address', address)
        AbstractMember._validate_string_input('Phone', phone)


        self.f_name = f_name
        self.l_name = l_name
        self.address = address
        self.phone = phone
        self.type = type

    def to_dict(self):
        raise NotImplementedError('Abstract Method to Dict must be implemented')

    def get_details(self):
        raise NotImplementedError('Abstract Method Get Details must be implemented.')

    def copy(self, member):
        raise NotImplementedError('Abstract Method Copy must be implemented')

    @staticmethod
    def _validate_int_input(display_name, seq):
        """ Private helper to validate int values """
        if seq is None:
            raise ValueError(display_name + " cannot be undefined.")

        if type(seq) is not int:
            raise ValueError(display_name + " has to be an int.")

    @staticmethod
    def _validate_string_input(display_name, str_value):
        """ Private helper to validate string values """

        if str_value is None:
            raise ValueError(display_name + " cannot be undefined.")

        if str_value == "":
            raise ValueError(display_name + " cannot be empty.")