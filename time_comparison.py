from bisect import bisect_left
from functools import total_ordering
from heapq import merge
import time
from random import randint

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

def quick_sort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)

testList = []
for i in range(1000000):
    testList.append(randint(0,1000000))

testList2 = testList.copy()

start = time.time()
sortedList = quick_sort(testList)
end = time.time()
print("\nTime for quick_sort :")
print(end - start)

start2 = time.time()
sortedList = patience_sort(testList)
end2 = time.time()
print("\nTime for patience_sort :")
print(end2 - start2)

