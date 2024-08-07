from selenium import webdriver

from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains, Keys

driver = webdriver.Chrome()
driver.get("https://www.google.com")
driver.maximize_window()
driver.find_element("xpath", '//textarea[@name="q"]').send_keys("python")
action = ActionChains(driver)
action.send_keys(Keys.ENTER).perform()
searchwebsite = "Python Programming Language"
index = 2
found = True
while found:
    try:
        driver.find_element("xpath", f"//h3[.='{searchwebsite}']").click()
        found = False

    except NoSuchElementException:
        driver.execute_script("window .scrollTo(0,document.body.scrollHeight)")
        driver.find_element("xpath", f'//a[@aria-label="Page {index}"]').click()
        index += 1
