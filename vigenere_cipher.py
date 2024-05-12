# Vigenere Cipher is another Symmetric or Private key encryption, that was used in 16th century.
# This technique was considered as the most invisible encryption algorithm in the 16th Century, till it was cracked by Kaminski algorithm / technique in the 19th century.
# In this python class I will try to do encryption using Vigenere technique and then decrypt it.
# Assumption: Assuming there is only upper-case alphabet and space in key & message for simplicity.
from loguru import logger

class VigenereCipher():
    def __init__(self):
        self.ALPHABET = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    # encryption formulae = (x + k) % len(ALPHABET)
    def encrypt(self, msg, key) -> str :
        msg = msg.upper()
        key = key.upper()
        encr_list = []
        encr_msg = ''
        key_len = len(key)
        key_list = [ch for ch in key]
        key_index = 0
        for ch in msg:
            # get numerical value of each character of the message
            msg_n = self.ALPHABET.find(ch)
            
            # logger.debug(f"char is {ch} numeric value is {msg_n}")
            # associate a character of key to each char of message. 
            # Hence finding the numerical value of the respective key char
            key_n = self.ALPHABET.find(key_list[key_index])
            # logger.debug(f"key-char is {key_list[key_index]} and its numeric value is {key_n}")
            # Once all the chars of the secret key is assigned once, restart from the begining of the secret key phrase. Hence set key_index as 0.
            key_index += 1
            if key_index == key_len:
                key_index = 0

            encr_n = (msg_n + key_n) % len(self.ALPHABET)
            encr_ch = self.ALPHABET[encr_n]
            encr_list.append(encr_ch)

        # so we have a list of characters. We just need to join them to form the encrypted string
        # logger.debug(f"the final list is {encr_list}")
        encr_msg = ''.join(encr_list)
        return encr_msg

    # decryption formulae = (x - k) % len(ALPHABET)
    def decrypt(self, msg, key) -> str :
        msg = msg.upper()
        key = key.upper()
        decr_list = []
        decr_msg = ''
        key_len = len(key)
        key_list = [ch for ch in key]
        key_index = 0
        for ch in msg:
            # get numerical value of each character of the message
            msg_n = self.ALPHABET.find(ch)
            
            # logger.debug(f"char is {ch} numeric value is {msg_n}")
            # associate a character of key to each char of message. 
            # Hence finding the numerical value of the respective key char
            key_n = self.ALPHABET.find(key_list[key_index])
            # logger.debug(f"key-char is {key_list[key_index]} and its numeric value is {key_n}")
            # Once all the chars of the secret key is assigned once, restart from the begining of the secret key phrase. Hence set key_index as 0.
            key_index += 1
            if key_index == key_len:
                key_index = 0

            decr_n = (msg_n - key_n) % len(self.ALPHABET)
            decr_ch = self.ALPHABET[decr_n]
            decr_list.append(decr_ch)

        # so we have a list of characters. We just need to join them to form the decrypted string
        # logger.debug(f"the final list is {decr_list}")
        decr_msg = ''.join(decr_list)
        return decr_msg

if __name__ == '__main__':
    vc = VigenereCipher()
    msg = 'Hi I am testing Vigenere Cipher'
    key = 'CIPHERKEY'
    encrypted_msg = vc.encrypt(msg, key)
    logger.debug(f'encrypted string is :: {encrypted_msg}')

    # lets try decrypting it
    decrypted_msg = vc.decrypt(encrypted_msg, key)
    logger.debug(f'decrypted string is :: {decrypted_msg}')
            



