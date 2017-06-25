import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#You can put this in your path or optionally specify exactly where you the chromedriver executable is
browser = webdriver.Chrome()

#Where you search
base = u'https://twitter.com/search?q='

#Argument to search for. Replace 'empty' with search query
query = 'empty'
url = base + query
#get the url
browser.get(url)
time.sleep(1)

body = browser.find_element_by_tag_name('body')

#how many time to send the page_down command
for _ in range(10):
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.3)

tweets = browser.find_element_by_class_name('tweet-text')
#Print the tweets
for tweet in tweets:
    print(tweet.text)