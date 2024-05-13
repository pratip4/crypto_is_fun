# implementation of One Time PAD (OTP) Symmetric allgorithm

from random import randint
from loguru import logger

class OneTimePad():
    def __init__(self):
        self.ALPHABET = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    def random_secret_key(self, key_length):
        range_start = 10**(key_length - 1)
        range_end = (10**key_length) - 1

        return randint(range_start, range_end)

    def encrypt(self, msg, key):
        msg = msg.upper()
        cipher_text = ''

        for index, char in enumerate(msg):
            # the value with which we shift the given letter
            key_value = str(key)[index]

            cipher_text += self.ALPHABET[(self.ALPHABET.find(char) + int(key_value)) % len(self.ALPHABET)]

        return cipher_text

    def decrypt(self, msg, key):
        msg = msg.upper()
        cipher_text = ''

        for index, char in enumerate(msg):
            # the value with which we shift the given letter
            key_value = str(key)[index]

            cipher_text += self.ALPHABET[(self.ALPHABET.find(char) - int(key_value)) % len(self.ALPHABET)]

        return cipher_text


if __name__ == '__main__':
    otp = OneTimePad()
    msg = 'I am testing OTP cipher'
    key = otp.random_secret_key(len(msg))
    encr_msg = otp.encrypt(msg, key)
    logger.debug(f"encrypted message :: {encr_msg}")

    decr_msg = otp.decrypt(encr_msg, key)
    logger.debug(f"decrypted message is :: {decr_msg}")
