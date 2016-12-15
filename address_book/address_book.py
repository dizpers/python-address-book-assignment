__all__ = ['AddressBook']


class AddressBook(object):

    def __init__(self):
        self.persons = []

    def add_person(self, person):
        self.persons.append(person)
