import math


# 1. Given an array, find the average of all contiguous subarrays of size ‘K’ in it.
def find_averages_of_subarrays_brute_force(K, arr):
    result = []
    for i in range(len(arr) - K + 1):
        _sum = 0.0
        for j in range(i, i + K):
            _sum += arr[j]
        result.append(_sum / K)
    return result


def find_averages_of_subarrays_sliding_window(K, arr):
    result = []
    windowSum, windowstart = 0.0, 0
    for windowEnd in range(len(arr)):
        windowSum += arr[windowEnd]

        if windowEnd >= K - 1:
            result.append(windowSum / K)
            windowSum -= arr[windowstart]
            windowstart += 1

    return result


# 2. Given an array of positive numbers and a positive number ‘k,’ find the maximum sum of any contiguous subarray of
# size ‘k’.
def max_sub_array_of_size_k_brute_force(k, arr):
    max_sum = 0
    window_sum = 0

    for i in range(0, len(arr) - k + 1):
        window_sum = 0
        for j in range(i, k + i):
            window_sum += arr[j]
        max_sum = max(max_sum, window_sum)

    return max_sum


# Time Complexity#
# The time complexity of the above algorithm will be O(N).
#
# Space Complexity#
# The algorithm runs in constant space O(1).
def max_sub_array_of_size_k_sliding_window(k, arr):
    windowSum, windowStart, maxsum = 0, 0, 0
    for windowEnd in range(len(arr)):
        windowSum += arr[windowEnd]

        if windowEnd >= k - 1:
            maxsum = max(maxsum, windowSum)
            windowSum -= arr[windowStart]
            windowStart += 1

    return maxsum


# 3. Smallest Subarray with a given sum
# Given an array of positive numbers and a positive number ‘S,’ find the length
# of the smallest contiguous subarray whose sum is greater than or equal to ‘S’. Return 0 if no such subarray exists.

# Time Complexity
# The time complexity of the above algorithm will be O(N). The outer for loop runs for all
# elements, and the inner while loop processes each element only once; therefore, the time complexity of the
# algorithm will be O(N+N), which is asymptotically equivalent to O(N).
def smallest_subarray_with_given_sum(s, arr):
    window_start, window_end = 0, 0
    window_sum = 0
    min_subarr_len = math.inf

    for window_end in range(len(arr)):
        window_sum += arr[window_end]

        while window_sum >= s:
            min_subarr_len = min(min_subarr_len, window_end - window_start + 1)
            window_sum -= arr[window_start]
            window_start += 1
    if min_subarr_len == math.inf:
        return 0
    return min_subarr_len


# 4. Longest Substring with maximum K Distinct Characters (medium)
# Given a string, find the length of the longest substring in it with no more than K distinct characters.

# Time Complexity
# The above algorithm’s time complexity will be O(N), where NN is the number of characters in the
# input string. The outer for loop runs for all characters, and the inner while loop processes each character only
# once; therefore, the time complexity of the algorithm will be O(N+N), which is asymptotically equivalent to
# O(N).
# Space Complexity
# The algorithm’s space complexity is O(K), as we will be storing a maximum of K+1 characters in the HashMap.
def longest_substring_with_k_distinct(str1, k):
    window_end, window_start = 0, 0
    char_frequency = {}
    max_length = 0

    for window_end in range(len(str1)):
        right_char = str1[window_end]
        if right_char not in char_frequency:
            char_frequency[right_char] = 0
        char_frequency[right_char] += 1

        while len(char_frequency) > k:
            left_char = str1[window_start]
            char_frequency[left_char] -= 1
            if char_frequency[left_char] == 0:
                del char_frequency[left_char]
            window_start += 1
        max_length = max(max_length, window_end - window_start + 1)
    return max_length


# 5. Fruits into Baskets (medium)
# Given an array of characters where each character represents a fruit tree,
# you are given two baskets, and your goal is to put maximum number of fruits in each basket. The only restriction is
# that each basket can have only one type of fruit.

# Time Complexity
# The above algorithm’s time complexity will be O(N), where ‘N’ is the number of characters in
# the input array. The outer for loop runs for all characters, and the inner while loop processes each character only
# once; therefore, the time complexity of the algorithm will be O(N+N), which is asymptotically equivalent to
# O(N).

# Space Complexity
# The algorithm runs in constant space O(1)O(1) as there can be a maximum of three types of fruits
# stored in the frequency map.
def fruits_into_baskets(fruits):
    window_end, window_start = 0, 0
    fruit_frequency = {}
    max_length = 0

    for window_end in range(len(fruits)):
        right_char = fruits[window_end]
        if right_char not in fruit_frequency:
            fruit_frequency[right_char] = 0
        fruit_frequency[right_char] += 1

        while len(fruit_frequency) > 2:
            left_char = fruits[window_start]
            fruit_frequency[left_char] -= 1
            if fruit_frequency[left_char] == 0:
                del fruit_frequency[left_char]
            window_start += 1
        max_length = max(max_length, window_end - window_start + 1)
    return max_length


# 6: Longest Substring with at most 2 distinct characters
# Given a string, find the length of the longest substring in it with at most two distinct characters.
def longest_substring_at_most_2_distinct_characters(str_1):
    window_end, window_start = 0, 0
    char_frequency = {}
    max_length = 0

    for window_end in range(len(str_1)):
        right_char = str_1[window_end]
        if right_char not in char_frequency:
            char_frequency[right_char] = 0
        char_frequency[right_char] += 1

        while len(char_frequency) > 2:
            left_char = str_1[window_start]
            char_frequency[left_char] -= 1
            if char_frequency[left_char] == 0:
                del char_frequency[left_char]
            window_start += 1
        max_length = max(max_length, window_end - window_start + 1)
    return max_length


# 7. Longest Substring with Distinct Characters (hard)
# Given a string, find the length of the longest substring, which has all distinct characters.

# Time Complexity
# The above algorithm’s time complexity will be O(N), where ‘N’ is the number of characters in the input string.

# Space Complexity
# The algorithm’s space complexity will be O(K)


def non_repeat_substring(str1):
    window_start = 0
    max_length = 0
    char_index_map = {}

    for window_end in range(len(str1)):
        right_char = str1[window_end]

        if right_char in char_index_map:
            window_start = max(window_start, char_index_map[right_char] + 1)

        char_index_map[right_char] = window_end
        max_length = max(max_length, window_end - window_start + 1)
        return max_length


if __name__ == '__main__':
    # 7
    print("Length of the longest substring: " + str(non_repeat_substring("aabccbb")))
    print("Length of the longest substring: " + str(non_repeat_substring("abbbb")))
    print("Length of the longest substring: " + str(non_repeat_substring("abccde")))

    # 6
    print("Length of the longest substring: " + str(longest_substring_at_most_2_distinct_characters("araaci")))
    print("Length of the longest substring: " + str(longest_substring_at_most_2_distinct_characters("cbbebi")))
    print("Length of the longest substring: " + str(longest_substring_at_most_2_distinct_characters("aaaa")))
    print("Length of the longest substring: " + str(longest_substring_at_most_2_distinct_characters("abcd")))

    # 5
    print("Maximum number of fruits: " + str(fruits_into_baskets(['A', 'B', 'C', 'A', 'C'])))
    print("Maximum number of fruits: " + str(fruits_into_baskets(['A', 'B', 'C', 'B', 'B', 'C'])))

    # 4
    print("Length of the longest substring: " + str(longest_substring_with_k_distinct("araaci", 2)))
    print("Length of the longest substring: " + str(longest_substring_with_k_distinct("araaci", 1)))
    print("Length of the longest substring: " + str(longest_substring_with_k_distinct("cbbebi", 3)))
    # 3
    print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 3, 2])))
    print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 8])))
    print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(8, [3, 4, 1, 1, 6])))

    # 2
    print("Maximum sum of a subarray of size K: " + str(max_sub_array_of_size_k_sliding_window(3, [2, 1, 5, 1, 3, 2])))
    print("Maximum sum of a subarray of size K: " + str(max_sub_array_of_size_k_sliding_window(2, [2, 3, 4, 1, 5])))

    print("Maximum sum of a subarray of size K: " + str(max_sub_array_of_size_k_brute_force(3, [2, 1, 5, 1, 3, 2])))
    print("Maximum sum of a subarray of size K: " + str(max_sub_array_of_size_k_brute_force(2, [2, 3, 4, 1, 5])))

    # 1
    result = find_averages_of_subarrays_sliding_window(5, [1, 3, 2, 6, -1, 4, 1, 8, 2])
    print(f"Averages of subarrays of size K: {result}")

    result = find_averages_of_subarrays_brute_force(5, [1, 3, 2, 6, -1, 4, 1, 8, 2])
    print(f"Averages of subarrays of size K: {result}")
