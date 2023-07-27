from atbash import AtbashCipher
from long_live_the_caeser import CaesarCipher
from vigenere import VigenereCipher
from enigma import SimpleEnigmaCipher


class CipherRunner:
    @staticmethod
    def run():
        try:
            # Atbash
            a = input("Plain text: ")
            if not isinstance(a, str):
                raise ValueError("Input must be a string")
            print("Encrypted text: " + AtbashCipher.encrypt(a))
            print("Decrypted text: " + AtbashCipher.decrypt(AtbashCipher.encrypt(a)))
            print()

            # Caesar
            key = input("Key: ")
            if not key.isdigit():
                raise ValueError("Key must be an integer")
            key = int(key)
            caesar_cipher = CaesarCipher(key)
            a = input("Plain text: ")
            if not isinstance(a, str):
                raise ValueError("Input must be a string")
            print("Encrypted text: " + caesar_cipher.encrypt(a))
            print("Decrypted text: " + caesar_cipher.decrypt(caesar_cipher.encrypt(a)))
            print()

            # Vigenere
            key = [1, 3, 2]
            vigenere_cipher = VigenereCipher(key)
            print("Key " + str(key))
            a = input("Plain text: ")
            if not isinstance(a, str):
                raise ValueError("Input must be a string")
            print("Encrypted text: " + vigenere_cipher.encrypt(a))
            print("Decrypted text: " + vigenere_cipher.decrypt(vigenere_cipher.encrypt(a)))
            print()

            # Enigma
            key = ('bcdefghijklmnopqrstuvwxyza', 'qwertyuioplkjhgfdsazxcvbnm', 'zxcvbnmlkjhgfdsaqwertyuiop')
            enigma_cipher = SimpleEnigmaCipher(key)
            print("Key " + key[0] + "\n" + key[1] + "\n" + key[2])
            a = input("Plain text: ")
            if not isinstance(a, str):
                raise ValueError("Input must be a string")
            print("Encrypted text: " + enigma_cipher.encrypt(a))
            print("Decrypted text: " + enigma_cipher.decrypt(enigma_cipher.encrypt(a)))
        except ValueError as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    CipherRunner.run()
