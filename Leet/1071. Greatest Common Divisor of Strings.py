# 1071. Greatest Common Divisor of Strings
# For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t 
# (i.e., t is concatenated with itself one or more times).

# Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.
class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        l1 = len(str1)
        l2 = len(str2)
        def is_gcd(str):
            return (str1 == str*(l1//len(str)) and str2 == str*(l2//len(str)))
        if str1+str2 != str2+str1:
            return ""
        l_min = min(l1,l2)
        for i in range(l_min,0,-1):
            print(i)
            if l1%(i)==0 and l2%(i)==0 :
                if is_gcd(str1[:i]):
                    return str1[:i]
        return ""
    
    def gcdOfStrings2(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        def gcd(a, b):
            while b:
                a, b = b, a % b  # Euclidean algorithm
            return a
            
        if str1 + str2 != str2 + str1:
            return ""

        gcd_length = gcd(len(str1), len(str2))
        return str1[:gcd_length]
    
str1 ="AAAA"
str2 ="AAA"
sol = Solution()
print(sol.gcdOfStrings(str1, str2))