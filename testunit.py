import unittest
import HtmlTestRunner
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
chromedriver="chromedriver"
#python -m unittest testunit.py
class testcalc(unittest.TestCase):
    def test_admin_login(self):
        self.driver=webdriver.Chrome(chromedriver)
        self.driver.get('http://localhost/E-Commerce-Website-Using-PHP/admin/login.php')
        self.driver.find_element_by_xpath('//*[@id="content"]/form/div[1]/input').send_keys('admin')
        self.driver.find_element_by_xpath('//*[@id="content"]/form/div[2]/input').send_keys('123')
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="content"]/form/div[2]/input').send_keys(Keys.ENTER)
        sleep(1)
        self.driver.close()
        
    def test_user_login(self):
        """ Login sukses dengan id yang sudah terdaftar"""
        self.driver=webdriver.Chrome(chromedriver)
        self.driver.get("http://localhost/E-Commerce-Website-Using-PHP/")
        self.driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div[3]/a').click()
        self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[1]/form/input[1]').send_keys('ariefchaerudin@gmail.com')
        self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[1]/form/input[2]').send_keys('12345678')
        self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[1]/form/div/div/button').click()
        self.driver.close()
      
    def test_register(self):
        """ Register dengan akun yang belum terdaftar """
        self.driver=webdriver.Chrome(chromedriver)
        self.driver.get("http://localhost/E-Commerce-Website-Using-PHP/login.php")
        self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[2]/form/table/tbody/tr/td[1]/div[1]/input').send_keys('Elon Chan')
        self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[2]/form/table/tbody/tr/td[1]/div[2]/input').send_keys('Jl.Telekomunikasi')
        self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[2]/form/table/tbody/tr/td[1]/div[3]/input').send_keys('Bandung')
        self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[2]/form/table/tbody/tr/td[1]/div[4]/input').send_keys('13950')
        self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[2]/form/table/tbody/tr/td[2]/div[1]/input').send_keys('elonchan@gmail.com')
        self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[2]/form/table/tbody/tr/td[2]/div[2]/input').send_keys('Indonesia')
        self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[2]/form/table/tbody/tr/td[2]/div[3]/input').send_keys('0213513632')
        self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[2]/form/table/tbody/tr/td[2]/div[4]/input').send_keys('12345678')
        self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[2]/form/div[1]/div/button').click()
        self.driver.close()
        
    def test_add_cart(self):
        self.driver=webdriver.Chrome(chromedriver)
        self.driver.get("http://localhost/E-Commerce-Website-Using-PHP/")
        self.driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div[3]/a').click()
        self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[1]/form/input[1]').send_keys('ariefchaerudin@gmail.com')
        self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[1]/form/input[2]').send_keys('12345678')
        self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[1]/form/input[2]').send_keys(Keys.ENTER)
        self.driver.get('http://localhost/E-Commerce-Website-Using-PHP/index.php')        
        self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div[1]/div[2]/div[2]/div/span/a').click()
        self.driver.find_element_by_xpath('/html/body/div/div[3]/div/div/div/div[2]/div[2]/form/input[2]').click()
        self.driver.close()
        
    def test_checkout(self):
        self.driver=webdriver.Chrome(chromedriver)
        self.driver.get("http://localhost/E-Commerce-Website-Using-PHP/")
        self.driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div[3]/a').click()
        self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[1]/form/input[1]').send_keys('ariefchaerudin@gmail.com')
        self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[1]/form/input[2]').send_keys('12345678')
        self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[1]/form/div/div/button').click()
        self.driver.get('http://localhost/E-Commerce-Website-Using-PHP/index.php')        
        self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div[1]/div[2]/div[2]/div/span/a').click()
        self.driver.find_element_by_xpath('/html/body/div/div[3]/div/div/div/div[2]/div[2]/form/input[2]').click()
        self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[1]/div[2]/div[2]/a/img').click()
        self.driver.find_element_by_xpath('/html/body/div/div[3]/div/div/div[1]/a').click()
        self.driver.find_element_by_xpath('/html/body/div/div[3]/div/div[2]/a').click()
        self.driver.find_element_by_xpath('/html/body/div/div[3]/div/div/div/p/a').click()
        self.driver.close()
    
    def test_add_category(self):
        self.driver=webdriver.Chrome(chromedriver)
        self.driver.get('http://localhost/E-Commerce-Website-Using-PHP/admin/login.php')
        self.driver.find_element_by_xpath('//*[@id="content"]/form/div[1]/input').send_keys('admin')
        self.driver.find_element_by_xpath('//*[@id="content"]/form/div[2]/input').send_keys('123')
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="content"]/form/div[2]/input').send_keys(Keys.ENTER)
        sleep(5)
        self.driver.find_element_by_xpath('//*[@id="section-menu"]/ul/li[1]/ul/li[1]/a').click()
        self.driver.find_element_by_xpath('/html/body/div[1]/div[6]/div/div/form/table/tbody/tr[1]/td/input').send_keys('Furnitur')
        self.driver.find_element_by_xpath('/html/body/div[1]/div[6]/div/div/form/table/tbody/tr[2]/td/input').click()
        self.driver.close()

    def test_add_barang(self):
        self.driver=webdriver.Chrome(chromedriver)
        self.driver.get('http://localhost/E-Commerce-Website-Using-PHP/admin/login.php')
        self.driver.find_element_by_xpath('//*[@id="content"]/form/div[1]/input').send_keys('admin')
        self.driver.find_element_by_xpath('//*[@id="content"]/form/div[2]/input').send_keys('123')
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="content"]/form/div[2]/input').send_keys(Keys.ENTER)
        sleep(5)
        self.driver.get('http://localhost/E-Commerce-Website-Using-PHP/admin/productadd.php')
        self.driver.find_element_by_xpath('/html/body/div[1]/div[6]/div/div/form/table/tbody/tr[1]/td[2]/input').send_keys('gelas')
        self.driver.find_element_by_xpath('/html/body/div[1]/div[6]/div/div/form/table/tbody/tr[2]/td[2]/select/option[6]').click()
        self.driver.find_element_by_xpath('/html/body/div[1]/div[6]/div/div/form/table/tbody/tr[3]/td[2]/select/option[4]').click()
        self.driver.find_element_by_xpath('/html/body/div[1]/div[6]/div/div/form/table/tbody/tr[4]/td[2]/textarea').send_keys('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris purus odio, venenatis ut enim eu, varius viverra tortor. Vestibulum aliquam metus libero, at luctus diam dignissim vitae.')
        self.driver.find_element_by_xpath('/html/body/div[1]/div[6]/div/div/form/table/tbody/tr[5]/td[2]/input').send_keys('100')
        self.driver.find_element_by_xpath('/html/body/div[1]/div[6]/div/div/form/table/tbody/tr[6]/td[2]/input').send_keys('C://Users/Felixyu/Pictures/doge.jpg')
        self.driver.find_element_by_xpath('/html/body/div[1]/div[6]/div/div/form/table/tbody/tr[7]/td[2]/select/option[2]').click()
        self.driver.find_element_by_xpath('/html/body/div[1]/div[6]/div/div/form/table/tbody/tr[8]/td[2]/input').click()
        self.driver.close()
        
        
        
        
        
if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='example_dir'))