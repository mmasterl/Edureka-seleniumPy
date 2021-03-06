from selenium import webdriver

from selenium.webdriver.common.keys import Keys

#driver = webdriver.Firefox(executable_path="/Users/markomasterl/Library/Selenium/WebDriver/firefox/geckodriver")
driver = webdriver.Chrome(executable_path="/Users/markomasterl/Library/Selenium/WebDriver/chrome/chromedriver")

driver.get("http://www.python.org")

assert "Python" in driver.title

elem = driver.find_element_by_name("q")

elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)

assert "No result found" not in driver.page_source

# driver.quit()
