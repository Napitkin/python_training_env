import pymysql.cursors
from model.group import Group
from model.user import User


class DbFixture:
    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password, autocommit=True)

    # Загружаем из БД инф. о группах
    def get_group_list(self):
        group_list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                group_list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return group_list

    # Загружаем из БД инф. о пользователях
    def get_user_list(self):
        user_list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname from addressbook")
            for row in cursor:
                (id, firstname, lastname) = row
                user_list.append(User(id=str(id), first_name=firstname, last_name=lastname))
        finally:
            cursor.close()
        return user_list

    def destroy(self):
        self.connection.close()
