import time

from selenium import webdriver

chrome_path = r'C:\Users\Admin\Documents\Drv\chromedriver.exe'
driver = webdriver.Chrome(executable_path=chrome_path)
# driver.get("https://develop.ezeetel.ca/")
driver.maximize_window()
time.sleep(5)
driver.find_element_by_name('password').send_keys('321')
# driver.close()
driver.find_element_by_id('login-button').click()
time.sleep(5)
driver.get("https://develop.ezeetel.ca/extensionlist")
# driver.find_element_by_xpath("/html/body/div[2]/div[2]/section[2]/div/div/div/div[1]/div/div[1]/a").click()
time.sleep(5)
driver.get("https://develop.ezeetel.ca/extGrouplist")
time.sleep(5)
driver.refresh()
driver.get("https://develop.ezeetel.ca/contactlist")
time.sleep(8)
driver.get("https://develop.ezeetel.ca/tenant-api-key-generator/?id=1450")
time.sleep(3)
driver.forward()
# driver.back()
driver.get("https://develop.ezeetel.ca/sms-report?id=1450&t_id=1450")
time.sleep(5)
# driver.find_element_by_xpath("//span[text()='API Key']").click()
driver.get("https://develop.ezeetel.ca/logout")
# driver.find_element_by_xpath("//span[text()='Sign out']").click()
# Click the button
# for screenshot
# driver.save_screenshot("screenshot.png")
driver.close()
