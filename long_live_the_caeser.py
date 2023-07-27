class CaesarCipher:
    def __init__(self, shift):
        if not isinstance(shift, int):
            raise ValueError("Shift must be an integer")
        self.shift = shift
        self.key_dic = self.create_key_dic()
        self.reverse_key_dic = {v: k for k, v in self.key_dic.items()}

    def create_key_dic(self):
        key_dic = {chr(97 + i): chr(97 + (i + self.shift) % 26) for i in range(26)}
        key_dic.update({chr(65 + i): chr(65 + (i + self.shift) % 26) for i in range(26)})
        key_dic.update({".": ",", ",": ".", "!": "?", "?": "!", "0": "1", "1": "0",
                        "2": "3", "3": "2", "4": "5", "5": "4", "6": "7", "7": "6",
                        "8": "9", "9": "8"})
        return key_dic

    def encrypt(self, text):
        if not isinstance(text, str):
            raise ValueError("Input text must be a string")
        try:
            return ''.join(self.key_dic.get(char, char) for char in text)
        except KeyError:
            raise ValueError("Invalid character encountered during Caesar encryption")

    def decrypt(self, text):
        if not isinstance(text, str):
            raise ValueError("Input text must be a string")
        try:
            return ''.join(self.reverse_key_dic.get(char, char) for char in text)
        except KeyError:
            raise ValueError("Invalid character encountered during Caesar decryption")
