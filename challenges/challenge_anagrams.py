def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result += left[i:]
    result += right[j:]

    return result


def is_anagram(first_string, second_string):
    # Convert strings to lowercase for case-insensitive comparison
    str1 = first_string.lower()
    str2 = second_string.lower()

    if first_string == '' and second_string == '':
        return ('', '', False)

    # Convert strings to sorted lists of characters
    sorted_str1 = merge_sort(str1)
    sorted_str2 = merge_sort(str2)

    # Compare the sorted lists of characters
    if sorted_str1 == sorted_str2:
        return ("".join(sorted_str1), "".join(sorted_str2), True)
    else:
        return ("".join(sorted_str1), "".join(sorted_str2), False)
