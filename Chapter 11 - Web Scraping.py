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

    # 'Gather user input'
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

# Image Site Downloader
# Write a program that goes to a photo-sharing site like Flickr or Imgur,
# searches for a category of photos, 
# and then downloads all the resulting images. 
# You could write a program that works with any photo site that has a search feature.
def imageSiteDownloader():
    import requests, os, bs4
    print('Please enter item you want to search on imgur:')
    searchCategory = input()
    searchText = searchCategory.replace(' ', '%20') #user search input space turn into special character
    url_search = f'https://imgur.com/search?q={searchText}'
    os.makedirs(f'imgur_image_{searchCategory}', exist_ok=True)

    res = requests.get(url_search)
    res.raise_for_status()

    soupSearch = bs4.BeautifulSoup(res.text, 'html.parser')
    url_photo =  soupSearch.select('.post a')

    if url_photo == []:
        print(f'Can\'t find any {searchCategory} picture')
    else:
        for i in range(len(url_photo)):
            pageUrl = 'https://imgur.com' + url_photo[i].get('href')
            res= requests.get(pageUrl)
            res.raise_for_status()
            page_soup = bs4.BeautifulSoup(res.text, 'html.parser') #get full html for picture page
            
            picElements = page_soup.select('head link')  #word around to get the image link from head instead ;), it is slower, but works as of May 2019
            for picElement in picElements:
                if picElement.get('rel') == ['image_src']:
                    picUrl = picElement.get('href') #image link for each page
                    print(f'downloading picture {picUrl}')
                    res = requests.get(picUrl)
                    res.raise_for_status()
        
                    with open(os.path.join(f'imgur_image_{searchCategory}', os.path.basename(picUrl)), 'wb') as imageFile:
                        for chunk in res.iter_content(100000):
                            imageFile.write(chunk)
                        imageFile.close()
    
    print('it\'s done!')

# 2048
# 2048 is a simple game where you combine tiles by sliding them up, down, left, or right 
# with the arrow keys. You can actually get a fairly high score by repeatedly 
# sliding in an up, right, down, and left pattern over and over again. 
# Write a program that will open the game at 
# https://gabrielecirulli.github.io/2048/ and keep sending up, right, down, and 
# left keystrokes to automatically play the game.
def play_2048():
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    browser = webdriver.Firefox()
    browser.get('https://gabrielecirulli.github.io/2048/')

    # while game-over not exist
    condition = len(browser.find_elements_by_class_name('game-over'))
    while condition == 0:
        condition = len(browser.find_elements_by_class_name('game-over'))
        browser.find_element_by_tag_name('html').send_keys(Keys.UP)
        browser.find_element_by_tag_name('html').send_keys(Keys.RIGHT)
        browser.find_element_by_tag_name('html').send_keys(Keys.DOWN)
        browser.find_element_by_tag_name('html').send_keys(Keys.LEFT)
    print('game end!')

if __name__ == "__main__":
    # commandLineEmailer()
    imageSiteDownloader()
    # play_2048()