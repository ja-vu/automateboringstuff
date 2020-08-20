from selenium import webdriver

browser = webdriver.Firefox()
browser.get('https://automatetheboringstuff.com/')
# elem = browser.find_element_by_css_selector('div.gb_h:nth-child(1) > a:nth-child(1)')
# elem.click()
elems = browser.find_elements_by_css_selector('p')
print(len(elems))

# searchElem = browser.find_element_by_css_selector('.gLFyf')
# searchElem.send_keys('James Bond')
# searchElem.submit()

elem = browser.find_element_by_css_selector('.main > div:nth-child(1) > p:nth-child(8)')
print(elem.text)