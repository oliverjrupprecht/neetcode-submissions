class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == [""]:
            return ""
        if strs == []:
           return "[]"
        out = []
        for string in strs:
            word = []
            for j in range(len(string)):
                word.append(str(self.get_key(string[j], 2)))
            out.append(".".join(word))
        

        return (" ".join(out))

    
    def get_key(self, ch : str, shift : int):
        length = 256
        return ord(ch) + (shift % length)

    def decode_char(self, i, shift):
        length = 256
        return chr((i + shift) % length)

    def decode(self, s: str) -> List[str]:
        if s == "":
            return [""]
        if s == "[]":
            return []
        recovered = s.split(" ")

        if s == "": return []

        decoded = []
        for word in recovered:
            wrd = []
            for char_id in word.split("."):
                if char_id == "": continue
                wrd.append(self.decode_char(int(char_id), -2))
            joined = "".join(wrd)
            decoded.append(joined)
        
        return decoded
        

