#!/usr/bin/env python
from bs4 import BeautifulSoup
from local_settings import username,password
import twill
import webapp2
import urllib2
from twill.commands import *

class Bot(webapp2.RequestHandler):
    def get(self):
        go('http://hackerstreet.in/submit')
        fv("1", "u", username)
        fv("1", "p", password)
        submit('0')
        go('http://hackerstreet.in/submit')
        text,url = self.gen_post()
        fv("1", "t", text)
        fv("1", "u", url)
        submit('0')
        self.response.write(text + url)

    def gen_post(self):
        url = "https://twitter.com/yugdom"
        soup = BeautifulSoup( urllib2.urlopen(url).read() )
        #finding the first tweet in yugdom twitter handle
        tweet = soup.find('p',{'class':'js-tweet-text'}).get_text()
        #removing non-ascii characters form tweet
        tweet = "".join(i for i in tweet if ord(i)<128)
        #splitting tweet into text and url
        text = tweet.split(' ')[:-1]
        text = ' '.join(text)
        url = tweet.split(' ')[-1]
        return text,url

application = webapp2.WSGIApplication([
    ('/', Bot)
    ],debug=True)