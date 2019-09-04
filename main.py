
def VigenereCipherEncode(message : str, key : str):
    result = ''
    keyLength = len(key)
    for i in range(0, len(message)):
        result += chr(ord(message[i]) + ord(key[i % keyLength]))
    return result

def VigenereCipherDecode(message : str, key : str):
    result = ''
    keyLength = len(key)
    for i in range(0, len(message)):
        result += chr(ord(message[i]) - ord(key[i % keyLength]))
    return result


def CesarCipherEncode(message : str):
    result = ''
    for i in range(0, len(message)):
        result += chr(ord(message[i]) + 3)
    return result

def CesarCipherDecode(message : str):
    result = ''
    for i in range(0, len(message)):
        result += chr(ord(message[i]) - 3)
    return result


def test(funcEncode, funcDecode, message : str):
    print('=============== Test ================')
    encoded = funcEncode(message)
    decoded = funcDecode(encoded)
    print('Message: "' + message + '"')
    print('Encoded: "' + encoded + '"')
    print('Decoded: "' + decoded + '"')
    print('Test success: ' + str(bool(decoded == message)))
    print('============= End test ==============\n')

def testWithKey(funcEncode, funcDecode, message : str, key : str):
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
    print('####################################################')
    print('############# Test Cesar ###########################')
    print('####################################################\n')
    for i in range(0, len(testWords)):
        test(CesarCipherEncode, CesarCipherDecode, testWords[i])

    print('####################################################')
    print('############ Test Vigenere #########################')
    print('####################################################\n')
    for i in range(0, len(testWords)):
        testWithKey(VigenereCipherEncode, VigenereCipherDecode, testWords[i], 'prosto key')


if __name__ == '__main__':
    main()

