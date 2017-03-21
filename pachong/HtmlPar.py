#Author:zzk
#coding=utf-8
from HTMLParser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print "a start tag:",tag,self.getpos()

parser=MyHTMLParser()

parser.feed('<div><p>"hello"</p></div>')