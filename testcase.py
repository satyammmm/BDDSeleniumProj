from behave import *
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

@given(u'launch browser')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.implicitly_wait(20)


@when(u'get amazon url')
def step_impl(context):
    context.driver.get("https://www.amazon.in")
    time.sleep(4)


@then(u'page should appear')
def step_impl(context):
    assert context.driver.find_element(By.XPATH,"//a[@class='nav-logo-link nav-progressive-attribute']").is_displayed()
    context.driver.quit()

@given(u'assert flag from scenario 1')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.implicitly_wait(20)
    context.driver.get("https://www.amazon.in")

@when(u'click on search icon and search for non existing product')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//input[@type='text']").send_keys("id4567")
    context.driver.find_element(By.XPATH, "//input[@type='submit']").click()

@then(u'No result found should be displayed')
def step_impl(context):
    assert context.driver.find_element(By.XPATH, "//span[@class='a-size-medium a-color-base' and contains(text(),'No results for ')]").is_displayed()
    context.driver.quit()

@given(u'assert flag from scenario 2')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.implicitly_wait(20)
    context.driver.get("https://www.amazon.in")

@when(u'click on search icon and search for existing product')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//a[@class='nav-logo-link nav-progressive-attribute']").is_displayed()
    context.driver.find_element(By.XPATH, "//input[@type='text']").send_keys("laptop")
    context.driver.find_element(By.XPATH, "//input[@type='submit']").click()
    products = []
    for i in range(5):
        print("Fetching Result", i + 1)
        product = context.driver.find_elements(By.XPATH, "//span[@class='a-size-medium a-color-base a-text-normal']")
        for p in product:
            products.append(p.text)
    print(products[:5])
    print("\n")

@then(u'result should be displayed')
def step_impl(context):
    assert context.driver.find_element(By.XPATH,"//h2[@class='a-size-medium-plus a-spacing-none a-color-base a-text-bold' and text()='Results']").is_displayed()
    context.driver.quit()

@given(u'assert flag from scenario 3')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.implicitly_wait(20)
    context.driver.get("https://www.amazon.in")

@when(u'select first result from search result')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//a[@class='nav-logo-link nav-progressive-attribute']").is_displayed()
    context.driver.find_element(By.XPATH, "//input[@type='text']").send_keys("laptop")
    context.driver.find_element(By.XPATH, "//input[@type='submit']").click()
    context.driver.find_element(By.XPATH, "//button[@class='a-button-text' and @id='a-autoid-3-announce' and text()='Add to cart']").click()
    context.driver.find_element(By.XPATH, "//div[@class='ewc-compact sc-java-remote-feature celwidget']")
    context.driver.find_element(By.XPATH, "//span[@class='a-button-text a-declarative']//span[text()='1']").click()
    context.driver.find_element(By.XPATH, "//span[@data-action='update-quantity']//input[@data-action='update-quantity' and @value='2']").click()

@then(u'selected product should be added to cart')
def step_impl(context):
    assert context.driver.find_element(By.XPATH, "//span[@class='a-dropdown-prompt' and text()='2']").is_displayed()
    context.driver.quit()

@given(u'assert flag from scenario 4')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.implicitly_wait(20)
    context.driver.get("https://www.amazon.in")

@when(u'remove product form the cart')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//a[@class='nav-logo-link nav-progressive-attribute']").is_displayed()
    context.driver.find_element(By.XPATH, "//input[@type='text']").send_keys("laptop")
    context.driver.find_element(By.XPATH, "//input[@type='submit']").click()
    context.driver.find_element(By.XPATH, "//button[@class='a-button-text' and @id='a-autoid-3-announce' and text()='Add to cart']").click()
    context.driver.find_element(By.XPATH, "//div[@class='ewc-compact sc-java-remote-feature celwidget']")
    context.driver.find_element(By.XPATH, "//span[@class='a-button-text a-declarative']//span[text()='1']").click()
    context.driver.find_element(By.XPATH, "//span[@data-action='update-quantity']//input[@data-action='update-quantity' and @value='2']").click()
    context.driver.find_element(By.XPATH, "//span[@class='a-button a-button-span11 a-button-base a-button-small']/span[@class='a-button-inner']").click()
    context.driver.find_element(By.XPATH,"//input[@value='Delete' and @data-action='delete']").click()

@then(u'cart should be empty')
def step_impl(context):
    assert context.driver.find_element(By.XPATH, "//h2[contains(text(),'is empty')]").is_displayed()
    context.driver.quit()