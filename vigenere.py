class VigenereCipher:
    def __init__(self, shift_list):
        if not isinstance(shift_list, list) or not all(isinstance(i, int) for i in shift_list):
            raise ValueError("Shift list must be a list of integers")
        self.shift_list = shift_list
        self.key_dic = {".": ",", ",": ".", "!": "?", "?": "!", "0": "1", "1": "0",
                        "2": "3", "3": "2", "4": "5", "5": "4", "6": "7", "7": "6",
                        "8": "9", "9": "8"}

    def encrypt(self, text):
        if not isinstance(text, str):
            raise ValueError("Input text must be a string")
        anban = [chr(i) for i in range(97, 123)]
        did_anban = [chr(i) for i in range(65, 91)]
        try:
            return ''.join(
                anban[(ord(text[i]) - 97 + self.shift_list[i % len(self.shift_list)]) % 26]
                if text[i].islower()
                else did_anban[(ord(text[i]) - 65 + self.shift_list[i % len(self.shift_list)]) % 26]
                if text[i].isupper()
                else self.key_dic.get(text[i], text[i])
                for i in range(len(text))
            )
        except (IndexError, KeyError):
            raise ValueError("Error encountered during Vigenere encryption")

    def decrypt(self, text):
        if not isinstance(text, str):
            raise ValueError("Input text must be a string")
        anban = [chr(i) for i in range(97, 123)]
        did_anban = [chr(i) for i in range(65, 91)]
        try:
            return ''.join(
                anban[(ord(text[i]) - 97 - self.shift_list[i % len(self.shift_list)]) % 26]
                if text[i].islower()
                else did_anban[(ord(text[i]) - 65 - self.shift_list[i % len(self.shift_list)]) % 26]
                if text[i].isupper()
                else self.key_dic.get(text[i], text[i])
                for i in range(len(text))
            )
        except (IndexError, KeyError):
            raise ValueError("Error encountered during Vigenere decryption")
