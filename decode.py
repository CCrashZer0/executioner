import re
import base64
import binascii

def decode_string(args):
    patt = re.compile(r'(?:[A-Za-z0-9+/]{4}){2,}(?:[A-Za-z0-9+/]{2}[AEIMQUYcgkosw048]=|[A-Za-z0-9+/][AQgw]==)')

    try:
        re.match(patt, args.base)
        results = base64.b64decode(args.base).decode("utf-8")
        print(f'[+] Decoded sting: {results}')
    except binascii.Error as e:
        print(f'Input is not base64 encoded:\n{e}')