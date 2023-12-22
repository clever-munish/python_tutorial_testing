
from selenium import webdriver

# Replace 'path/to/chromedriver.exe' with the actual path to your chromedriver.exe
chrome_path = r'C:\Users\Admin\Documents\Drv\chromedriver.exe'

driver = webdriver.Chrome(executable_path=chrome_path)
driver.get("https://chat.openai.com/")












