import pytest
from selenium import webdriver
class TestRitesh():
        @pytest.fixture()
        def setup(self):
                self.driver=webdriver.Chrome(executable_path="D://PYTHON//chromedriver.exe")
                self.driver.maximize_window()
                yield
                self.driver.quit()

        def test_homePage(self,setup):
                self.driver.get("http://facebook.com")
                self.driver.find_element_by_id("email").send_keys("riteshranjanmishra938@gmail.com")
                self.driver.find_element_by_id("pass").send_keys("mishra21")
                self.driver.find_element_by_xpath("//*[@value='Log In']").click()
                print(self.driver.title)
                assert self.driver.title=="Facebook"









