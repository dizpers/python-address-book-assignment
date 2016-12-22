__all__ = ['Person']


class Person(object):

    searchable_fields = ['first_name', 'last_name', 'email']

    def __init__(self, first_name, last_name, addresses, phone_numbers, emails):
        self.first_name = first_name
        self.last_name = last_name
        self.addresses = addresses
        self.phone_numbers = phone_numbers
        self.emails = emails
        self.groups = []

    def add_address(self, address):
        self.addresses.append(address)

    def add_phone_number(self, phone_number):
        self.phone_numbers.append(phone_number)

    def add_email(self, email):
        self.emails.append(email)

    def add_to_group(self, group, update_group=True):
        self.groups.append(group)
        if update_group:
            group.add_person(self, update_person=False)

    def match(self, **match_fields):
        matches = {}

        for field, value in match_fields.iteritems():
            #TODO: sounds like the hack :3
            if field == 'email':
                field = 'emails'
                value = [value]

            self_value = getattr(self, field)

            if type(value) == list:
                matched = set(self_value).issuperset(value)
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