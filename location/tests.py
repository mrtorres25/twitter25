from django.test import TestCase

# Create your tests here.
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

class Blanktest(unittest.TestCase):
    def setUp(self):
        # binary = FirefoxBinary('C:\Program Files (x86)\Mozilla Firefox\Firefox.exe')  # ESTO HAY QUE PONERLO PARA AUTOMATIZAR LAS PRUEBAS EN TU CASA
        binary = FirefoxBinary(r'/opt/firefox/firefox')  #ESTO HAY QUE PONERLO PARA AUTOMATIZAR LAS PRUEBAS EN AMAZON
        self.driver = webdriver.Firefox(firefox_binary=binary)  # ESTO HAY QUE PONERLO PARA AUTOMATIZAR LAS PRUEBAS EN AMAZON
        self.driver.implicitly_wait(5)
        self.base_url = ip  # ESTO HAY QUE PONERLO PARA AUTOMATIZAR LAS PRUEBAS EN AMAZON
        self.verificationErrors = []  # AGNADIR ESTO SI NO ESTA
        self.accept_next_alert = True

    def test_blank(self):
        driver = self.driver
        driver.get(self.base_url + "/location/")
        driver.find_element_by_id("searchbox").clear()
        driver.find_element_by_id("searchbox").send_keys("https://twitter.com/lucacdc/status/804059526840418304")

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

class Invalidtest(unittest.TestCase):
    def setUp(self):
        # binary = FirefoxBinary('C:\Program Files (x86)\Mozilla Firefox\Firefox.exe')  # ESTO HAY QUE PONERLO PARA AUTOMATIZAR LAS PRUEBAS EN TU CASA
        binary = FirefoxBinary(r'/opt/firefox/firefox')  #ESTO HAY QUE PONERLO PARA AUTOMATIZAR LAS PRUEBAS EN AMAZON
        self.driver = webdriver.Firefox(firefox_binary=binary)  # ESTO HAY QUE PONERLO PARA AUTOMATIZAR LAS PRUEBAS EN AMAZON
        self.driver.implicitly_wait(5)
        self.base_url = ip  # ESTO HAY QUE PONERLO PARA AUTOMATIZAR LAS PRUEBAS EN AMAZON
        self.verificationErrors = []  # AGNADIR ESTO SI NO ESTA
        self.accept_next_alert = True

    def test_invalid(self):
        driver = self.driver
        driver.get(self.base_url + "/location/")
        driver.find_element_by_id("searchbox").clear()
        driver.find_element_by_id("searchbox").send_keys("64trgfjki34")
        driver.find_element_by_css_selector("button.searchbutton").click()
        self.assertRegexpMatches(driver.find_element_by_css_selector("div.container").text, r"^[\s\S]*Invalid URL or tweet ID, try again\.[\s\S]*$")

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

class Madridtest(unittest.TestCase):
    def setUp(self):
        # binary = FirefoxBinary('C:\Program Files (x86)\Mozilla Firefox\Firefox.exe')  # ESTO HAY QUE PONERLO PARA AUTOMATIZAR LAS PRUEBAS EN TU CASA
        binary = FirefoxBinary(r'/opt/firefox/firefox')  #ESTO HAY QUE PONERLO PARA AUTOMATIZAR LAS PRUEBAS EN AMAZON
        self.driver = webdriver.Firefox(firefox_binary=binary)  # ESTO HAY QUE PONERLO PARA AUTOMATIZAR LAS PRUEBAS EN AMAZON
        self.driver.implicitly_wait(5)
        self.base_url = ip  # ESTO HAY QUE PONERLO PARA AUTOMATIZAR LAS PRUEBAS EN AMAZON
        self.verificationErrors = []  # AGNADIR ESTO SI NO ESTA
        self.accept_next_alert = True

    def test_madrid(self):
        driver = self.driver
        driver.get(self.base_url + "/location/")
        driver.find_element_by_id("searchbox").clear()
        driver.find_element_by_id("searchbox").send_keys("https://twitter.com/hohahehoha/status/808337681616867328")
        driver.find_element_by_css_selector("button.searchbutton").click()
        self.assertRegexpMatches(driver.find_element_by_css_selector("div.container").text, r"^Coordenadas del tweet original: 40\.3120713,-3\.8890049[\s\S]*$")

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


class Nolocationtest(unittest.TestCase):
    def setUp(self):
        # binary = FirefoxBinary('C:\Program Files (x86)\Mozilla Firefox\Firefox.exe')  # ESTO HAY QUE PONERLO PARA AUTOMATIZAR LAS PRUEBAS EN TU CASA
        binary = FirefoxBinary(r'/opt/firefox/firefox')  #ESTO HAY QUE PONERLO PARA AUTOMATIZAR LAS PRUEBAS EN AMAZON
        self.driver = webdriver.Firefox(firefox_binary=binary)  # ESTO HAY QUE PONERLO PARA AUTOMATIZAR LAS PRUEBAS EN AMAZON
        self.driver.implicitly_wait(5)
        self.base_url = ip  # ESTO HAY QUE PONERLO PARA AUTOMATIZAR LAS PRUEBAS EN AMAZON
        self.verificationErrors = []  # AGNADIR ESTO SI NO ESTA
        self.accept_next_alert = True

    def test_nolocation(self):
        driver = self.driver
        driver.get(self.base_url + "/location/")
        driver.find_element_by_id("searchbox").clear()
        driver.find_element_by_id("searchbox").send_keys("https://twitter.com/charlie0x0/status/811714970933227521")
        driver.find_element_by_css_selector("button.searchbutton").click()
        self.assertRegexpMatches(driver.find_element_by_css_selector("div.container").text, r"^[\s\S]*Coordenadas del tweet original: No hay coordenadas disponibles\.[\s\S]*$")

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
