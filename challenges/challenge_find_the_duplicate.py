def merge_sort(numbers):
    if len(numbers) <= 1:
        return numbers

    mid = len(numbers) // 2
    left = merge_sort(numbers[:mid])
    right = merge_sort(numbers[mid:])
    return merge(left, right)


def merge(left, right):
    merged = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged += left[i:]
    merged += right[j:]
    return merged


def find_duplicate(nums):
    if (
        not isinstance(nums, list)
        or not all(isinstance(num, int) for num in nums)
        or any(num < 0 for num in nums)
    ):
        return False

    seen = set()

    for num in nums:
        if num in seen:
            return num
        seen.add(num)

    return False
