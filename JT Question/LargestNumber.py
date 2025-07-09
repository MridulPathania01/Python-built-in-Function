# leetcode "Largest Number"
from typing import List
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        v = [str(num) for num in nums]
        v.sort(key=lambda a: a * 10, reverse=True)
        if v[0] == "0":
            return "0"
        return "".join(v)