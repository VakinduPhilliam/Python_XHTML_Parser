# Python Telnet
# telnetlib — Telnet client
# The telnetlib module provides a Telnet class that implements the Telnet protocol. 
# In addition, it provides symbolic constants for the protocol characters, and for the telnet options.
# The symbolic names of the telnet options follow the definitions in arpa/telnet.h, with the leading TELOPT_ removed.
# For symbolic names of options which are traditionally not included in arpa/telnet.h, see the module source itself.
#
#
# A simple example illustrating typical use:
#
# 

import getpass
import telnetlib

HOST = "localhost"
user = input("Enter your remote account: ")

password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until(b"login: ")
tn.write(user.encode('ascii') + b"\n")

if password:

    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

tn.write(b"ls\n")
tn.write(b"exit\n")

print(tn.read_all().decode('ascii'))
