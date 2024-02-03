from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

SEARCH_ENGINE = 'https://google.com'
KEYWORD = 'fmdskal'

browser.get(SEARCH_ENGINE)


search_bar = browser.find_element(By.CLASS_NAME,'gLFyf')
search_bar.send_keys(KEYWORD)
search_bar.send_keys(Keys.ENTER)

print(search_bar)
browser.quit()