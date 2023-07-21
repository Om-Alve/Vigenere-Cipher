import string

chars = string.punctuation + string.ascii_lowercase + string.digits + " " + string.ascii_uppercase

chars = list(chars)
 
n = len(chars)

def encrypt():
    message = input("Enter a message to encrypt :\n")
    
    keyword = input("Keyword : ")

    kl = len(keyword)

    if len(message) - kl < 0 :
        keyword = keyword[:len(message)]
    else:
        for i in range(len(message) -kl):
            keyword+= keyword[(i%kl)]

    keys = [chars.index(l) for l in keyword]

    encrypted = [ chars[(chars.index(c) + key) % n] for key,c in zip(keys,message)]
    
    print("Encrypted Text:"+''.join(encrypted))

def decrypt():
    
    message = input("Enter a message to decrypt :\n")
    
    keyword = input("Keyword : ")

    kl = len(keyword)

    if len(message) - kl < 0 :
        keyword = keyword[:len(message)]
    else:
        for i in range(len(message) -kl):
            keyword+= keyword[(i%kl)]

    keys = [chars.index(l) for l in keyword]

    decrypted = [chars[(chars.index(c) - key)%n] for key,c in zip(keys,message)]

    print("Decrypted Text:"+''.join(decrypted))

action = input("Enter E to encrypt or D to decrept a message: ").upper()

if action == "E":
    encrypt()
elif action == "D":
    decrypt()
else:
    print("Invalid Input!")


