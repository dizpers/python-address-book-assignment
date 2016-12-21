from group import Group

from person import Person

__all__ = ['AddressBook']


class AddressBook(object):

    def __init__(self):
        self.persons = []
        self.groups = []

    def add_person(self, person):
        self.persons.append(person)

    def add_group(self, group):
        self.groups.append(group)

    def find(self, **kwargs):
        first_name = kwargs.get('first_name')
        last_name = kwargs.get('last_name')
        email = kwargs.get('email')
        if not (first_name or last_name or email):
            return
        for person in self.persons:
            if person.first_name == first_name:
                return person
            if person.last_name == last_name:
                return person
            # TODO: person.emails?
            if email in person.email:
                return person


    def __contains__(self, item):
        if isinstance(item, Person):
            return item in self.persons
        if isinstance(item, Group):
            return item in self.groups
        return False
