from person import Person

__all__ = ['AddressBook']


class AddressBook(object):

    def __init__(self):
        self.persons = []

    def add_person(self, person):
        self.persons.append(person)

    def __contains__(self, item):
        if isinstance(item, Person):
            return item in self.persons
        return False
