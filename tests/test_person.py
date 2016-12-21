from copy import copy

from unittest import TestCase

from address_book import Person


class PersonTestCase(TestCase):

    def test_get_groups(self):
        pass

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
        pass

    def test_add_email(self):
        pass