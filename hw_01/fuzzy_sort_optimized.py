"""
Goal: implement and test the "fuzzy sorting" for intervals
Note: in comparison to the `fuzzy_sort.py` this "optimized"
     version uses the right end of the interval to reduce
     the "problem size" and achieve O(n) expected running
     time when all intervals overlap.

@see CLRS v3 book page 189
@date: 2017-01-21
@author: Andrei Sura
"""

class segment():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return "({}, {})".format(self.x, self.y)


def partition(data, left, right):
    print("\n==> Enter partition: left={}, right={}".format(left, right))
    pivot = data[right].x
    print("pivot = data[{}] = {}".format(right, pivot))

    i = left - 1  # this is a dangerous line

    for j in range(left, right):  # this is same as "for j = left to right-1"
        print("j: {}".format(j))
        if data[j].x <= pivot:
            i = i + 1
            print("new i: {}".format(i))
            print("swap: {} <-> {}".format(data[i], data[j]))
            data[i], data[j] = data[j], data[i]

    print("swap2: {} <-> {}".format(data[i + 1], data[right]))
    data[i + 1], data[right] = data[right], data[i + 1]

    adv = i + 1

    # extra loop to see how many additional elements we can "cover"
    # with the "right" end of the segment we just placed...
    for t in range(i + 1, right):
        if data[t].x <= data[i + 1].y:
            adv += 1
            print("Advance the pivot to {} because: x:{} <= y:{}"
                  .format(adv, data[t].x, data[i + 1].y))
            # data[t].x < data[i + 1].y))  # noqa
    return adv


def quick_sort(data, left, right):
    if left < right:
        pivot = partition(data, left, right)
        quick_sort(data, left, pivot - 1)
        quick_sort(data, pivot + 1, right)

data = [segment(5, 10),
        segment(3, 5),
        segment(4, 6),
        segment(1, 2),
        segment(2, 7)]

print("Input array: {}".format(data))
quick_sort(data, 0, len(data) - 1)
print("Output array: {}".format(data))
"""
Output array: [(1, 2), (2, 7), (4, 6), (5, 10), (3, 5)]
"""
