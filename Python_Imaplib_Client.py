# Python imaplib — IMAP4 protocol client.
# This module defines three classes, IMAP4, IMAP4_SSL and IMAP4_stream, which encapsulate a connection to an IMAP4 server and
# implement a large subset of the IMAP4rev1 client protocol as defined in RFC 2060.
# It is backward compatible with IMAP4 (RFC 1730) servers, but note that the STATUS command is not supported in IMAP4.
# The IMAP4 class supports the with statement. When used like this, the IMAP4 LOGOUT command is issued automatically when the with
# statement exits. E.g.:
 
from imaplib import IMAP4

    with IMAP4("domain.org") as M:
        M.noop()

#
# OUTPUT:
# ('OK', [b'Nothing Accomplished. d25if65hy903weo.87'])
#