from model.user import User
import re


class UserHelper:
    def __init__(self, app):
        self.app = app

    def create(self, user):
        wd = self.app.wd
        self.open_page_create_user()
        # fill user form
        self.method_filling_user_form(user)
        # click button 'Enter" - create user
        wd.find_element_by_xpath("//div[@id='content']/form/input[20]").click()
        self.return_to_homepage()
        # После успешного метода (create) кэш сбрасываем
        self.user_cache = None

    def modify_first_user(self):
        self.modify_user_by_index(0)

    def modify_user_by_index(self, index, user):
        wd = self.app.wd
        self.open_homepage()
        # select random user
        self.select_user_by_index(index)
        # click button 'Edit"
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        # fill user form
        self.method_filling_user_form(user)
        # click button 'update" - modify user
        wd.find_element_by_name("update").click()
        # После успешного метода (modify) кэш сбрасываем
        self.user_cache = None

    def select_user_by_index(self, index):
        wd = self.app.wd
        # Получение всех checkbox's по index - порядковому номеру
        wd.find_elements_by_name("selected[]")[index].click()

    def delete_first_user(self):
        self.delete_user_by_index(0)

    def delete_user_by_index(self, index):
        wd = self.app.wd
        self.open_homepage()
        self.select_user_by_index(index)
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        # После успешного метода (delete) кэш сбрасываем
        self.user_cache = None

    # Заполнение формы Пользователя (User)
    def method_filling_user_form(self, user):
        wd = self.app.wd
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(user.first_name)
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(user.last_name)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(user.address)
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(user.tel_home)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(user.tel_mobile)
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(user.tel_work)
        wd.find_element_by_name("fax").click()
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys(user.tel_fax)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(user.email)
        wd.find_element_by_name("email2").click()
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys(user.email_2)
        wd.find_element_by_name("email3").click()
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys(user.email_3)

    def open_homepage(self):
        wd = self.app.wd
        if not (wd.current_url and len(wd.find_elements_by_name("add")) > 0):
            wd.find_element_by_link_text("home").click()

    def open_page_create_user(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def return_to_homepage(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()

    # Страница просмотра карточки пользователя
    def open_user_view_by_index(self, index):
        wd = self.app.wd
        self.open_homepage()
        self.select_user_by_index(index)
        wd.find_element_by_xpath("//img[@alt='Details']").click()

    def count(self):
        wd = self.app.wd
        self.open_homepage()
        return len(wd.find_elements_by_name("selected[]"))

    # Возвращаем кэшированное значение (если оно доступно)
    user_cache = None

    def get_user_list(self):
        if self.user_cache is None:
            wd = self.app.wd
            self.app.open_homepage()
            self.user_cache = []
            for element in wd.find_elements_by_name("entry"):
                blocks = element.find_elements_by_tag_name("td")
                last_name = blocks[1].text
                first_name = blocks[2].text
                id = blocks[0].find_element_by_tag_name("input").get_attribute("value")
                address = blocks[3].text
                all_emails = blocks[4].text
                all_phones = blocks[5].text
                # Фамилия, Имя, id
                self.user_cache.append(User(first_name=first_name, last_name=last_name, address=address, id=id,
                                            all_phones_from_home_page=all_phones, all_emails_from_home_page=all_emails))
        # Возвращеам не сам кэш, а его копию
        return list(self.user_cache)

    # Читаем данные (фамилия, имя, телефоны) в окне редактирование пользователя.
    def get_user_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_homepage()
        # select random user
        self.select_user_by_index(index)
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        first_name = wd.find_element_by_name("firstname").get_attribute("value")
        last_name = wd.find_element_by_name("lastname").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        tel_home = wd.find_element_by_name("home").get_attribute("value")
        tel_mobile = wd.find_element_by_name("mobile").get_attribute("value")
        tel_work = wd.find_element_by_name("work").get_attribute("value")
        tel_fax = wd.find_element_by_name("fax").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email_2 = wd.find_element_by_name("email2").get_attribute("value")
        email_3 = wd.find_element_by_name("email3").get_attribute("value")
        return User(first_name=first_name, last_name=last_name, address=address, id=id,
                    tel_home=tel_home, tel_mobile=tel_mobile, tel_work=tel_work, tel_fax=tel_fax, email=email, email_2=email_2, email_3=email_3)

    def get_user_from_view_page(self, index):
        wd = self.app.wd
        self.open_user_view_by_index(index)
        text = wd.find_element_by_id("content").text
        tel_home = re.search("H: (.*)", text).group(1)
        tel_mobile = re.search("M: (.*)", text).group(1)
        tel_work = re.search("W: (.*)", text).group(1)
        tel_fax = re.search("F: (.*)", text).group(1)
        return User(tel_home=tel_home, tel_mobile=tel_mobile, tel_work=tel_work, tel_fax=tel_fax)
