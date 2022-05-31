from bisect import bisect_left
from functools import total_ordering
from heapq import merge
@total_ordering
class Stack(list):
    def __lt__(self, other):
        return self[-1] < other[-1]
    def __eq__(self, other):
        return self[-1] == other[-1]
def patience_sort(collection: list) -> list:
    stacks = []
    # sort into stacks
    for element in collection:
        new_stacks = Stack([element])
        i = bisect_left(stacks, new_stacks)
        if i != len(stacks):
            stacks[i].append(element)
        else:
            stacks.append(new_stacks)
    # use a heap-based merge to merge stack efficiently
    collection[:] = merge(*[reversed(stack) for stack in stacks])
    return collection   
    
             
nums = [5, 9, 10, 3, -4, 5, 178, 92, 46, -18, 0, 7]
print("\nOriginal list:")
print(nums)
patience_sort(nums)
print("Sorted order is:", nums)