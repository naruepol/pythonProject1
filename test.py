import time
from selenium import webdriver

driver = webdriver.Chrome(executable_path = "/Users/naruaponsuwanwijit/Desktop/chromedriver")
# driver = webdriver.Chrome('/Users/naruaponsuwanwijit/Desktop/chromedriver')


driver.get("http://www.google.com/")
time.sleep(2)
driver.close()