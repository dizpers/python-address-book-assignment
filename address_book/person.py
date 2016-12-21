__all__ = ['Person']


class Person(object):

    def __init__(self, first_name, last_name, addresses, phone_numbers, emails):
        self.first_name = first_name
        self.last_name = last_name
        self.addresses = addresses
        self.phone_numbers = phone_numbers
        #TODO: have some method to add more emails -> we have to store list of mails
        self.emails = emails

    def add_address(self, address):
        self.addresses.append(address)

    def add_phone_number(self, phone_number):
        self.phone_numbers.append(phone_number)