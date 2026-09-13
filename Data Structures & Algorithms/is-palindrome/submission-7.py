class Solution:
    def isPalindrome(self, s: str) -> bool:
        chars=list(s)
        strings=[]
        for ch in chars:
            if ch.isalnum():
                strings.append(ch.lower())
            else:
                pass
        
        string="".join(strings)
        if string==string[::-1]:
            return True
        else:
            return False

        