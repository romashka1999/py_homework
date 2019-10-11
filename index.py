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

################################################## L I S T #######################################################
def listEncrypt(key, word):
    ans = ''
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    key = setKey(key, word)
    for i in range(len(word)):
        ans += alphabet[(alphabet.find(word[i])+alphabet.find(key[i]))%26]
    return ans

def lisetDecrypt(key, word):
    ans = ''
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    key = setKey(key, word)
    for i in range(len(word)):
        ans += alphabet[(26+(alphabet.find(word[i])-alphabet.find(key[i])))%26]
    return ans

################################################## T U P L E #######################################################
def tupleEncrypt(key, word):
    ans = ''
    alphabet = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')
    key = setKey(key, word)
    for i in range(len(word)):
        ans += alphabet[(alphabet.find(word[i])+alphabet.find(key[i]))%26]
    return ans

def tupleDecrypt(key, word):
    ans = ''
    alphabet = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')
    key = setKey(key, word)
    for i in range(len(word)):
        ans += alphabet[(26+(alphabet.find(word[i])-alphabet.find(key[i])))%26]
    return ans

print(strDecrypt(key, word))



        
