# Time is O(n) -> To iterate and to remove from the stack(technically O(2n)
# Space is O(1) -> Auxiliary space

# The intuition is to use a monotonically decreasing stack and once we find a greater element then update the result array with that as long as its value is greater than
# all the values at the top of the stack
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        visit = set()
        n = len(nums)
        result = [-1] * n
        stack = []
        for i in range(2 * n):
            if i >= n:
                i = i % n
            while stack and nums[i] > nums[stack[-1]]:
                popped = stack.pop()
                result[popped] = nums[i]
            if (nums[i], i) not in visit:
                visit.add((nums[i], i))
                stack.append(i)

        return result