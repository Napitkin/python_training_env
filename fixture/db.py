import pymysql.cursors
from model.group import Group
from model.user import User
from test.test_phones import merge_phones_like_on_home_page, merge_emails_like_on_home_page


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
            cursor.execute("select id, firstname, lastname, address, home, mobile, work, email, email2, email3  from addressbook")
            for row in cursor:
                (id, firstname, lastname, address, home, mobile, work, email, email2, email3) = row
                user_list.append(User(id=str(id), first_name=firstname, last_name=lastname, address=address,
                                      tel_home=home, tel_mobile=mobile, tel_work=work, email=email, email_2=email2, email_3=email3))
        finally:
            cursor.close()

        for user in user_list:
            phones = merge_phones_like_on_home_page(user)
            emails = merge_emails_like_on_home_page(user)
            user.all_phones_from_home_page = phones
            user.all_emails_from_home_page = emails

        return user_list


    def destroy(self):
        self.connection.close()
