from unittest import TestCase

from address_book import AddressBook, Person


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
        pass

    def test_find_person_by_first_name(self):
        pass

    def test_find_person_by_last_name(self):
        pass

    def test_find_person_by_email(self):
        passjjj