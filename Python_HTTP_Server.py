# Python HTML and XHTML Parser
# html.parser — Simple HTML and XHTML parser.
# This module defines a class HTMLParser which serves as the basis for parsing text files formatted in HTML
# (HyperText Mark-up Language) and XHTML.
# http.server — HTTP servers.
# This module defines classes for implementing HTTP servers (Web servers).
#
# One class, HTTPServer, is a socketserver.TCPServer subclass. It creates and listens at the HTTP socket, dispatching
# the requests to a handler. Code to create and run the server looks like this:
 
def run(server_class=HTTPServer, handler_class=BaseHTTPRequestHandler):
    server_address = ('', 8000)

    httpd = server_class(server_address, handler_class)

    httpd.serve_forever()
