# Python HTML and XHTML Parser
# html.parser — Simple HTML and XHTML parser.
# This module defines a class HTMLParser which serves as the basis for parsing text files formatted in HTML
# (HyperText Mark-up Language) and XHTML.
# 
# The SimpleHTTPRequestHandler class can be used in the following manner in order to create a very basic webserver serving files
# relative to the current directory:
# 

import http.server
import socketserver

PORT = 8000

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("serving at port", PORT)

    httpd.serve_forever()
