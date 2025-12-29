# Remove duplicates from a list while preserving the original order.

# Example
# Input:  [10, 20, 10, 30, 20, 40]
# Output: [10, 20, 30, 40]

def remove_duplicates(numbers):
    unique_nums = []
    for  num in numbers:
        if num not in unique_nums:
            unique_nums.append(num)
    return unique_nums

def second_largest_num(numbers):
    largest = float('-inf')
    second_largest = float('-inf')

    for  num in numbers:
        if num > largest :
            second_largest = largest
            largest = num
        # elif largest > num and num > second_largest:
        elif largest > num > second_largest:
            second_largest = num

    return second_largest

nums =  [10]
print(second_largest_num(nums))

list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
# Output: [3, 4]
def find_common_elements(list1, list2):
    set_list = set(list2)
    result = []
    for num in list1:
        if num in set_list:
            result.append(num)
    return result

print(find_common_elements(list1, list2))

input = [1, 2, 2, 3, 3, 3]

def count_frequency(numbers):
    frequency_dict = {}
    for num in numbers:
        if num in frequency_dict:
            frequency_dict[num] = frequency_dict[num]+1
        else:
            frequency_dict[num] = 1
    return frequency_dict

print(count_frequency(input))