from splinter import Browser

browser = Browser()

# visit site
browser.visit('http://google.com')
browser.visit('http://selenium-python.readthedocs.io/')
browser.visit('https://splinter.readthedocs.io/')

# browser navigation
browser.back()

# saving vars
titleOfBrowser = browser.title
urlOfBrowser = browser.url

browser.forward()

# testing wait_time
browser.is_text_present('splinter', wait_time=10)

# testing execution of simple script
#browser.execute_script("alert('Hello')")

browser.quit()

# should output the second site info
print titleOfBrowser
print urlOfBrowser