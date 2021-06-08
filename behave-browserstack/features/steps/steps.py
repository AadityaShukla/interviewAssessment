from behave import given, when, then
from selenium.webdriver.common.by import By

@given('user opens the store page "{url}"')
def step(context, url):
    context.browser.get(url)

@given('user adds an item to the cart')
def step(context):
    #all_items = context.browser.find_elements_by_xpath("//div[@class='card card-body']")
    #item_text = [item.text for item in all_items]
    #print(item_text)
    context.price_dict={}
    count=1
    for row in context.table:
        row['name']
        context.item_name = row['name']
        item_name = row['name']
        #adding item to cart
        context.browser.find_element(By.XPATH, "//div[@class='card card-body']/p[contains(text(),'" +item_name+ "')]//following-sibling::div[@class='text-right']/button[text()='Add to cart']").click()
        context.item_price_homepage = context.browser.find_element(By.XPATH,"//div[@class='card card-body']/p[contains(text(),'" +item_name+ "')]/following-sibling::h3").text
        context.price_dict[count]=[item_name, context.browser.find_element(By.XPATH,"//div[@class='card card-body']/p[contains(text(),'" +item_name+ "')]/following-sibling::h3").text.strip('$'),1]
        count = count +1

@when('user goes to cart')
def step(context):
    context.browser.find_element(By.XPATH, "//a[@href='/cart']").click()

@then('check that item exists in cart')
def step(context):
    context.browser.find_element(By.XPATH, "//div[@class='col-sm-4 p-2']/h5[contains(text(),'" + context.item_name + "')]").is_displayed()

@then('check value of total items is "{quantity}" and total payment is correct')
def step(context, quantity):
    item_quantity = context.browser.find_element(By.XPATH, "//div[@class='card card-body']/p[contains(text(),'Total Items')]/following-sibling::h4").text
    item_price = context.browser.find_element(By.XPATH, "//div[@class='card card-body']/p[contains(text(),'Total Payment')]/following-sibling::h3").text
    assert item_quantity == quantity
    total_value_cart = float()
    if quantity == 1:
        assert float(item_price.strip('$')) == float(context.item_price_homepage.strip('$'))*int(quantity)
    else:
        for i in context.price_dict.keys():
            total_value_cart = total_value_cart + float(context.price_dict[i][1].strip('$')) * context.price_dict[i][2]
        assert total_value_cart == float(item_price.strip('$'))

@then('check that delete button appears for the added item')
def step(context):
    button_exist = context.browser.find_element(By.XPATH, "//button[@class='btn btn-danger btn-sm mb-1']").is_enabled()
    assert button_exist == True

@then('click clear button')
def step(context):
    context.browser.find_element(By.XPATH, "//button[contains(text(),'CLEAR')]").click()

@then('check that cart is clear')
def step(context):
    clear_cart = context.browser.find_element(By.XPATH, "//div[contains(text(),'Your cart is empty')]").text
    assert clear_cart == 'Your cart is empty'

@when('for the first item, increase quantity to "{quantity}"')
def step(context, quantity):
    for click in range(int(quantity)-1):
        context.browser.find_element(By.XPATH, "//div[@class='col-sm-4 p-2']/h5[contains(text(),'" + context.price_dict[1][0] + "')]/following::div[2]/button[@class='btn btn-primary btn-sm mr-2 mb-1']").click()
    context.price_dict[1][2] = int(quantity)

@then('check that reduce button displays for the first item')
def step(context):
    context.browser.find_element(By.XPATH, "//div[@class='col-sm-4 p-2']/h5[contains(text(),'" + context.price_dict[1][0] + "')]/following::div[2]/button[@class='btn btn-danger btn-sm mb-1']").is_enabled()

@then('check that Delete button displays for the second item')
def step(context):
    context.browser.find_element(By.XPATH, "//div[@class='col-sm-4 p-2']/h5[contains(text(),'" + context.price_dict[2][0] + "')]/following::div[2]/button[@class='btn btn-danger btn-sm mb-1']").is_enabled()


@then('for the first item, decrease quantity to "{decrease_quantity}"')
def step(context, decrease_quantity):
    for click in range(int(decrease_quantity)-1):
        context.browser.find_element(By.XPATH, "//div[@class='col-sm-4 p-2']/h5[contains(text(),'" + context.price_dict[1][0] + "')]/following::div[2]/button[@class='btn btn-danger btn-sm mb-1']").click()
    context.price_dict[1][2] = int(decrease_quantity)

@then('delete the second item')
def step(context):
    context.browser.find_element(By.XPATH, "//div[@class='col-sm-4 p-2']/h5[contains(text(),'" + context.price_dict[2][0] + "')]/following::div[2]/button[@class='btn btn-danger btn-sm mb-1']").click()


@then('check that the first item is removed from cart')
def step(context):
    try:
        context.browser.find_element(By.XPATH, "//div[@class='col-sm-4 p-2']/h5[contains(text(),'" + context.price_dict[2][0] + "')]").is_displayed()
    except:
        assert True

@then('click checkout button')
def step(context):
    context.browser.find_element(By.XPATH, "//button[contains(text(),'CHECKOUT')]").click()

@then('check that message “Checkout successfully” displayed')
def step(context):
    context.browser.find_element(By.XPATH,"//p[contains(text(),'Checkout successfull')]").is_displayed()


