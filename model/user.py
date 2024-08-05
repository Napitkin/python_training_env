from sys import maxsize


class User:
    def __init__(self, first_name=None, last_name=None, tel_home=None, tel_mobile=None, tel_work=None, tel_fax=None, id=None):
        self.first_name = first_name
        self.last_name = last_name
        self.tel_home = tel_home
        self.tel_mobile = tel_mobile
        self.tel_work = tel_work
        self.tel_fax = tel_fax
        self.id = id

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.first_name, self.last_name)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.first_name == other.first_name and self.last_name == other.last_name

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
