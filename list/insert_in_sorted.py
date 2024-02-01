# You are given a list of sorted "elements" and a number "num" to be inserted
# into this list such that the new list is also sorted in ascending order.
#
# Example:
# elements = [1,2,6,9], num = 3
# Output:
# [1,2,3,6,9]

# Time complexity: O(log n) where n=no. of elements in original list

class InsertInSorted:
    def insert(self, elements: list[int], num: int) -> list[int]:
        low, high = 0, len(elements)

        while low < high:
            mid = (low+high) // 2
            if num < elements[mid]:
                # num can be inserted at mid, so keep mid in further processing
                high = mid
            else:
                # num can be inserted only from (mid+1) onwards, so skip mid in further processing
                low = mid + 1

        return elements[:low] + [num] + elements[low:]


if __name__ == "__main__":
    inserter = InsertInSorted()
    print(inserter.insert([1,3,6,8,12], 3))
    print(inserter.insert([1,3,6,8,12], 8))
    print(inserter.insert([1,3,6,8,12], 7))
    print(inserter.insert([1,3,6,8,12], 9))
    print(inserter.insert([1,3,6,8,12], 1))
    print(inserter.insert([1,3,3,3,6,8,12], 3))
    print(inserter.insert([1,3,3,3,3,3,6,8,12], 3))
    print(inserter.insert([1,3], 2))
    print(inserter.insert([1], 2))
    print(inserter.insert([], 2))


# Approach 2 : Same time complexity but more lines

# num_elem = len(elements)
# if num_elem == 0:
#     return [num]
# if num <= elements[0]:
#     return [num] + elements
# if num >= elements[-1]:
#     return elements + [num]
#
# low, high = 0, num_elem
# while low <= high:
#     mid = (low + high) // 2
#     if num <= elements[mid] and mid-1>=0 and num >= elements[mid-1]:
#         return elements[:mid] + [num] + elements[mid:]
#     elif num > elements[mid] and mid+1<num_elem and elements[mid+1] > num:
#         return elements[:mid+1] + [num] + elements[mid+1:]
#     elif num < elements[mid]:
#         high = mid - 1
#     else:
#         low = mid + 1
