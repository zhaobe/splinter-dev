import os
from selenium import webdriver

'''
This is a simple file to test the chromedriver path by 
linking the chromedriver path to the os environment and using
the selenium webdriver
    - the <path/to/chromedriver> can be found using the command 
    on a Unix machine: 
    
    'which chromedriver'
    
'''

chromedriver = "<path/to/chromedriver>"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)
driver.get("https://splinter.readthedocs.io/en/latest/index.html")
driver.quit()