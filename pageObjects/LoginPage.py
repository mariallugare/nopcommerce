
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class LoginPage:
    textbox_username_id = "Email"
    textbox_password_id = "Password"

    button_login_xpath = "//input[@class='button-1 login-button']"
    link_logout_linktext = "Logout"

    def __init__(self, driver):
        self.driver = driver
        self.textbox_username_id = "Email"  # Replace with the actual ID
        self.textbox_password_id = "Password"  # Replace with the actual ID

    def setUserName(self, username):
        username_element = self.driver.find_element(By.ID, self.textbox_username_id)
        username_element.clear()
        username_element.send_keys(username)

    def setPassword(self, password):
        password_element = self.driver.find_element(By.ID, self.textbox_password_id)
        password_element.clear()
        password_element.send_keys(password)

    def clickLogin(self):
        try:
            print("Current URL:", self.driver.current_url)
            print("Page Source:", self.driver.page_source)

            login_button = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, self.button_login_xpath))
            )
            login_button.click()

        except TimeoutException as e:
            print(f"TimeoutException: Unable to find element with XPath: {self.button_login_xpath}")
            raise  # Reraise the exception to mark the test as failed

    def clickLogout(self):
        logout_link = self.driver.find_element(By.LINK_TEXT, self.link_logout_linktext)
        logout_link.click()



