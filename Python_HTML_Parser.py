# Python HTML and XHTML Parser
# html.parser — Simple HTML and XHTML parser.
# This module defines a class HTMLParser which serves as the basis for parsing text files formatted in HTML
# (HyperText Mark-up Language) and XHTML.
# HTML Parser Application
#
# As a basic example, below is a simple HTML parser that uses the HTMLParser class to print out start tags, end tags, and
# data as they are encountered:
# 

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        print("Encountered a start tag:", tag)

    def handle_endtag(self, tag):
        print("Encountered an end tag :", tag)

    def handle_data(self, data):
        print("Encountered some data  :", data)

parser = MyHTMLParser()

parser.feed('<html><head><title>Test</title></head>'
            '<body><h1>Parse me!</h1></body></html>')
