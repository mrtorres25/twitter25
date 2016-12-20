# -*- coding: utf-8 -*-
from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class TestSearchEnglish(unittest.TestCase):
    def setUp(self):
        binary = FirefoxBinary(r'/opt/firefox/firefox')
        self.driver = webdriver.Firefox(firefox_binary=binary)
        self.driver.implicitly_wait(30)
        self.base_url = "http://127.0.0.1:8080/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_search_english(self):
        driver = self.driver
        driver.get(self.base_url + "")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("root")
        driver.find_element_by_name("username").clear()
        driver.find_element_by_name("username").send_keys("root")
        driver.find_element_by_xpath("//button[@type='submit']").click()
        driver.find_element_by_id("toSearch").send_keys(Keys.ENTER)
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "div.alert.alert-info"))
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        driver.find_element_by_id("searchbox").clear()
        driver.find_element_by_id("searchbox").send_keys("Renfe")
        Select(driver.find_element_by_name("languageCode")).select_by_visible_text("English : English")
        driver.find_element_by_css_selector("button.btn").click()
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
