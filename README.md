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

To be done

## Group

To be done

# Design question

The original task asks for the answer to the following question:

```text
Find person by email address (can supply any substring, ie. "comp" should work assuming "alexander@company.com" is an 
email address in the address book) - discuss how you would implement this without coding the solution.
```

The easiest way to perform such check is to use `in` clause like this:

```python
assert 'comp' in 'alexander@company.com'
```

Another way is to use regular expressions. It could be done like this:

```python
import re

assert re.search(r'comp', 'alexander@company.com')
assert re.search(r'^alex.*com$', 'alexander@company.com')
assert re.search(r'^alex.*ru$', 'alexander@company.com') is None
```

Both solutions can solve the problem. In the meantime, using regexp is much more powerful and require understanding of
regular expressions syntax (PCRE). So, I think using the first option is the best way. We can (and I think should) move
to regular expressions solutions in future to give more flexibility in searching things.

So, now we agreed to use Python's `in` clause to perform the check described in the question. The next step is to insert
that check in proper place. Search performed by [`find` method](address_book/address_book.py#L20) of `AddressBook`
class. The purpose of that method is to build the search query and iterate through all persons together with calling
`match` method on each person with search query as an argument. [`match` method](address_book/person.py#L30) of `Person`
class parse the search query and check if current instance of `Person` class match it or not. For emails checking we
have the [special block](address_book/person.py#L42-L50). So, we should insert our check at line 46. The match method
will look like this (I've added regexp option in comments too):

```python
def match(self, **match_fields):
    matches = {}

    for field, value in match_fields.iteritems():
        #TODO: sounds like the hack :3
        if field == 'email':
            field = 'emails'
            value = [value]

        self_value = getattr(self, field)

        if type(value) == list:
            if field == 'emails':
                matched = True
                for search_email in value:
                    for actual_email in self_value:
#                       Original line:
#                        if actual_email.startswith(search_email):
                        if search_email in actual_email:
#                       Regexp option:
#                        import re
#                        if re.search(search_email, actual_email):
                            break
                    else:
                        matched = False
                        break
            else:
                matched = set(self_value).issuperset(set(value))
        else:
            matched = self_value == value

        matches[field] = matched

    if all(matches.values()):
        return True

    return False
```

# Test

To run whole test suite just use this command:

```
nosetests
```

# TODO

There's still the big room for improvements. Some ideas are:

1. loading and saving the address book in some kind of db;
2. let the `find` method of `AddressBook` class to search for both persons and groups;
3. let the `find` method of `AddressBook` class to return a list of results, not just first match;
4. implement regexp matching for `find` method of `AddressBook` class;
5. check the necessity and ways of reducing memory usage (we're duplicating data for now);
6. add "setup file" to make this package distributable;
7. make `Person` instances matching modular by encapsulation related stuff for each attribute type in, for example, classes.