
#268. Missing Number
#Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.
#Time complexity = O(n)
#Space complexity = O(1)
#Run on leetcode = Yes
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # calculating sum n*(n+1)/2 
        expected_sum = len(nums)*(len(nums)+1)//2
        actual_sum = sum(nums)
        return expected_sum - actual_sum