from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

def set_browser_chrome(site_name):
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    browser.get(site_name)
    return browser

def set_browser_firefox(site_name):
    
    
    browser = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    browser.get(site_name)
    return browser