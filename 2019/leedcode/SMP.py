class Solution:
    def getNext(self, str):
        k = -1
        j = 0
        lenth = len(str)
        next = []
        next.append(-1)
        while j<lenth-1:
            if k == -1 or str[k] == str[j]:
                k += 1
                j += 1
                next.append(k)
            else:
                k = next[k]
        return next
    def strStr(self, haystack: str, needle: str) -> int:
        next = self.getNext(needle)
        i = 0
        j = 0
        slen = len(haystack)
        plen = len(needle)
        while(i<slen and j<plen):
            if j==-1 or haystack[i]==needle[j]:
                i+=1
                j+=1
            else:
                j = next[j]
        if j==plen:
            return i-j
        else:
            return -1



a = Solution()
print(a.strStr("assadadas", "ada"))