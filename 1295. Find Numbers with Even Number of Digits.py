'''
Find Numbers with Even Number of Digits

Given an array nums of integers, return how many of them contain an even number of digits.
 

Example 1:

Input: nums = [12,345,2,6,7896]
Output: 2
Explanation: 
12 contains 2 digits (even number of digits). 
345 contains 3 digits (odd number of digits). 
2 contains 1 digit (odd number of digits). 
6 contains 1 digit (odd number of digits). 
7896 contains 4 digits (even number of digits). 
Therefore only 12 and 7896 contain an even number of digits.
Example 2:

Input: nums = [555,901,482,1771]
Output: 1 
Explanation: 
Only 1771 contains an even number of digits.
 

Constraints:

1 <= nums.length <= 500
1 <= nums[i] <= 10^5
   Hide Hint #1  
How to compute the number of digits of a number ?
   Hide Hint #2  
Divide the number by 10 again and again to get the number of digits.


Leetcode Python Solution 1 :
'''

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return sum(len(str(num))%2==0 for num in nums)

# Complexity: time complexity is O(n^2)


#Leetcode Python Solution 2 :

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        sum = 0
        for item in nums:
            if ((item >= 10) and (item <= 99)) \
            or ((item >= 1000) and (item <= 9999)) \
            or (item == 100000) :
                sum += 1
        
        return sum

# Complexity: time complexity is O(n)

#Leetcode Python Solution 3:
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count=0
        for i in range(len(nums)):
            if len(str(nums[i])) % 2 == 0:
                count=count+1


        return count
# Complexity: time complexity is O(n^2)