class Solution:
    def encode(self, strs):
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + "#" + s
        return encoded

    def decode(self, encoded):
        res = []
        i = 0
        while i < len(encoded):
            j = i
            while encoded[j] != "#":
                j += 1
            length = int(encoded[i:j])
            res.append(encoded[j+1 : j+1+length])
            i = j + 1 + length
        return res

