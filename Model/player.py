from Model.abstract_member import AbstractMember
from sqlalchemy import Column, Integer, String


class Player(AbstractMember):
    """ Creates Player object """

    player_position = Column(String(50))
    jersey_number = Column(String(50))
    hourly_wage = Column(Integer)

    def __init__(self, f_name, l_name, address, phone, position, jersey_number, hourly_wage, type):
        """ Initialize Player with parameters """

        AbstractMember._validate_string_input('Player Position', position)
        AbstractMember._validate_int_input('Jersey Number', jersey_number)
        Player._validate_float_input('Hourly Wage', hourly_wage)

        super().__init__(f_name, l_name, address, phone, type)
        self.player_position = position
        self.jersey_number = jersey_number
        self.hourly_wage = hourly_wage

    def to_dict(self):
        dict = {}
        dict['id'] = self.member_id
        dict['f_name'] = self.f_name
        dict['l_name'] = self.l_name
        dict['address'] = self.address
        dict['phone'] = self.phone
        dict['player_position'] = self.player_position
        dict['jersey_number'] = self.jersey_number
        dict['hourly_wage'] = self.hourly_wage
        dict['type'] = self.type
        return dict

    def get_details(self):
        """ Returns a formatted sting of all manager details """
        details = 'Id: %d\nFirst\nName: %s\nLast Name: %s\nAddress: %s\nPhone: %s\nPlayer Position: %s\n' \
                  'Jersey Number: %d\nHourly Wage: %f\n' % (self.member_id, self.f_name, self.l_name,
                                                            self.address, self.phone, self.player_position,
                                                            self.jersey_number, self.hourly_wage)

        return details

    def copy(self, member):
        """ Copies data from object to object """
        if isinstance(member, Player):
            self.member_id = member.member_id
            self.f_name = member.f_name
            self.l_name = member.l_name
            self.phone = member.phone
            self.address = member.address
            self.type = member.type
            self.hourly_wage = member.hourly_wage
            self.jersey_number = member.jersey_number
            self.player_position = member.player_position
        else:
            self.member_id = member.member_id
            self.f_name = member.f_name
            self.l_name = member.l_name
            self.phone = member.phone
            self.address = member.address
            self.type = member.type
            self.salary = member.salary
            self.manager_position = member.manager_position

    @staticmethod
    def _validate_float_input(display_name, temp):
        """ Private helper to validate float values """

        if temp is None:
            raise ValueError(display_name + " cannot be undefined.")

        if type(temp) is not float:
            raise ValueError(display_name + " has to be float.")
