from copy import copy

from unittest import TestCase

from address_book import Person, Group


class PersonTestCase(TestCase):

    def test_get_groups(self):
        person = Person(
            'John',
            'Doe',
            ['Russian Federation, Kemerovo region, Kemerovo, Kirova street 23, apt. 42'],
            ['+79834772053'],
            ['john@gmail.com']
        )
        self.assertFalse(person.groups)
        group_friends = Group('friends')
        group_family = Group('family')
        person.add_to_group(group_friends)
        person.add_to_group(group_family)
        self.assertEqual(
            person.groups,
            [group_friends, group_family]
        )
        self.assertIn(person, group_friends.persons)
        self.assertIn(person, group_family.persons)

    def test_add_address(self):
        basic_address = ['Russian Federation, Kemerovo region, Kemerovo, Kirova street 23, apt. 42']
        person = Person(
            'John',
            'Doe',
            copy(basic_address),
            ['+79834772053'],
            ['john@gmail.com']
        )
        person.add_address('new address')
        self.assertEqual(
            person.addresses,
            basic_address + ['new address']
        )

    def test_add_phone(self):
        basic_phone = ['+79237778492']
        person = Person(
            'John',
            'Doe',
            ['Russian Federation, Kemerovo region, Kemerovo, Kirova street 23, apt. 42'],
            copy(basic_phone),
            ['john@gmail.com']
        )
        person.add_phone_number('+79234478810')
        self.assertEqual(
            person.phone_numbers,
            basic_phone + ['+79234478810']
        )

    def test_add_email(self):
        basic_email = ['john@gmail.com']
        person = Person(
            'John',
            'Doe',
            ['Russian Federation, Kemerovo region, Kemerovo, Kirova street 23, apt. 42'],
            ['+79834772053'],
            copy(basic_email)
        )
        person.add_email('new@mail.net')
        self.assertEqual(
            person.emails,
            basic_email + ['new@mail.net']
        )
