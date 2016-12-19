from unittest import TestCase

from address_book import AddressBook, Person, Group


class AddressBookTestCase(TestCase):

    def test_add_person(self):
        address_book = AddressBook()
        person = Person(
            'John',
            'Doe',
            ['Russian Federation, Kemerovo region, Kemerovo, Kirova street 23, apt. 42'],
            ['+79834772053']
        )
        address_book.add_person(person)
        self.assertIn(person, address_book)

    def test_add_group(self):
        address_book = AddressBook()
        group = Group('Brozzz')
        address_book.add_group(group)
        self.assertIn(group, address_book)

    def test_find_person_by_first_name(self):
        address_book = AddressBook()
        john_person = Person(
            'John',
            'Doe',
            ['Russian Federation, Kemerovo region, Kemerovo, Kirova street 23, apt. 42'],
            ['+79834772053']
        )
        ivan_person = Person(
            'Ivan',
            'Doe',
            ['Russian Federation, Kemerovo region, Belovo, Kirova street 42, apt. 13'],
            ['+79834771122']
        )
        found_person = address_book.find(first_name='Ivan')
        self.assertEqual(found_person, ivan_person)

    def test_find_person_by_last_name(self):
        pass

    def test_find_person_by_email(self):
        pass