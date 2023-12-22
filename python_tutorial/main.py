from selenium import webdriver

chrome_path = r'C:\Users\Admin\Documents\Drv\chromedriver.exe'
driver = webdriver.Chrome(executable_path=chrome_path)
driver.get("https://develop.ezeetel.ca/")
driver.maximize_window()
driver.find_element_by_id("email").send_keys('munish@ezeetel.ca')
driver.find_element_by_name('password').send_keys('123')
# driver.close()
driver.find_element_by_id('login-button').click()
# driver.find_element_by_xpath("//span[text()='API Key']").click()
driver.find_element_by_xpath("//span[text()='Sign out']").click()
driver.find_element_by_xpath('"//a[contains(@class, 'btn') and contains(@class, 'primary') and contains(@class, 'sm') and contains(@class, 'px-4') and contains(@class, 'rounded')]"')
