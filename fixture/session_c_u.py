class SessionHelperCreateUser:
    def __init__(self, app_c_u):
        self.app_c_u = app_c_u #application_create_user

    def login(self, username, password):
        wd = self.app_c_u.wd
        self.app_c_u.open_home_page()
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def logout(self):
        wd = self.app_c_u.wd
        wd.find_element_by_link_text("Logout").click()