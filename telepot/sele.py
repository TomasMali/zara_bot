from bs4 import BeautifulSoup
from selenium import webdriver
import time

url = 'https://pokedex.org/'
webdriver = webdriver.Chrome()
webdriver.get(url)
time.sleep(2)

webdriver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(5)
html = BeautifulSoup(webdriver.page_source,'lxml')

uls = html.find('ul', attrs = {'id':'monsters-list'})

print(uls.prettify())