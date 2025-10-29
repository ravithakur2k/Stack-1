# Time is O(n) -> To iterate and to remove from the stack(technically O(2n)
# Space is O(1) -> Auxiliary space

# The intuition is to use a stack data structure in a monotonically decreasing fashion. Once we find a temperature greater than the one on top of the stack we can calculate the difference
# and update the result array

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                popped = stack.pop()
                result[popped] = i - popped
            stack.append(i)

        return result