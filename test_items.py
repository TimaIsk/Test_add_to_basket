import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_add_basket_button(browser):
    browser.get(link)
    time.sleep(30)
    button = browser.find_element_by_xpath('//button[@class="btn btn-lg btn-primary btn-add-to-basket"]')

    assert len(button) > 0, "Mission: Impossible"
    
