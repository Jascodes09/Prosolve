# two_sum_input.py

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        numToIndex = {}
        for i, num in enumerate(nums):
            if target - num in numToIndex:
                return [numToIndex[target - num], i]
            numToIndex[num] = i
        return []  # In case no solution is found

if __name__ == "__main__":
    # Get user input
    nums_input = input("Enter a list of numbers separated by spaces: ")
    target_input = input("Enter the target number: ")

    # Process input
    nums = list(map(int, nums_input.strip().split()))
    target = int(target_input)

    # Call the solution
    solution = Solution()
    result = solution.twoSum(nums, target)

    if result:
        print("Indices of numbers that add up to the target:", result)
    else:
        print("No two numbers add up to the target.")
