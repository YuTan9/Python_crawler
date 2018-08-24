from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome('./chromedriver') #add path of the chromedriver
browser.get("https://libportal.nus.edu.sg/frontend/index")

browser.find_element_by_id("databases-tab").click()

searchBox = browser.find_element_by_name("DBsearchString")
searchBox.clear()
searchBox.send_keys('journal citation report')
searchBox.send_keys(Keys.RETURN)
browser.find_element_by_partial_link_text('citation reports').click()

# user = browser.find_element_by_name("user")
# print(user)
# user.clear()
# user.send_keys('a0133950')
pwd = browser.find_element_by_name("frmSSO")
username = browser.find_element_by_xpath("//form[@name='frmSSO']")
pwd = browser.find_element_by_name("pass")
pwd.clear()
pwd.send_keys('') # put in password
searchBox.send_keys(Keys.RETURN)

# searchBox.send_keys(Keys.RETURN)
# assert "Python" in driver.title # confirm whether 'Python' appears in the title
# elem = driver.find_element_by_name("q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# browser.close()