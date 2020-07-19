# 给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。 
# 
#  说明：本题中，我们将空字符串定义为有效的回文串。 
# 
#  示例 1: 
# 
#  输入: "A man, a plan, a canal: Panama"
# 输出: true
#  
# 
#  示例 2: 
# 
#  输入: "race a car"
# 输出: false
#  
#  Related Topics 双指针 字符串 
#  👍 246 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 去掉字符串中的空格和符号等多余内容,并返回颠倒后的字符串
        # 时间复杂度O(n)，空间复杂度O(n)
        def deleteNullAndSigh(s):
            newStr = ''
            for i in s:
                if i.isdigit() or i.isalpha():
                    newStr += i.lower()
            Str = newStr[::-1]
            if newStr == Str:
                # 比较新旧字符串是否相同
                return True
            else:
                return False
        return deleteNullAndSigh(s)


    def isPalindrome_2(self):
        # 使用指针的方法，从字符首尾往内部靠近，实时比较
        # 时间复杂度O(n)，空间复杂度O(1)
        def isPalindrome(self, s: str) -> bool:
            i, j = 0, len(s) - 1
            while i < j:
                if not (s[i].isdigit() or s[i].isalpha()):
                    i += 1
                    continue
                if not (s[j].isdigit() or s[j].isalpha()):
                    j -= 1
                    continue
                if s[i].lower() != s[j].lower():
                    return False
                else:
                    i += 1
                    j -= 1
            return True


# leetcode submit region end(Prohibit modification and deletion)
