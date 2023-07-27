class SimpleEnigmaCipher:
    def __init__(self, keys):
        if not isinstance(keys, tuple) or len(keys) != 3 or not all(isinstance(key, str) and len(key) == 26 for key in keys):
            raise ValueError("Keys must be a tuple of three 26-character strings")
        self.keys = keys

    @staticmethod
    def meramdenea_aso(letter):
        if not isinstance(letter, str) or len(letter) != 1:
            raise ValueError("Input must be a single character")
        if letter.islower():
            return ord(letter) % 97
        elif letter == "A":
            return 42
        elif letter.isalpha():
            return -(ord(letter) % 65)
        else:
            raise ValueError("Invalid character for meramdenea_aso")

    def encrypt(self, text):
        if not isinstance(text, str):
            raise ValueError("Input text must be a string")
        for i in range(3):
            key = self.keys[i]
            try:
                text = ''.join(
                    key[self.meramdenea_aso(letter)] if (a := self.meramdenea_aso(letter)) >= 0 and a != 42
                    else key[0].capitalize() if a == 42
                    else key[-a].capitalize() if letter.isalpha()
                    else letter
                    for letter in text
                )
            except IndexError:
                raise ValueError("Key indexing error during encryption")
        return text

    def decrypt(self, text):
        if not isinstance(text, str):
            raise ValueError("Input text must be a string")
        for i in range(3):
            key = self.keys[2 - i]
            key_dic_pat = {key[j]: chr(97 + j) for j in range(26)}
            key_dic_did = {key[j].capitalize(): chr(65 + j) for j in range(26)}
            text = ''.join(
                key_dic_pat.get(char, char) if char.islower()
                else key_dic_did.get(char, char) if char.isupper()
                else char
                for char in text
            )
        return text
