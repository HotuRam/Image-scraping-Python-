import selenium
import time
from selenium import webdriver
import io
from io import StringIO
import string
from PIL import Image
import hashlib
import os
import requests
#############################################################################################################
DRIVER_PATH = 'chromedriver.exe'
# driver download link - https://chromedriver.chromium.org/downloads
# make sure you put chromedriver exe file in same folder as where is your py file (Important)
# my chrome browser Version 93.0.4577.63 (Official Build) (64-bit) this diver is work for this only,
# so you have to check your version and download the driver first.
wd = webdriver.Chrome(executable_path=DRIVER_PATH)
wd.get('https://google.com')
search_box = wd.find_element_by_css_selector('input.gLFyf')
search_box.send_keys('Pandas')   #####Change the name of animal like cat or dog 
wd.quit() # closing the driver