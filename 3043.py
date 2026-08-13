class Solution(object):
    def longestCommonPrefix(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: int
        """
        st = set()
        for num in arr1:
            while num and num not in st:
                st.add(num)
                num //= 10
        ans = -1
        for num in set(arr2):
            while num:
                if num in st:
                    ans = max(ans, num)
                    break
                num //= 10
        return 0 if ans == -1 else len(str(ans))