# # Test Case
# # ------------------------------------------------
# # 1)open Web browser (Chrome,Firefox,Edge)
# # 2)open url https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
# # 3)Enter username (Admin)
# # 4)Enter password (admin123)
# # 5)click on Login
# # 6)Capture title of the home page (Actual title)
# # 7)Verify title of the page : OrangeHRM (Expected)
# # 8)Close browser
#
# # from selenium import webdriver
# #
# # driver=webdriver.Chrome()
# # driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
#
# # from selenium import webdriver
# #
# # chrome_driver_path = "path/to/chromedriver.exe"
# # driver = webdriver.Chrome(executable_path="D:\\Selenium project\\chromedriver-win64\\chromedriver-win64")
# # driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
#
#
#
# # from selenium import webdriver
# #
# # chrome_driver_path = "D:\\Selenium project\\chromedriver-win64\\chromedriver-win64"
# # driver = webdriver.Chrome(service_args=[f'--webdriver-path={"D:\\Selenium project\\chromedriver-win64\\chromedriver-win64"}'])
#
# #
# # from selenium import webdriver
# #
# # chrome_driver_path = "D:\\Selenium project\\chromedriver-win64\\chromedriver.exe"
# # driver = webdriver.Chrome(executable_path="D:\\Selenium project\\chromedriver-win64\\chromedriver.exe")
# # driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
#
# # from selenium import webdriver
# #
# # chrome_driver_path = "D:\\Selenium project\\chromedriver-win64\\chromedriver.exe"
# # chrome_options = webdriver.ChromeOptions()
# # chrome_options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"  # Adjust the path if necessary
# #
# # driver = webdriver.__init__(executable_path=chrome_driver_path, options=chrome_options)
# # driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
#
#
# # from selenium import webdriver
# #
# # chrome_driver_path = "D:\\Selenium project\\chromedriver-win64\\chromedriver.exe"
# # chrome_options = webdriver.ChromeOptions()
# # chrome_options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"  # Adjust the path if necessary
# #
# # driver = webdriver.Chrome=chrome_driver_path, options=chrome_options
# # driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
#
#
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
#
# chrome_driver_path = "D:\\Selenium project\\chromedriver-win64\\chromedriver.exe" # Update with your actual path
# chrome_options = Options()
# # Add any desired options to chrome_options
#
# # Corrected line: Use parentheses () instead of equal sign =
# driver = webdriver.Chrome(chrome_driver_path, options=chrome_options)
#
#
# from selenium import webdriver
#
# driver=webdriver.Chrome()
# url='https://stackoverflow.com/questions/59415623/selenium-webdriver-missing-1-required-positional-argument-self'
# driver.get(url)

#
# from selenium import webdriver
#
# D:\Python Projects\python_tutorial\myenv\Lib\site-packages\selenium\webdriver\common\windows


#
# from selenium import webdriver
#
# # Get the version of the installed WebDriver
# webdriver_version = webdriver.__version__
#
# print("Selenium WebDriver version:", webdriver_version)


# from selenium import webdriver
#
# # Instantiate a Chrome browser
# browser = webdriver.Chrome()
#
# # Get the version of the ChromeDriver
# chrome_version = browser.capabilities['chrome']['chromedriverVersion']
#
# print("ChromeDriver version:", chrome_version)
#
# # Close the browser
# browser.quit()

#
# from selenium import webdriver
#
# # Use double backslashes or a raw string for Windows path
#
#
# # Instantiate a Chrome browser with the specified executable path
# browser = webdriver.Chrome("C:\\Users\\Admin\\PycharmProjects\\pythonTutorials\\venv\\Lib\\site-packages\\selenium\\webdriver\\common\\windows")
#


# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
#
# option = webdriver.ChromeOptions()
# driver = webdriver.Chrome(options = option)
#
# driver.get('https://www.google.com/')