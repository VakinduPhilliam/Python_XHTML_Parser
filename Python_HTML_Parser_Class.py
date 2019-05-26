# Python HTML and XHTML Parser
# html.parser — Simple HTML and XHTML parser.
# This module defines a class HTMLParser which serves as the basis for parsing text files formatted in HTML
# (HyperText Mark-up Language) and XHTML.
#
# The following class implements a parser:
# 

from html.parser import HTMLParser
from html.entities import name2codepoint

class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        print("Start tag:", tag)

        for attr in attrs:
            print("     attr:", attr)

    def handle_endtag(self, tag):
        print("End tag  :", tag)

    def handle_data(self, data):
        print("Data     :", data)

    def handle_comment(self, data):
        print("Comment  :", data)

    def handle_entityref(self, name):
        c = chr(name2codepoint[name])
        print("Named ent:", c)

    def handle_charref(self, name):

        if name.startswith('x'):
            c = chr(int(name[1:], 16))

        else:
            c = chr(int(name))
        print("Num ent  :", c)

    def handle_decl(self, data):
        print("Decl     :", data)

parser = MyHTMLParser()
