from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
SEARCH_ENGINE = 'https://google.com'
KEYWORD = 'hello'

# option to be kept open
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),options=chrome_options)

browser.get(SEARCH_ENGINE)


search_bar = browser.find_element(By.CLASS_NAME,'gLFyf')
search_bar.send_keys(KEYWORD)
search_bar.send_keys(Keys.ENTER)

search_results = browser.find_element(By.ID,'rso').find_elements(By.CLASS_NAME,'MjjYud')
 
for index,search_result in enumerate(search_results):
    search_result.screenshot(f"screenshots/{KEYWORD}x{index}.png")
    

browser.quit()
