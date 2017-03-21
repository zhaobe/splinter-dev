from splinter import Browser

browser = Browser()

browser.visit('https://splinter.readthedocs.io/')

# testing wait_time
browser.is_text_present('splinter', wait_time=10)

# testing execution of simple script
#browser.execute_script("alert('Hello')")

browser.quit()