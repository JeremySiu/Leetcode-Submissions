class Solution:
    def valid_char (self, s, counter):
        ascii = ord(s[counter])
        if (ascii >= 48 and ascii <= 57) or (ascii >= 97 and ascii <= 122):
            return True
        else:
            return False
        
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        left_counter = 0;
        right_counter = len(s) - 1
        while left_counter < right_counter:
            while self.valid_char(s, left_counter) == False:
                if left_counter < len(s) - 1:
                    left_counter += 1
                else: 
                    return True
            while self.valid_char(s, right_counter) == False:
                if right_counter > 0:
                    right_counter -= 1
                else:
                    return True
            if ord(s[left_counter]) != ord(s[right_counter]):
                return False
            left_counter += 1
            right_counter -= 1
        return True
            
