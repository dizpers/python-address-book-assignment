# python-address-book-assignment

Asessment for applying to GingerPayments ([link to the original description](https://github.com/gingerpayments/hiring/blob/master/coding-assignments/python-address-book-assignment/python-address-book-assignment.rst)).

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

There are 3 entities used in this library:

1. address book;
2. person;
3. group.

**Address book** represents actual address book. It contains persons and groups. You can perform different actions on
them.

**Person** represents the specific person.

**Group** represents the specific group of persons.

# API

## AddressBook

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
