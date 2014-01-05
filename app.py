#!/usr/bin/env python

import urllib

import logging
import json
import urllib2
from bs4 import BeautifulSoup

import sys
import webapp2

from local_settings import username,password

import twill
from twill.commands import *

class Bot(webapp2.RequestHandler):
    def get(self):
        #self.response.out.write(self.gen_post())
        go('http://hackerstreet.in/submit')
        #showforms()
        fv("1", "u", username)
        fv("1", "p", password)
        submit('0')
        go('http://hackerstreet.in/submit')
        #showforms()
        text,url = self.gen_post()
        fv("1", "t", text)
        fv("1", "u", url)
        submit('0')

    def gen_post(self):
        url = "https://twitter.com/yugdom"
        soup = BeautifulSoup( urllib2.urlopen(url).read() )

        #finding the first tweet in yugdom twitter handle
        tweet = soup.find('p',{'class':'js-tweet-text'}).get_text()

        #removing non-ascii characters form tweet
        tweet = "".join(i for i in tweet if ord(i)<128)
        
        text = tweet.split(' ')[:-1]
        text = ' '.join(text)
        url = tweet.split(' ')[-1]
        return text,url

application = webapp2.WSGIApplication([
    ('/', Bot)
    ],debug=True)