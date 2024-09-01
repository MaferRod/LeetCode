class Solution(object):
    def permute(self, nums):
        n = len(nums)
        output, temp = [], []

        if not nums:
            return 0

        def dfs():
            if len(temp) == n:
                output.append(temp[:])
                return

            for num in nums:
                if num not in temp:
                    temp.append(num)
                    dfs()
                    temp.pop()
        dfs()
        return output

        