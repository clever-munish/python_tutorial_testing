import time

from selenium import webdriver

chrome_path = r'C:\Users\Admin\Documents\Drv\chromedriver.exe'
driver = webdriver.Chrome(executable_path=chrome_path)
driver.get("https://web.whatsapp.com/")
driver.maximize_window()
time.sleep(5)
# Find all elements matching the XPath
elements = driver.find_elements_by_xpath('//span[@role="button" and @tabindex="0" and @class="_3iLTh"]')

# Check if any elements are found
if elements:
    # Click on the first element in the list
    elements[0].click()
else:
    print("Element not found")
print("Before finding the element")
try:
    input_element = driver.find_element_by_xpath("//body/div[@id='app']/div[1]/div[2]/div[3]/div[1]/div[1]/div[3]/div[2]/div[1]/div[1]/div[1]/form[1]/input[1]")
    print("Element found. Continuing with the script.")
    input_element.send_keys(6985741258)
except Exception as e:
    print(f"Error: {e}")
    # Add more detailed information if needed


# driver.quit()