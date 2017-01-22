"""
Goal: implement and test quicksort

@see CLRS v3 book page 171
@date: 2017-01-21
@author: Andrei Sura
"""

def partition(data, p, right):
    print("\n==> Enter partition: p={}, right={}".format(p, right))
    pivot = data[right]
    print("pivot = data[{}] = {}".format(right, pivot))

    i = p - 1  # this is a dangerous line

    for j in range(p, right):
        print("j: {}".format(j))
        if data[j] <= pivot:
            i = i + 1
            print("new i: {}".format(i))
            print("swap: {} <-> {}".format(data[i], data[j]))
            data[i], data[j] = data[j], data[i]

    print("swap2: {} <-> {}".format(data[i + 1], data[right]))
    data[i + 1], data[right] = data[right], data[i + 1]
    return i + 1


def quick_sort(data, left, right):
    if left < right:
        pivot = partition(data, left, right)
        quick_sort(data, left, pivot - 1)
        quick_sort(data, pivot + 1, right)

data = [2, 8, 7, 1, 3, 5, 6, 4]

print("Input array: {}".format(data))
quick_sort(data, 0, len(data) - 1)
print("Output array: {}".format(data))
