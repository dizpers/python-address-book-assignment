from unittest import TestCase

from address_book import AddressBook, Person, Group


class AddressBookTestCase(TestCase):

    def test_add_person(self):
        address_book = AddressBook()
        person = Person(
            'John',
            'Doe',
            ['Russian Federation, Kemerovo region, Kemerovo, Kirova street 23, apt. 42'],
            ['+79834772053'],
            ['john@gmail.com']
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
            ['+79834772053'],
            ['john@gmail.com']
        )
        ivan_person = Person(
            'Ivan',
            'Doe',
            ['Russian Federation, Kemerovo region, Belovo, Kirova street 42, apt. 13'],
            ['+79834771122'],
            ['ivan@kgb.ru']
        )
        address_book.add_person(john_person)
        address_book.add_person(ivan_person)
        found_person = address_book.find(first_name='Ivan')
        self.assertEqual(found_person, ivan_person)

    def test_find_person_by_last_name(self):
        address_book = AddressBook()
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
        address_book.add_person(john_person)
        address_book.add_person(ivan_person)
        found_person = address_book.find(last_name='Sidorov')
        self.assertEqual(found_person, ivan_person)

    def test_find_person_by_full_name(self):
        address_book = AddressBook()
        ivan_popov_person = Person(
            'Ivan',
            'Popov',
            ['Russian Federation, Kemerovo region, Kemerovo, Kirova street 23, apt. 42'],
            ['+79834772053'],
            ['john@gmail.com']
        )
        ivan_sidorov_person = Person(
            'Ivan',
            'Sidorov',
            ['Russian Federation, Kemerovo region, Belovo, Kirova street 42, apt. 13'],
            ['+79834771122'],
            ['john@gmail.com']
        )
        address_book.add_person(ivan_popov_person)
        address_book.add_person(ivan_sidorov_person)
        found_person = address_book.find(first_name='Ivan', last_name='Sidorov')
        self.assertEqual(found_person, ivan_sidorov_person)

    def test_find_person_by_email(self):
        address_book = AddressBook()
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
            ['ivan@kgb.ru']
        )
        address_book.add_person(john_person)
        address_book.add_person(ivan_person)
        found_person = address_book.find(email='ivan@kgb.ru')
        self.assertEqual(found_person, ivan_person)

    def test_find_person_by_set_of_emails(self):
        address_book = AddressBook()
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
            ['ivan@kgb.ru']
        )
        address_book.add_person(john_person)
        address_book.add_person(ivan_person)
        found_person = address_book.find(emails=['ivan@kgb.ru', 'sn0uden@us.gov'])
        self.assertIsNone(found_person)
        ivan_person.add_email('sn0uden@us.gov')
        found_person = address_book.find(emails=['ivan@kgb.ru', 'sn0uden@us.gov'])
        self.assertEqual(found_person, ivan_person)
