from pageObjects.LoginPage import LoginPage


class Test_001_Login:
    baseUrl = "https://admin-demo.nopcommerce.com/"
    username = "admin@yourstore.com"
    password = "admin"

    def test_homePageTitle(self, setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        act_title = self.driver.title
        self.driver.close()
        if act_title == "Your store. Login":
            assert True
        else:
            self.driver.save_screenshot(".\\screenshots\\"+"test_homePageTitle.png")
            self.driver()
            assert False

    def test_login(self, setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = \
            LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        self.driver.close()
        if act_title == "Dashboard / nopCommerce administration":
            assert True
        else:
            self.driver.save_screenshot(".\\screenshots\\" + "test_Login.png")
            self.driver()
            assert False
