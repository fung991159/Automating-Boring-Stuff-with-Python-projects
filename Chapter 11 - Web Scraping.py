# Command Line Emailer
# Write a program that takes an email address 
# and string of text on the command line 
# and then, using Selenium, logs into your email account 
# and sends an email of the string to the provided address. 
# (You might want to set up a separate email account for this program.)

# This would be a nice way to add a notification feature to your programs. 
# You could also write a similar program to send messages from a Facebook or Twitter account.
def commandLineEmailer():
    from selenium import webdriver
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.common.exceptions import TimeoutException
    from selenium.webdriver.common.keys import Keys

    'Gather user input'
    print('Please input receipt\'s address:')
    reAddress = input()
    print('Please input E-mail subject')
    emailSubject = input()
    print('Please input E-mail content message')
    emailBody = input()

    print('starting execution')
    browser = webdriver.Firefox()
    browser.get('https://www.gmx.com/')
    
    #log into E-mail account
    browser.find_element_by_id('login-button').click()
    loginEmailElem = browser.find_element_by_id('login-email')
    loginEmailElem.send_keys('')   #Login user name here
    passwordElem = browser.find_element_by_id('login-password')
    passwordElem.send_keys('') #login password here
    # browser.find_element_by_css_selector('button.btn:nth-child(11)').click()
    passwordElem.submit()

    #Notfication page before mail dashboard, might not be there in future
    try:
        browser.find_element_by_class_name('button cta ').click()
    except:
        pass

    delay = 10 #seconds
    browser.implicitly_wait(delay)
    
    browser.switch_to.frame(browser.find_element_by_id('thirdPartyFrame_home'))
    browser.find_element_by_class_name('new-mail').click()
    browser.implicitly_wait(delay)
    browser.switch_to.default_content()
    browser.switch_to.frame(browser.find_element_by_id('thirdPartyFrame_mail')) #nested i-frame lv1
    browser.find_element_by_class_name('select2-input').send_keys(reAddress)
    browser.find_element_by_id('id53').send_keys(emailSubject)
    browser.switch_to.frame(browser.find_element_by_class_name('cke_wysiwyg_frame'))  #nested i-frame lv2
    browser.find_element_by_id('body').click()
    browser.find_element_by_id('body').send_keys(emailBody)
    browser.switch_to.default_content()
    browser.switch_to.frame(browser.find_element_by_id('thirdPartyFrame_mail'))   
    browser.find_element_by_id('compose-form-submit-send').click()

    input('Press Enter to send E-mail')
    print('E-mail sent!')
    
if __name__ == "__main__":
    # commandLineEmailer()
