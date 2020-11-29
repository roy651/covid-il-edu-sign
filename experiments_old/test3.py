import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options  

chrome_options = Options()  
#chrome_options.add_argument("--headless")  
chrome_options.binary_location = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'

driver = webdriver.Chrome('/Users/royabitbol/Development/private/schooly/chromedriver')  # Optional argument, if not specified will search path.
driver.get('http://www.google.com/');
time.sleep(5) # Let the user actually see something!
search_box = driver.find_element_by_name('q')
search_box.send_keys('ChromeDriver')
search_box.submit()
time.sleep(5) # Let the user actually see something!
driver.quit()