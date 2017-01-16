__all__ = ['Group']


class Group(object):

    def __init__(self, name):
        """
        Constructor of Group
        :param name: name of the gorup
        :type name: str or unicode
        """
        self.name = name
        self.persons = []

    def add_person(self, person, update_person=True):
        """
        Connect current group with the given person
        :param person: person to be added
        :param update_person: indicates if we also must update the person instance, connect to the group
        :type person: address_book.Person
        :type update_person: bool
        """
        self.persons.append(person)
        if update_person:
            person.add_to_group(self, update_group=False)
