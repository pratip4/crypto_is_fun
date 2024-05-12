# Cryptography is fun
In this repository I will be implementing some basic Cryptographic algorithms using Python.
The community can feel free to contribute or learn as well.

## Symmetric or Private Key Encryption
### Caesar Cipher - Going back 2000 years
This is a 2000 years old Cipher where the key is added to the Alphabets and the final encrypted string is created.
The formulae of encryption is : (x+k) % 26
The caesar_cipher.py implements encryption & decryption of the same.

### Vigenere Cipher - The 16th century's invincible cipher.
Vigenere cipher was the invinsible cipher of the 16th century. It was finally cracked by the Kaminski technique in the 19th century.
In the file vigenere_cipher.py, I have done a simple string encryption & decryption using a key string.
The formulae for encryption is : (xi + ki) % 26. So every character is mapped to a character of the secret key in this Cipher.
