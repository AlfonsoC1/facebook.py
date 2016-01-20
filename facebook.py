from selenium import webdriver

print('Input your email adrress')
userEmail = raw_input()

print('Input your password')
userPassword = raw_input()

browser = webdriver.Firefox()
browser.get('http://facebook.com')

emailElem = browser.find_element_by_id('email')
emailElem.send_keys(userEmail)


passwordElem = browser.find_element_by_id('pass')
passwordElem.send_keys(userPassword)

signInElem = browser.find_element_by_id('u_0_n')
signInElem.click()

