#!/bin/env python3

# Convert a 32-bit packed IPV4 address to its standard dotted-quad string representation


import socket
import struct


def convert(bits):
  """Convert a 32-bit packed IPv4 address (a bytes-like object four bytes in length)
  to its standard dotted-quad string representation (for example, ‘123.45.67.89’).
  This is useful when conversing with a program that uses the standard C library and
  needs objects of type struct in_addr, which is the C type for the 32-bit packed
  binary data this function takes as an argument.

  If the byte sequence passed to this function is not exactly 4 bytes in length,
  OSError will be raised. inet_ntoa() does not support IPv6, and inet_ntop() should
  be used instead for IPv4/v6 dual stack support.
  """

  addr_long = int(bits, 16)

  struct_pack = struct.pack('<L', addr_long)

  converted = socket.inet_ntoa(struct_pack)

  return converted
