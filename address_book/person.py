__all__ = ['Person']


class Person(object):

    def __init__(self, first_name, last_name, addresses, phone_numbers, email):
        self.first_name = first_name
        self.last_name = last_name
        self.addresses = addresses
        self.phone_numbers = phone_numbers
        #TODO: have some method to add more emails -> we have to store list of mails
        self.email = email
