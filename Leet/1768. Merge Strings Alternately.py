# 1768. Merge Strings Alternately
# You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, 
# starting with word1. If a string is longer than the other, append the additional letters onto the end 
# of the merged string.

# Return the merged string.

class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """

        new_word = ""
        len_1 = len(word1)
        len_2 = len(word2)
        min_len = min(len_1, len_2)

        for i in range(min_len):
            new_word = new_word + word1[i]
            new_word = new_word + word2[i]

        if len_1 > min_len:
            new_word = new_word + word1[min_len:]
        else:
            new_word = new_word + word2[min_len:]
        
        return new_word
    
class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        li = []
        i,j=0,0
        while i<len(word1) and i<len(word2):
            li.append(word1[i])
            li.append(word2[j])
            i+=1
            j+=1
        li.append(word1[i:]) if i<len(word1) else li.append(word2[j:])
        return ''.join(li)