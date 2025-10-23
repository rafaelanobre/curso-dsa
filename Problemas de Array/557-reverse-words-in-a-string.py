# LeetCode 557 - Reverse Words in a String III

class Solution:
    def reverse_words(self, s) -> str:
        res = ''
        l,r = 0, 0

        while r < len(s):
            if s[r] != ' ':
                r += 1
            else:
                res += s[l:r][::-1] + ' '
                r += 1
                l = r
        res += s[l:r][::-1]
        return res

print(Solution().reverse_words('Hello World'))
print(Solution().reverse_words("Let's take LeetCode contest"))



