from selenium import webdriver

url = 'https://www.python.org'

browser = webdriver.Chrome('C:\selenium\chromedriver')
browser.implicitly_wait(3)

browser.get(url)
browser.save_screenshot('python.png')

browser.quit