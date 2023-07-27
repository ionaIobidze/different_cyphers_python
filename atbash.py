class AtbashCipher:
    @staticmethod
    def encrypt(text):
        if not isinstance(text, str):
            raise ValueError("Input text must be a string")
        key_dic = {chr(97 + i): chr(122 - i) for i in range(26)}
        try:
            return ''.join(key_dic[char] if char in key_dic else char for char in text)
        except KeyError:
            raise ValueError("Invalid character encountered during Atbash encryption")

    @staticmethod
    def decrypt(text):
        if not isinstance(text, str):
            raise ValueError("Input text must be a string")
        key_dic = {chr(122 - i): chr(97 + i) for i in range(26)}
        try:
            return ''.join(key_dic[char] if char in key_dic else char for char in text)
        except KeyError:
            raise ValueError("Invalid character encountered during Atbash decryption")
