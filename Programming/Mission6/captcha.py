# Captcha Beater for HTS Mission 6
# https://www.hackthissite.org/missions/prog/6/
# Author: CuddleDeath
# Date: 9/8/2016

import mechanize
import os
import cookielib
import urllib
import sys
import re
from bs4 import BeautifulSoup
from PIL import Image
from selenium import webdriver
import capture
from capture import Screenshot

br = mechanize.Browser()
cj = cookielib.CookieJar()
br.set_cookiejar(cj)

# Browser options
br.set_handle_equiv(True)

#br.set_handle_gzip(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)

# User-Agent (this is cheating, ok?)
br.addheaders = [
    ('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

# Follows refresh 0 but not hangs on refresh > 0
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.open("https://www.hackthissite.org/missions/prog/6/")
br.select_form(nr=0)
br.form['username'] = '********'  # Enter Username
br.form['password'] = '********'  # Enter Password e1f516b84ed4
br.submit()

webdriver.get('https://www.hackthissite.org/missions/prog/6/image/')
#   Retrieve Image
#br.retrieve('https://www.hackthissite.org/missions/prog/6/image/', 'PNG.png')
# Open Image
#im = Image.open('PNG.png' , 'r' )
#site = br.open("https://www.hackthissite.org/missions/prog/6/image/")
#s = Screenshot()
#s.capture(site, 'website.png')


#print text
#br.select_form(nr=0)
#br.form['solution'] = str(result)
#br.submit()
