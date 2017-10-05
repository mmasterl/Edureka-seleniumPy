import unittest

from selenium import webdriver

from selenium.webdriver.common.keys import Keys

# test class
class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox(executable_path="/Users/markomasterl/Downloads/webdrivers/firefox/geckodriver")

    # test case method
    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://www.python.org")
        self.assertIn("Python", driver.title)
        elem = driver.find_element_by_name("q")
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        assert "No result found" not in driver.page_source
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()


#
# # find_element_by_xpath
#
# <html>
#   <body>
#       <form id="loginForm">
#           <input name="username" type="text" />
#           <input name="password" type="password" />
#           <input name="continue" type="submit" value="Login" />
#       </form>
#   </body>
# <html>
#
# login_form = driver.find_element_by_xpath("//form[@id='loginForm']")
#

#
# # find_element_by_link_text
#
# <html>
#   <body>
#       <p>Are you sure you want to do this?</p>
#       <a href="continue.html">Continue<a/>
#       <a href="cancel.html">Cancel<a/>
#   </body>
# <html>
#
# continue_link = driver.find_element_by_link('Continue')
#

#
# # find_element_by_tag_name
#
# <html>
#   <body>
#       <h1>Welcome</h1>
#       <p>Site content goes here.<p/>
#   </body>
# <html>
#
# heading1 = driver.find_element_by_tag_name('h1')
#

#
# # find_element_by_class_name
#
# <html>
#   <body>
#       <p class="content">Site content goes here.</p>
#   </body>
# <html>
#
# content = driver.find_element_by_class_name('content')
#

