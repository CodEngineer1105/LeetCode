class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lst = []
        ans = 0
        i=0
        while i<len(s):
            if s[i] in lst:
                ans=max(ans,len(lst))
                lst=lst[lst.index(s[i])+1:]
            lst.append(s[i])
            ans=max(ans,len(lst))
            i+=1
        return ans
