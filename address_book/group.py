__all__ = ['Group']


class Group(object):

    def __init__(self, name):
        self.name = name
        self.persons = []

    def add_person(self, person):
        self.persons.append(person)
        person.add_to_group(self)
