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

    def modify_first_user(self, user):
        wd = self.app.wd
        self.open_homepage()
        # select first user
        wd.find_element_by_name("selected[]").click()
        # click button 'Edit"
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        # fill user form
        self.method_filling_user_form(user)
        # click button 'update" - modify user
        wd.find_element_by_name("update").click()

    def delete_first_user(self):
        wd = self.app.wd
        self.open_homepage()
        # select first user
        wd.find_element_by_name("selected[]").click()
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()

    # Заполнение формы Пользователя (User)
    def method_filling_user_form(self, user):
        wd = self.app.wd
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(user.first_name)
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(user.middle_name)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(user.nick_name)
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(user.title)
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(user.company)
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
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(user.email)
        wd.find_element_by_name("bday").click()
        wd.find_element_by_xpath("//option[@value='22']").click()
        wd.find_element_by_name("bmonth").click()
        wd.find_element_by_xpath("//option[@value='August']").click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(user.b_year)
        wd.find_element_by_name("aday").click()
        wd.find_element_by_xpath("//div[@id='content']/form/select[3]/option[12]").click()
        wd.find_element_by_name("amonth").click()
        wd.find_element_by_xpath("//div[@id='content']/form/select[4]/option[9]").click()
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys(user.anniversary_year)

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

    def count(self):
        wd = self.app.wd
        self.open_homepage()
        return len(wd.find_elements_by_name("selected[]"))
