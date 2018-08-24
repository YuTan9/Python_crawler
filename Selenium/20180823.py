from selenium import selenium
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup

browser = webdriver.Firefox()
browser.get('https://shopee.tw/shopee24h')
browser.close()