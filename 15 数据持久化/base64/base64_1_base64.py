import base64

def bytes_b64(convert_bytes):
    bytes_b64code = base64.b64encode(convert_bytes)
    return bytes_b64code.decode()

def b64_bytes(b64):
    b4code_back = bytes(b64, 'utf8')
    signature = base64.b64decode(b4code_back)
    return signature

if __name__ == '__main__':
    test_bytes = b'\xac!{'
    base64_result = bytes_b64(test_bytes)
    print(base64_result)
    bytes_result = b64_bytes(base64_result)
    print(bytes_result)
