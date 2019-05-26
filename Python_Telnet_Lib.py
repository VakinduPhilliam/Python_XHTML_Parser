# Python Telnet
# telnetlib — Telnet client
# The telnetlib module provides a Telnet class that implements the Telnet protocol. 
# In addition, it provides symbolic constants for the protocol characters, and for the telnet options.
# The symbolic names of the telnet options follow the definitions in arpa/telnet.h, with the leading TELOPT_ removed.
# For symbolic names of options which are traditionally not included in arpa/telnet.h, see the module source itself.
#
# A Telnet object is a context manager and can be used in a with statement. When the with block ends, the close() method
# is called:
# 

from telnetlib import Telnet
    with Telnet('localhost', 23) as tn:

        tn.interact()
