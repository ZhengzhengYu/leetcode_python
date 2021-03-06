"""
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

For example,
Given nums = [0, 1, 3] return 2.

Note:
Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?

"""
"""利用求和公式求解"""
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        return n * (n+1) / 2 - sum(nums)


"""二进制的思路
仍然利用两个相同的数的异或为0
"""

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = len(nums)
        for index,value in enumerate(nums):
            result ^= index
            result ^= value
        return result