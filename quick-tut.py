# creating the browser instance
from splinter import Browser

browser = Browser('chrome')

# going to google.com
browser.visit('http://google.com')

# input search for splinter - python acceptance ...
browser.fill('q', 'splinter - python acceptance testing for web applications')

# find the search button and click it
browser.find_by_name('btnG').click()

# check if the Splinter official website is in search 
if browser.is_text_present('splinter.readthedocs.io'):
    print "Yes, the official website was found!"
else:
    print "No, it wasn't found... We need to improve our SEO techniques"

# close the browser
browser.quit()
