from unittest import TestCase

from address_book import Person, Group


class GroupTestCase(TestCase):

    def get_persons(self):
        john_person = Person(
            'John',
            'Doe',
            ['Russian Federation, Kemerovo region, Kemerovo, Kirova street 23, apt. 42'],
            ['+79834772053'],
            ['john@gmail.com']
        )
        ivan_person = Person(
            'Ivan',
            'Sidorov',
            ['Russian Federation, Kemerovo region, Belovo, Kirova street 42, apt. 13'],
            ['+79834771122'],
            ['john@gmail.com']
        )
        group = Group('friends')
        self.assertFalse(group.persons)
        group.add_person(ivan_person)
        group.add_person(john_person)
        self.assertEqual(
            group.persons,
            [ivan_person, john_person]
        )
