from selenium import webdriver
from fixture.session_c_u import SessionHelperCreateUser
from fixture.user import UserHelper


class Application_create_user:
    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
        self.session = SessionHelperCreateUser(self)
        self.user = UserHelper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def destroy(self):
        self.wd.quit()
