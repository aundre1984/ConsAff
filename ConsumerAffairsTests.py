import unittest
from time import sleep

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

class HomePageTest(unittest.TestCase):
    @classmethod
    def setUp(inst):
        # creates a new chrome session """
        inst.driver = webdriver.Chrome()
        inst.driver.implicitly_wait(30)
        inst.driver.maximize_window()

        # navigates to the application home page """
        inst.driver.get("https://www.consumeraffairs.com/recalls/liberty-mountain-recalls-birdie-belay-devices-032921.html")


    def test_verify_disclaimer(self):
        browser = self.driver
        elem = browser.find_element_by_class_name('js-discl')
        assert 'ConsumerAffairs is not a government agency and may be compensated by companies displayed.' in elem.get_attribute('innerHTML')

    def test_verify_footer_pt1(self):
        browser = self.driver
        elem = browser.find_element_by_class_name('ca-ft__ctnt')
        assert 'ConsumerAffairs is not a government agency. Companies displayed may pay us to be Authorized or when you click a link, call a number or fill a form on our site. Our content is intended to be used for general information purposes only. It is very important to do your own analysis before making any investment based on your own personal circumstances and consult with your own investment, financial, tax and legal advisers.' in elem.get_attribute('innerHTML')

    def test_verify_footer_pt2(self):
        browser = self.driver
        elem = browser.find_element_by_class_name('ca-ft__ctnt')
        assert 'Consumers Unified LLC. All Rights Reserved. The contents of this site may not be republished, reprinted, rewritten or recirculated without written permission.' in elem.get_attribute('innerHTML')

    def test_facebook_link(self):
        browser = self.driver

        facebook_elem = browser.find_element_by_css_selector('#wrpr > div.h-sect.h-cont.h-col.h-col--invert > article > div:nth-child(6) > a:nth-child(1) > svg > g > path.ca-icon__colored-fill')
        facebook_elem.click();
        
        sleep(5)
        
        parent_handle = browser.current_window_handle
        for handle in browser.window_handles:
            if handle != parent_handle:
                browser.switch_to.window(handle)
                assert 'Facebook' in browser.title


    def test_twitter_link(self):
        browser = self.driver

        twitter_elem = browser.find_element_by_css_selector('#wrpr > div.h-sect.h-cont.h-col.h-col--invert > article > div:nth-child(6) > a:nth-child(2) > svg > g > path.ca-icon__colored-fill')
        twitter_elem.click();
        
        sleep(5)
        
        parent_handle = browser.current_window_handle
        for handle in browser.window_handles:
            if handle != parent_handle:
                browser.switch_to.window(handle)
                assert 'Twitter' in browser.title


    def test_find_my_match(self):
        browser = self.driver
        elem_txt = browser.find_element_by_css_selector('.ca-mt-zip__input')
        elem_btn = browser.find_element_by_css_selector('.ca-mt-zip__btn')
        elem_txt.send_keys("77001")
        sleep(5)
        elem_btn.click()
        
        parent_handle = browser.current_window_handle
        for handle in browser.window_handles:
            if handle != parent_handle:
                browser.switch_to.window(handle)
                assert 'Get Matched With Your Best Home Warranty Today!' in browser.title
        
        
    @classmethod
    def tearDown(inst):
        # close the browser window
        inst.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)