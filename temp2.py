from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException

browser = webdriver.Chrome('./chromedriver') #add path of the chromedriver
browser.get("https://proxylogin.nus.edu.sg/libproxy1/public/login.asp?logup=false&url=https://jcr.incites.thomsonreuters.com")
pwd = browser.find_element_by_name("frmSSO")
user = browser.find_element_by_name("user")
user.clear()
user.send_keys('a0133950')
# pwd = browser.find_element_by_name("pass")
# username = browser.find_element_by_xpath("//form[@name='frmSSO']")
pwd = browser.find_element_by_name("pass")
pwd.clear()
pwd.send_keys('365ZYLwlp!!!')
clear_button = browser.find_elements_by_xpath("//input[@type='submit']")
for button in clear_button:
	if button.get_attribute('value') == 'Login':
		login = button

if login is not None:
	login.click()
	browser.find_element_by_xpath("//input[@type='submit']").click()
	# browser.find_element_by_partial_link_text('Select Journals').click()

	# test with search and get result first (only one result)
	search = browser.find_element_by_id("search-inputEl")
	search.clear()
	search.send_keys("COMPUT HUM BEHAV")
	time.sleep(3)
	i = browser.find_element_by_xpath("//input[@type='submit']")
	print(i)
	print(i.get_attribute('onclick'))
	i.click()
	time.sleep(30)




# browser.close()
	