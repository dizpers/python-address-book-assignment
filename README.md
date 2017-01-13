# python-address-book-assignment (docs WIP)

Asessment for applying to GingerPayments ([link to the original description](https://github.com/gingerpayments/hiring/blob/master/coding-assignments/python-address-book-assignment/python-address-book-assignment.rst)).
If you can't access that link, please visit [my gist with saved description](https://gist.github.com/dizpers/e427278fe10b9a2c73caa8da2261a786).

Please, feel free to checkout these 3 videos, describing the process of development (no sound, just sreen capturing):

1. https://youtu.be/JfcehW7wuU4
2. https://youtu.be/1NTcvhRgMJ8
3. https://youtu.be/KrZh-SrfEG8

# Intro

This repository contains implementation of the address book based on requirements provided by GingerPayments. Please,
feel free to use it in your applications if you love it. :)

# Installation

This library is implemented like just python package (with no setup file). So, to start using it you can just do this:

```python
from address_book import AddressBook

address_book = AddressBook()
```

# Entities

There are 3 entities (models) used in this library:

1. address book;
2. person;
3. group.

**Address book** represents actual address book. It contains persons and groups. You can perform different actions on
them.

**Person** represents the specific person.

**Group** represents the specific group of persons.

# API

## AddressBook

### Create a new address book

To create a new address book, just use the constructor of `AddressBook` class like the following:

```python
from address_book import AddressBook

addres_book = AddressBook()
```

### Add the person to the address book

To add the person (instance of `Person` class) to the address book (instance of `AddressBook` class) you should use
`add_person` method of `AddressBook` class like the following:

```python
from address_book import AddressBook, Person

# Create the new address book
address_book = AddressBook()

# Create the new person
person = Person(
    'John',
    'Doe',
    ['Russian Federation, Kemerovo region, Kemerovo, Kirova street 23, apt. 42'],
    ['+79834772053'],
    ['john@gmail.com']
)

# Add the person created above to the address book
address_book.add_person(person)
```

### Add the group to the address book

To add the group (instance of `Group` class) to the addres book (instance of `AddressBook` class) you should use
`add_group` method of `AddressBook` class like in the example below:

```python
from address_book import AddressBook, Group

# Create the address book
address_book = AddressBook()

# Create the group
group = Group('employers')

# Add that just created group to the address book:
address_book.add_group(group)
```

### Find the person in the address book

All searches of persons (instances of `Person` class) are performed by the call of the `find` method in the instance of
`AddressBook` class. Please, check the example below to see how to use it:

```python
from address_book import AddressBook, Person

# First, let's create the address book
address_book = AddressBook()

# Then let's add some people to it
address_book.add_person(Person(
    'John',
    'Doe',
    ['Russian Federation, Kemerovo region, Kemerovo, Kirova street 23, apt. 42'],
    ['+79834772053'],
    ['john@gmail.com']
))
address_book.add_person(Person(
    'Ivan',
    'Doe',
    ['Russian Federation, Kemerovo region, Kemerovo, Kirova street 23, apt. 42'],
    ['+79834772053'],
    ['john@gmail.com']
))

# Let's find person with first name `Ivan`
ivan_person = address_book.find(first_name='Ivan')
```

## Person

## Group

# Design question

The original task asks for the answer to the following question:

```text
Find person by email address (can supply any substring, ie. "comp" should work assuming "alexander@company.com" is an 
email address in the address book) - discuss how you would implement this without coding the solution.
```



# Test

To run whole test suite just use this command:

```
nosetests
```
