__all__ = ['Group']


class Group(object):

    def __init__(self, name):
        self.name = name
        self.persons = []

    def add_person(self, person, update_person=True):
        self.persons.append(person)
        if update_person:
            person.add_to_group(self, update_group=False)
