class Solution:
    def isPalindrome(self, s: str) -> bool:
        char_list = []
        for character in s:
            if character.isalpha() or character.isdigit():
                char_list.append(character.lower())
        # print(char_list)

        """
        0 -1
        1 -2
        2 -3
        
        """
        for i in range(len(char_list)//2):
            if char_list[i] != char_list[-(i+1)] :
                print('false')
                return False
        print('true')
        return True


sol = Solution()
sol.isPalindrome("A man, a plan, a canal: Panama")
sol.isPalindrome("race a car")
