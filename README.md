# splinter-dev
Learning the basics of splinter automation

The setup below is done on a Mac OS with Homebrew and pip installed.

# Setup
- create a repo and cd into it, `pip install virtualenv` if you don't already have virtual environment on your local machine
- run `virtualenv env` to create a virtual environment for this repo
- run `pip install splinter`

## Setup Chrome WebDriver
- good reference to setup [Chromedriver](https://splinter.readthedocs.io/en/latest/drivers/chrome.html)
- for Mac OSX, it is recommended to use Homebrew to `brew install chromedriver`
- once you have installed chromedriver, use `which chromedriver` to locate the path of your chromedriver
- export that path to your `bash_profile` or `/etc/paths`

- if you installed the chromedriver, you will most likely need selenium as well
- to check if you have selenium installed you can use `pip list` to see all the packages from pip
- to check the version of selenium you have, you will have to open the Python interpreter and type `import selenium`, then `help(selenium)` to see which version of selenium you have installed.

- once you have exported the chromedriver path, you may run `python quick-tut.py` and it should run a demo of an automated open browser, go to Google, search `splinter - python acceptance testing for web applications`, quits browser, and returns `Yes, the official website was found!`

## For debugging chromedriver PATH
- if you don't want to export the chromedriver path on your local machine, you may add the code below to the top of `quick-tut.py` after the imports [reference doc](https://splinter.readthedocs.io/en/latest/drivers/chrome.html)
    - `executable_path = {'executable_path':' <put path to chromedriver here> '}`
    - `browser = Browser('chrome', **executable_path)`
