#! /usr/bin/env python3
#  cmd_line_email.py -- takes an email recipient email address and string of text as command line arguments 
#					 -- and then, using Selenium, logs into the current gmail account (which must already be 
#					 -- logged in) and then sends the string as an email to the email address provided
#  Usage: ./cmd_line_email.py <email_recipient@blah.com> <string of text...>


"""
README:
Automate The Boring Stuff Python (Ch.11 -- pg 262) Project
Solved by Z Meeks 10/01/17

Note:	if and when gmail changes their webpage, or even just the css selectors, 
		this script will no longer work correctly and will need to be updated...
"""


my_login = '________@gmail.com' # replace with your valid @gmail login
my_pword = '***********'		# replace with your correct password

import sys, time
from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://accounts.google.com/signin')
loginElem = browser.find_element_by_css_selector('#identifierId')
loginElem.send_keys(my_login)
nextElem = browser.find_element_by_css_selector('#identifierNext')
nextElem.click()
time.sleep(3)
pword_elem = loginElem = browser.find_element_by_css_selector('#password') 
pword_elem.send_keys(my_pword)
nextElem = browser.find_element_by_css_selector('#passwordNext') 
nextElem.click()
time.sleep(1)
browser.get('https://mail.google.com/mail/#inbox')
time.sleep(2)
nextElem = browser.find_element_by_css_selector('.T-I-KE')
nextElem.click()
time.sleep(2)
recipElem = browser.find_element_by_css_selector('.oj div textarea') 
recipElem.send_keys(sys.argv[1])
recipElem.click()
time.sleep(1)
msgElem = browser.find_element_by_css_selector('.Ar.Au div') 
sz_args = len(sys.argv)
msg_str = ""
for i in range(2,sz_args):
	msg_str += sys.argv[i] + ' '
time.sleep(1)
print("message = %s" % (msg_str))
msgElem.send_keys(str(msg_str))
time.sleep(1)
nextElem = browser.find_element_by_css_selector('.T-I.J-J5-Ji.aoO.T-I-atl.L3')
nextElem.click()