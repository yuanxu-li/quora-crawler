from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import getpass
import time
import pdb

class Driver(webdriver.PhantomJS):
    def __init__(self):
        super(Driver, self).__init__()
        website = input("Login Website: ")
        self.set_window_size()
        self.get(website)
        self.log_in()

    def set_window_size(self):
        super(Driver, self).set_window_size(2400, 1200)

    def log_in(self):
        email = input("Email: ")
        passwd = getpass.getpass("Password: ")
        self.find_elements_by_name("email")[1].clear()
        self.find_elements_by_name("email")[1].send_keys(email)
        self.find_elements_by_name("password")[1].clear()
        self.find_elements_by_name("password")[1].send_keys(passwd)
        if self.find_elements_by_name("email")[1].get_attribute("value") != email:
            raise Exception("Email input not received correctly!")
        if self.find_elements_by_name("password")[1].get_attribute("value") != passwd:
            raise Exception("Password input not received correctly!")

        
        time.sleep(5)
        self.find_element_by_css_selector("input[type='submit'][value='Login']").click()
        time.sleep(5)

        # pdb.set_trace()

        if "Top Stories For You" not in self.page_source:
            raise Exception("Login failed!")

    # scroll down the driver of a browser to render the whole page, in case
    # the page is rendered by javascript
    def scroll_down(self, times):
        body = self.find_element_by_tag_name("body")
        while times > 0:
            body.send_keys(Keys.PAGE_DOWN)
            times -= 1

    def __del__(self):
        self.quit()