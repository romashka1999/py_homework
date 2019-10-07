key = str(input('input key : '))
word = str(input('input word : '))

# setKey if a function to create key for encryption and decryption a word
def setKey(key, word):
    while(len(key) < len(word)):
        key += key
    return key[0:len(word)]
################################################## S T R I N G #######################################################
def strEncrypt(key, word):
    ans = ''
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    key = setKey(key, word)
    for i in range(len(word)):
        ans += alphabet[(alphabet.find(word[i])+alphabet.find(key[i]))%26]
    return ans

def strDecrypt(key, word):
    ans = ''
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    key = setKey(key, word)
    for i in range(len(word)):
        ans += alphabet[(26+(alphabet.find(word[i])-alphabet.find(key[i])))%26]
    return ans



print(strDecrypt(key, word))



        
