"""
base.py is a module created to identify base encoded strings. ie base64, base32, base58
"""
import re
import base64
import binascii

# a = '''VGhpcyBpcyBvbmx5IGEgdGVzdA==''' # <-- This is only a test

patt = re.compile(r'(?:[A-Za-z0-9+/]{4}){2,}(?:[A-Za-z0-9+/]{2}[AEIMQUYcgkosw048]=|[A-Za-z0-9+/][AQgw]==)')

def decodeBase64(args):
    try:
        re.match(patt, args.base)
        results = base64.b64decode(args.base).decode("utf-8")
        print(f'Your results are\n{results}')
    except binascii.Error as e:
        print(f'Input is not base64 encoded.\nError: {e}')
# decodBase64()