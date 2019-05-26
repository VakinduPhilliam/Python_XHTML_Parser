# Python HTML and XHTML Parser
# html.parser — Simple HTML and XHTML parser.
# This module defines a class HTMLParser which serves as the basis for parsing text files formatted in HTML
# (HyperText Mark-up Language) and XHTML.
#
# http.cookiejar — Cookie handling for HTTP clients.
#
# The http.cookiejar module defines classes for automatic handling of HTTP cookies.
# It is useful for accessing web sites that require small pieces of data – cookies – to be set on the client machine by an HTTP
# response from a web server, and then returned to the server in later HTTP requests.
#
# DefaultCookiePolicy Objects
# 
# Implements the standard rules for accepting and returning cookies.
# 
# Both RFC 2965 and Netscape cookies are covered. RFC 2965 handling is switched off by default.
# 
# The easiest way to provide your own policy is to override this class and call its methods in your overridden implementations before
# adding your own additional checks:
# 

import http.cookiejar

class MyCookiePolicy(http.cookiejar.DefaultCookiePolicy):

    def set_ok(self, cookie, request):

        if not http.cookiejar.DefaultCookiePolicy.set_ok(self, cookie, request):
            return False

        if i_dont_want_to_store_this_cookie(cookie):
            return False

        return True
