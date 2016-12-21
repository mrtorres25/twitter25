# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class SearchAnUMASTweet(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://127.0.0.1:8080/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_search_an_u_m_a_s_tweet(self):
        driver = self.driver
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        driver.find_element_by_name("username").clear()
        driver.find_element_by_name("username").send_keys("root")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("root")
        driver.find_element_by_xpath("//button[@type='submit']").click()
        driver.find_element_by_id("toInfo").click()
        driver.find_element_by_css_selector("div.container > button.btn").click()
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "img[alt=\"Un ejemplo de URL\"]"))
        self.assertEqual("Esto es un ejemplo de como obtener la URL de un tweet.", driver.find_element_by_css_selector("h3").text)
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "div.alert.alert-info"))
        self.assertEqual("Introduzca la URL del Tweet", driver.find_element_by_css_selector("div.alert.alert-info").text)
        driver.find_element_by_id("searchbox").clear()
        driver.find_element_by_id("searchbox").send_keys("https://twitter.com/InfoUMA/status/807170636091105280?lang=es")
        driver.find_element_by_css_selector("#searchform > button.btn").click()
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "div.alert.alert-success"))
        driver.find_element_by_xpath("(//button[@type='button'])[3]").click()
        driver.find_element_by_xpath("(//button[@type='button'])[3]").click()
        self.assertRegexpMatches(driver.find_element_by_css_selector("div.alert.alert-success").text, "^exact:Se ha realizado correctamente su busqueda del tweet con url: \"https://twitter\\.com/InfoUMA/status/807170636091105280[\\s\\S]lang=es\"$")
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
