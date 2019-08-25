from Model.abstract_member import AbstractMember
from sqlalchemy import Column, Integer, String


class Manager(AbstractMember):
    """ Creates a Manager object """

    manager_position = Column(String(50))
    salary = Column(Integer)

    def __init__(self, f_name, l_name, address, phone, position, salary, type):
        """ Initialize Manager with parameter values """

        AbstractMember._validate_string_input('Manager Position', position)
        AbstractMember._validate_int_input('Salary', salary)

        super().__init__(f_name, l_name, address, phone, type)
        self.manager_position = position
        self.salary = salary

    def to_dict(self):
        dict = {}
        dict['id'] = self.member_id
        dict['f_name'] = self.f_name
        dict['l_name'] = self.l_name
        dict['address'] = self.address
        dict['phone'] = self.phone
        dict['manager_position'] = self.manager_position
        dict['salary'] = self.salary
        dict['type'] = self.type

        return dict

    def get_details(self):
        """ Returns a formatted sting of all manager details """
        details = 'Id: %d\nFirst\nName: %s\nLast Name: %s\nAddress: %s\nPhone: %s\nManager Position: %s\n' \
                  'Salary: %d\n' % (self.member_id, self.f_name, self.l_name,
                                    self.address, self.phone, self.manager_position,
                                    self.salary)

        return details

    def copy(self, member):
        """ Copies data from object to object """
        if isinstance(member, Manager):
            self.member_id = member.member_id
            self.f_name = member.f_name
            self.l_name = member.l_name
            self.phone = member.phone
            self.address = member.address
            self.type = member.type
            self.salary = member.salary
            self.manager_position = member.manager_position
        else:
            self.member_id = member.member_id
            self.f_name = member.f_name
            self.l_name = member.l_name
            self.phone = member.phone
            self.address = member.address
            self.type = member.type
            self.hourly_wage = member.hourly_wage
            self.jersey_number = member.jersey_number
            self.player_position = member.player_position
