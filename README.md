# facebook.py

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


<!--code should be saved somewhere (for example desktop) as facebook.py
when opening it in terminal or cmd, go to where ever facebook.py is saved at and type python facebook.py-->
<!--from terminal/cmd enter email and password-->
