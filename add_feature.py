from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
#hi bor
driver = webdriver.Chrome()
movie_name = "Ready player one"
url = "https://moviesverse.org.in/"
driver.get(url)

search_button = driver.find_element_by_xpath('//*[@id="s"]').click()

driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[1])
driver.get(url)
search_button = driver.find_element_by_id('s').click()
time.sleep(30)
search_button.send_keys(movie_name)


