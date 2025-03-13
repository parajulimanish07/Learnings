import random
import string # for generating random alphanumeric strings like passwords

chars = " " + string.punctuation + string.digits + string.ascii_letters  # all possible characters #ascii_letters includes both uppercase and lowercase letters
chars = list(chars)
key = chars.copy()

random.shuffle(key) # shuffle the key list to create a random password 


#print(f"chars:{chars}")
#print(f"key:{key}")

#ENCRYPTION

plain_text = input("Enter the message to encrypt: ")
cipher_text = "" # to store the encrypted message

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]

print(f"original message: {plain_text}")
print(f"encrypted message: {cipher_text}")

#DECRYPTION

cipher_text = input("Enter the message to encrypt: ")
plain_text = "" # to store the encrypted message

for letter in cipher_text:
    index = key.index(letter)
    plain_text += chars[index]

print(f"original message: {cipher_text}")
print(f"encrypted message: {plain_text}")


