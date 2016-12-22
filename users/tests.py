from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import unittest, time, re
import socket

ip = "http://127.0.0.1:8080/"

class CorrectLogin(unittest.TestCase):
    def setUp(self):
        # binary = FirefoxBinary('C:\Program Files (x86)\Mozilla Firefox\Firefox.exe')  # ESTO HAY QUE PONERLO PARA AUTOMATIZAR LAS PRUEBAS EN TU CASA
        binary = FirefoxBinary(r'/opt/firefox/firefox')  #ESTO HAY QUE PONERLO PARA AUTOMATIZAR LAS PRUEBAS EN AMAZON
        self.driver = webdriver.Firefox(firefox_binary=binary)  # ESTO HAY QUE PONERLO PARA AUTOMATIZAR LAS PRUEBAS EN AMAZON
        self.driver.implicitly_wait(5)
        self.base_url = ip  # ESTO HAY QUE PONERLO PARA AUTOMATIZAR LAS PRUEBAS EN AMAZON
        self.verificationErrors = []  # AGNADIR ESTO SI NO ESTA
        self.accept_next_alert = True
    
    def test_correct_login(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_name("username").clear()
        driver.find_element_by_name("username").send_keys("root")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("root")
        driver.find_element_by_xpath("//button[@type='submit']").click()
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "div.alert.alert-success"))
        driver.find_element_by_link_text("Salir").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()



class WrongLogin(unittest.TestCase):
    def setUp(self):
        # binary = FirefoxBinary('C:\Program Files (x86)\Mozilla Firefox\Firefox.exe')  # ESTO HAY QUE PONERLO PARA AUTOMATIZAR LAS PRUEBAS EN TU CASA
        binary = FirefoxBinary(r'/opt/firefox/firefox')  #ESTO HAY QUE PONERLO PARA AUTOMATIZAR LAS PRUEBAS EN AMAZON
        self.driver = webdriver.Firefox(firefox_binary=binary)  # ESTO HAY QUE PONERLO PARA AUTOMATIZAR LAS PRUEBAS EN AMAZON
        self.driver.implicitly_wait(5)
        self.base_url = ip  # ESTO HAY QUE PONERLO PARA AUTOMATIZAR LAS PRUEBAS EN AMAZON
        self.verificationErrors = []  # AGNADIR ESTO SI NO ESTA
        self.accept_next_alert = True
    
    def test_wrong_login(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_name("username").clear()
        driver.find_element_by_name("username").send_keys("samuel")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("samuel")
        driver.find_element_by_xpath("//button[@type='submit']").click()
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "div.alert.alert-danger"))
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()



class Logout(unittest.TestCase):
    def setUp(self):
        # binary = FirefoxBinary('C:\Program Files (x86)\Mozilla Firefox\Firefox.exe')  # ESTO HAY QUE PONERLO PARA AUTOMATIZAR LAS PRUEBAS EN TU CASA
        binary = FirefoxBinary(r'/opt/firefox/firefox')  #ESTO HAY QUE PONERLO PARA AUTOMATIZAR LAS PRUEBAS EN AMAZON
        self.driver = webdriver.Firefox(firefox_binary=binary)  # ESTO HAY QUE PONERLO PARA AUTOMATIZAR LAS PRUEBAS EN AMAZON
        self.driver.implicitly_wait(5)
        self.base_url = ip  # ESTO HAY QUE PONERLO PARA AUTOMATIZAR LAS PRUEBAS EN AMAZON
        self.verificationErrors = []  # AGNADIR ESTO SI NO ESTA
        self.accept_next_alert = True
    
    def test_logout(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_name("username").clear()
        driver.find_element_by_name("username").send_keys("root")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("root")
        driver.find_element_by_xpath("//button[@type='submit']").click()
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "div.alert.alert-success"))
        driver.find_element_by_link_text("Salir").click()
        self.assertEqual("Login", driver.title)
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
