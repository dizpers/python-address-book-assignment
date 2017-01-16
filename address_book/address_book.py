from group import Group

from person import Person

__all__ = ['AddressBook']


class AddressBook(object):

    def __init__(self):
        """
        Constructor of AddressBook
        """
        self.persons = []
        self.groups = []

    def add_person(self, person):
        """
        Add the person to the address book
        :param person: person to be added
        :type person: address_book.Person
        """
        self.persons.append(person)

    def add_group(self, group):
        """
        Add group to the address book
        :param group: Add the group to the address book
        :type group: address_book.Group
        """
        self.groups.append(group)

    def find(self, **kwargs):
        """
        Search for the peron in the address book
        :param kwargs: Search arguments, which should be in address_book.Person.searchable_fields list
        :return: Found person or None
        :rtype: address_book.Person or None
        """
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
