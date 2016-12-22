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
        search_args = {}

        for field in Person.searchable_fields:
            value = kwargs.get(field)
            if value:
                search_args[field] = value

        if not search_args:
            return

        for person in self.persons:
            if person.match(**search_args):
                return person

    def __contains__(self, item):
        if isinstance(item, Person):
            return item in self.persons
        if isinstance(item, Group):
            return item in self.groups
        return False
