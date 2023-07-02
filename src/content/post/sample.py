# from pwntools.pwnlib.util.fiddling import *
from pwn import *
print(xor(b"label",13))