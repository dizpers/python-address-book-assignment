__all__ = ['Person']


class Person(object):

    searchable_fields = ['first_name', 'last_name', 'email', 'emails']

    def __init__(self, first_name, last_name, addresses, phone_numbers, emails):
        """
        Constructor of Person class
        :param first_name: first name of the person
        :type first_name: str or unicode
        :param last_name: last name of the person
        :type last_name: str or unicode
        :param addresses: list of person's addresses (list of strings)
        :type addresses: list
        :param phone_numbers: list of person's phone numbers (list of strings)
        :type phone_numbers: list
        :param emails: list of person's emails (list of strings)
        :type emails: list
        """
        self.first_name = first_name
        self.last_name = last_name
        self.addresses = addresses
        self.phone_numbers = phone_numbers
        self.emails = emails
        self.groups = []

    def add_address(self, address):
        """
        Add the address string to the list of addresses of current person
        :param address: address string to be added
        :type address: str or unicode
        """
        self.addresses.append(address)

    def add_phone_number(self, phone_number):
        """
        Add the phone number string to the list of phone numbers of current person
        :param phone_number: phone number string to be added
        :type phone_number: str or unicode
        """
        self.phone_numbers.append(phone_number)

    def add_email(self, email):
        """
        Add email string to the list of emails of current person
        :param email: email to be added
        :type email: str or unicode
        """
        self.emails.append(email)

    def add_to_group(self, group, update_group=True):
        """
        Connects current person and given group
        :param group: group to be extended with current person instance
        :param update_group: indicates if we also must update give group with current person
        :type group: address_book.Group
        :type update_group: bool
        """
        self.groups.append(group)
        if update_group:
            group.add_person(self, update_person=False)

    def match(self, **match_fields):
        """
        Match curren person object with set of fields
        :param match_fields: set of fields to be matched with current instance
        :return: does current person match given set of fields or not
        :rtype: bool
        """
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
                            if actual_email.startswith(search_email):
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

    def __unicode__(self):
        return u'Person<{first_name} {last_name}>'.format(
            first_name=self.first_name,
            last_name=self.last_name
        )

    def __str__(self):
        return unicode(self)

    def __repr__(self):
        return unicode(self)