# Two Pointers: Start-End

# def find_pair(nums, target):
#     # brute force method
#     # length = len(nums)

#     # for i in range(0, length):
#     #     j = i + 1
#     #     for j in range(0, length):
#     #         current_sum = nums[i] + nums[j]
#     #         if current_sum == target:
#     #             return [nums[i], nums[j]]
#     # return None

#     # two pointer method
#     left = 0
#     right = len(nums) - 1

#     while left < right:
#         if nums[left] + nums[right] == target:
#             return [nums[left], nums[right]]
#         elif nums[left] + nums[right] < target:
#             left += 1
#         else:
#             right -= 1
#     return None

# nums1 = [1, 3, 6, 7, 8, 12]
# target1 = 14
# print(find_pair(nums1, target1))

# nums2 = [2, 6, 8, 10]
# target2 = 17
# print(find_pair(nums2, target2))

# Two Pointers: Anchor-Runner

# def move_ones(nums):
    # brute force method
    # idx = 0
    # counter = 0

    # while counter < len(nums):
    #     if nums[idx] == 1:
    #         nums.remove(nums[idx])
    #         nums.append(1)
    #     else:
    #         idx += 1
    #     counter += 1
    # return nums

    # anchor runner method
    # [1, 2, 1, 4, 8]
    # iteration 1
    # anchor = 0, runner = 0
        # runner points to 1 so increment runner to 1
    # [1, 2, 1, 4, 8]
    # iteration 2
    # anchor = 0, runner = 1
        # runner points to 2 so runner swaps with anchor pointing to 1
        # increment anchor and runner by 1
    # [2, 1, 1, 4, 8]
    # iteration 3
    # anchor = 1, runner = 2
        # runner points to 1 so increment runner by 1
    # anchor = 1, runner = 3
        # runner points to 4 so runner swaps with anchor pointing to 1
        # increment anchor and runner by 1
    # [2, 4, 1, 1, 8]
    # iteration 4
    # anchor = 2, runner = 4
        # runner points to 8 so runner swaps with anchor at 1
        # anchor and runner increment by 1
    # [2, 4, 8, 1, 1]
    # iteration 5
    # anchor = 3, runner = 5
    # runner has reached the end of the array, so the iteration is complete
    # anchor = 0
    # runner = 0
    # while runner < len(nums):
    #     if nums[runner] == 1:
    #         runner += 1
    #     else:
    #         nums[anchor], nums[runner] = nums[runner], nums[anchor]
    #         anchor += 1
    #         runner += 1
    # return nums

    # reader writer variant
#     reader = 0
#     writer = 0
#     while reader < len(nums):
#         if nums[reader] == 1:
#             reader += 1
#         else:
#             nums[writer] = nums[reader]
#             writer += 1
#             reader += 1
    
#     while writer < len(nums):
#         nums[writer] = 1
#         writer += 1
    
#     return nums

# nums1 = [1, 2, 1, 4, 8]
# print(move_ones(nums1)) # [2, 4, 8, 1, 1]

# nums = [1, 2, 1, 4, 8], counter = 0, length = 5
# first iteration, nums[0] == 1
    # remove 1, [2, 1, 4, 8]
    # append 1, [2, 1, 4, 8, 1]
    # increment counter to 1
# nums = [2, 1, 4, 8, 1], counter = 1, length = 5
# second iteration, nums[0] == 2
    # increment idx to 1
    # increment counter to 2
# nums = [2, 1, 4, 8, 1], idx = 1, counter = 2, length = 5
# third iteration, nums[1] == 1
    # remove 1, [2, 4, 8, 1]
    # append 1, [2, 4, 8, 1, 1]
    # increment counter to 3
# nums = [2, 4, 8, 1, 1], idx = 1, counter = 3, length = 5
# fourth iteration, nums[1] == 4
    # increment idx to 2
    # increment counter to 4
# nums = [2, 4, 8, 1, 1], idx = 2, counter = 4, length = 5
# fifth iteration, nums[2] == 8
    # increment idx to 3
    # increment counter to 5
# nums = [2, 4, 8, 1, 1], idx = 3, counter = 5, length = 5
# sixth iteration, counter == length so the while loop exits
# return [2, 4, 8, 1, 1]

# --- Function Definition (Requires Implementation) ---

def reverseConsonants(s: str) -> str:
    
    # "HELLO"
    # VOWELS = 'aeiouAEIOU'
    # result = ''
    # reverse_consonants = ''

    # for char in s[::-1]:
    #     if char not in VOWELS:
    #         reverse_consonants += char
    # print(reverse_consonants)

    # length = len(reverse_consonants)
    # consonant_index = 0
    # for char in s:
    #     if char not in VOWELS:
    #         if consonant_index < length:
    #             result += reverse_consonants[consonant_index]
    #             consonant_index += 1
    #     else:
    #         result += char
    
    # return result
   
    VOWELS = 'aeiouAEIOU'
    left = 0
    right = len(s) - 1
    result = ''
    while left <= len(s) - 1:
        if s[left] not in VOWELS and s[right] in VOWELS:
            right -= 1
        elif s[left] not in VOWELS and s[right] not in VOWELS:
            result += s[right]
            left += 1
            right -= 1
        else:
            result += s[left]
            left += 1
    print("result: ", result)
    
    return result

# --- Test Cases ---

# Test Case 1: Empty string
assert reverseConsonants("") == "", 'Test Case 1 Failed: Empty string'

# Test Case 2: Single consonant
assert reverseConsonants("s") == "s", 'Test Case 2 Failed: Single consonant'

# Test Case 3: All caps word
assert reverseConsonants("HELLO") == "LELHO", 'Test Case 3 Failed: All caps word'

# Test Case 4: Mixed case word
assert reverseConsonants("leetcode") == "deectole", 'Test Case 4 Failed: Mixed case word 1'

# Test Case 5: Word with vowels and consonants
assert reverseConsonants("example") == "elapmxe", 'Test Case 5 Failed: Word with vowels and consonants'

# Test Case 6: Word starting and ending with consonant
assert reverseConsonants("Consonants") == "sotnonasnC", 'Test Case 6 Failed: Word starting/ending with consonant'

# If all assertions pass (after you implement the function), print a success message
print("All test cases passed!")