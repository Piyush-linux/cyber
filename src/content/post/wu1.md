---
title: "Write Ups 1 - Cryptography"
description: "This post is for testing and listing a number of different markdown elements"
publishDate: "26 Jun 2023"
tags: ["doc","crypto"]
---

ASCII is a 7-bit encoding standard which allows the representation of text using the integers 0-127.
```py
# Using the below integer array, convert the numbers to their corresponding ASCII characters to obtain a flag.
[99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]
# Python
a=[99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]
b=[]
for x in a:
	b.append(chr(x))
print("".join(b))


```
# Hexadecimal
- https://techantidote.com/hexadecimal-basics-using-basic-linux-utilities/

Hexadecimal can be used in such a way to represent ASCII strings. First each letter is converted to an ordinal number according to the ASCII table (as in the previous challenge). Then the decimal numbers are converted to base-16 numbers, otherwise known as hexadecimal. The numbers can be combined together, into one long hex string.

63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d

```sh
echo -n "63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d" | xxd -r -p
```
```py
a=bytes.fromhex()
b=a.hex()
print(b)
```

# Base64

Another common encoding scheme is Base64, which allows us to represent binary data as an ASCII string using an alphabet of 64 characters. One character of a Base64 string encodes 6 binary digits (bits), and so 4 characters of Base64 encode three 8-bit bytes.

```sh
72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf
# Revert a plaintext hexdump back into binary, and save it as a binary file: xxd -r -p input_file output_file
# Encode the contents of a file as base64 and write the result to `stdout`: base64 path/to/file
# hex to binary to base64
```
```sh
echo "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf" | xxd -r -p | base64
```
```py
import base64
num="72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"
a=base64.b64encode(num)
print(a)
```

# Bytes and Big Integers

- python cryptography

Cryptosystems like RSA works on numbers, but messages are made up of characters. How should we convert our messages into numbers so that mathematical operations can be applied?

The most common way is to take the ordinal bytes of the message, convert them into hexadecimal, and concatenate. This can be interpreted as a base-16/hexadecimal number, and also represented in base-10/decimal.

```sh
message: HELLO
ascii bytes: [72, 69, 76, 76, 79]
hex bytes: [0x48, 0x45, 0x4c, 0x4c, 0x4f]
base-16: 0x48454c4c4f
base-10: 310400273487
```

```py
# Convert the following integer back into a message:
# 11515195063862318899931685488813747395775516287289682636499965282714637259206269

from Crypto.Util.number import *
num=11515195063862318899931685488813747395775516287289682636499965282714637259206269
a=long_to_bytes(num)
print(a)
```
# XOR

XOR is a bitwise operator which returns 0 if the bits are the same, and 1 otherwise. In textbooks the XOR operator is denoted by ⊕, but in most challenges and programming languages you will see the caret ^ used instead.

- [pwntools](https://guyinatuxedo.github.io/02-intro_tooling/pwntools/index.html)

```sh
from pwn import *
print(xor(b"label",13))
```


---

# Resources
- https://cryptohack.org/courses/intro/xor1/
- https://pwnable.kr/play.php