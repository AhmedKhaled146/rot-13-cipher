alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def encrypt(msg, rot):
    cipherText = ''

    for letter in msg:
        if letter in alphabet:
            cipherIndex = (alphabet.index(letter) + rot) % 26 
            cipherText = cipherText + alphabet[cipherIndex]
        else:
            cipherText = cipherText + letter 
    return cipherText

msg = 'HELLO WOrLd'
rot = 13 
print (encrypt(msg,rot))