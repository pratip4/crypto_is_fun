from loguru import logger

# In Caesar Cipher the alphabets are manipulated with the key
# hence we need to determine the numerical value of a char.
# Hence the variable ALPHABET is being defined.


class CaesarCipher():
    def __init__(self):
        self.ALPHABET = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    def encrypt(self, msg, key):
        logger.debug(f"msg to encrypt {msg}")
        emsg = ''
        # now we will apply the Caesar Cipher formulae for encryption
        
        # first converting the numeric equivalent after encryption
        # formulae for encryption = (x+k) mod(ALPHABET)
        num_encrypted = [(lambda num_encry : (self.ALPHABET.find(c.upper()) + key) % len(self.ALPHABET))(c) for c in msg]
        logger.debug(f"numerical chars of encrypted value :: {num_encrypted}")

        # Now I will convert the numerical value to char and form the encrypted string
        char_encr = [(lambda encr_char : self.ALPHABET[num])(num) for num in num_encrypted]
        emsg = ''.join(char_encr)
        return emsg
    
    # Let's decrypt the String
    def decrypt(self, encr_msg, key):
        logger.debug(f"decrypting the encrypted string")

        # decryption formulae = (x-k) mod(ALPHABET)
        num_decr = [(lambda n : (self.ALPHABET.find(c)-key) % len(self.ALPHABET))(c) for c in encr_msg]
        logger.debug(f"decrypted nums :: {num_decr}")

        # now converting into decrypted string
        decr_chr = [(lambda decr_ch : self.ALPHABET[n])(n) for n in num_decr]
        decr_msg = ''.join(decr_chr)

        return decr_msg

if __name__ == '__main__':
    caesar_cipher = CaesarCipher()
    message = 'Cryptography is fun'
    key = 7
    encrypted_msg = caesar_cipher.encrypt(message, key)
    logger.debug(f'encrypted_msg :: {encrypted_msg}')

    decrypted_msg = caesar_cipher.decrypt(encrypted_msg, key)
    logger.debug(f'decrypted message :: {decrypted_msg}')
    
    result = False
    if decrypted_msg == message.upper():
        result = True

    logger.debug(f' verification of string :: {result}') 
