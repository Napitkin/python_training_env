from sys import maxsize


class User:
    def __init__(self, first_name=None, last_name=None, address=None, tel_home=None, tel_mobile=None, tel_work=None, email=None, email_2=None, email_3=None,
                 id=None, all_phones_from_home_page=None, all_emails_from_home_page=None):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.tel_home = tel_home
        self.tel_mobile = tel_mobile
        self.tel_work = tel_work
        self.email = email
        self.email_2 = email_2
        self.email_3 = email_3
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_emails_from_home_page = all_emails_from_home_page
        self.id = id

    def __repr__(self):
        return "%s:%s;%s" % (self.id, self.first_name, self.last_name)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.first_name == other.first_name and self.last_name == other.last_name

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
