from Crypto.Cipher import DES
from Crypto.Cipher import AES


def VigenereCipherEncode(message: str, key: str):
    result = ""
    keyLength = len(key)
    for i in range(0, len(message)):
        result += chr((ord(message[i]) + ord(key[i % keyLength])) % 256)
    return result


def VigenereCipherDecode(message: str, key: str):
    result = ""
    keyLength = len(key)
    for i in range(0, len(message)):
        result += chr((256 + ord(message[i]) - ord(key[i % keyLength])) % 256)
    return result


def CesarCipherEncode(message: str):
    result = ""
    for i in range(0, len(message)):
        result += chr((ord(message[i]) + 3) % 256)
    return result


def CesarCipherDecode(message: str):
    result = ""
    for i in range(0, len(message)):
        result += chr((256 + ord(message[i]) - 3) % 256)
    return result


def pad(text: bytearray, by: int):
    while len(text) % by != 0:
        text += b" "
    return text


def str2bytearray(string: str):
    return bytearray(string, encoding="1251")


def bytearray2str(bytearr: bytearray):
    return str(bytearr, encoding="1251")


def des_cipher_encrypt(message: str, key: str):
    byte_key = pad(str2bytearray(key))
    print('Length of byte_key: ' + str(len(byte_key)))
    if len(byte_key) != 8:
        raise ValueError('ValueError: Length of key must be equal to 8')

    message = pad(str2bytearray(message), len(byte_key))

    des = DES.new(byte_key, DES.MODE_ECB)
    output = bytearray(len(message))
    des.encrypt(message, output=output)
    return bytearray2str(output)


def des_cipher_decrypt(message: str, key: str):
    byte_key = pad(str2bytearray(key))
    print('Length of byte_key: ' + str(len(byte_key)))
    if len(byte_key) != 8:
        raise ValueError('ValueError: Length of key must be equal to 8')

    message = pad(str2bytearray(message), len(byte_key))

    des = DES.new(byte_key, DES.MODE_ECB)
    output = bytearray(len(message))
    des.decrypt(message, output=output)
    return bytearray2str(output).strip()


def aes_cipher_encrypt(message: str, key: str):
    byte_key = str2bytearray(key)
    if len(byte_key) not in (16, 24, 32):
        raise ValueError("Incorrect AES key length (%d bytes)" % len(key))

    aes = AES.new(byte_key, AES.MODE_ECB)

    message = pad(str2bytearray(message), len(byte_key))

    output = bytearray(len(message))
    aes.encrypt(message, output=output)
    return bytearray2str(output)


def aes_cipher_decrypt(message: str, key: str):
    byte_key = str2bytearray(key)
    if len(byte_key) not in (16, 24, 32):
        raise ValueError("Incorrect AES key length (%d bytes)" % len(key))

    aes = AES.new(byte_key, AES.MODE_ECB)

    message = pad(str2bytearray(message), len(byte_key))

    output = bytearray(len(message))
    aes.decrypt(message, output=output)
    return bytearray2str(output).strip()

# tests
def test(funcEncode, funcDecode, message: str):
    print('=============== Test ================')
    encoded = funcEncode(message)
    decoded = funcDecode(encoded)
    print('Message: "' + message + '"')
    print('Encoded: "' + encoded + '"')
    print('Decoded: "' + decoded + '"')
    print('Test success: ' + str(bool(decoded == message)))
    print('============= End test ==============\n')


def testWithKey(funcEncode, funcDecode, message: str, key: str):
    print('=============== Test ================')
    encoded = funcEncode(message, key)
    decoded = funcDecode(encoded, key)
    print('Message: "' + message + '"')
    print('Encoded: "' + encoded + '"')
    print('Decoded: "' + decoded + '"')
    print('Test success: ' + str(bool(decoded == message)))
    print('============= End test ==============\n')


def main():
    testWords = ['message', 'apple', 'simple text', '', 'русская строка']
    # print('####################################################')
    # print('############# Test Cesar ###########################')
    # print('####################################################\n')
    # for testWord in testWords:
    #     test(CesarCipherEncode, CesarCipherDecode, testWord)
    #
    # print('####################################################')
    # print('############ Test Vigenere #########################')
    # print('####################################################\n')
    # for testWord in testWords:
    #     testWithKey(VigenereCipherEncode, VigenereCipherDecode, testWord, 'prosto key')

    # print('####################################################')
    # print('############ Test DES ##############################')
    # print('####################################################\n')
    # for testWord in testWords:
    #     testWithKey(des_cipher_encrypt, des_cipher_decrypt, testWord, 'prostoke')

    print('####################################################')
    print('############ Test AES ##############################')
    print('####################################################\n')
    for testWord in testWords:
        testWithKey(aes_cipher_encrypt, aes_cipher_decrypt, testWord, 'prostokeprostoke')


if __name__ == '__main__':
    main()

