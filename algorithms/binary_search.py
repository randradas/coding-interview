#!/usr/bin/env python3


def main(dataset, item):
    left = 0
    right = len(dataset) - 1
    pivot = (left + right) / 2

    while left != right:
        print("left: %d" % left)
        print("right: %d" % right)
        print("pivot: %d" % pivot)

        if dataset[pivot] == item:
            return "item is at position %s" % (pivot)

        elif item < dataset[pivot]:
            print("position %d is not %d" % (pivot, item))
            if left != pivot:  # when item is at index 0, right is not moved.
                right = pivot

            pivot = (left + right) / 2

        elif item > dataset[pivot]:
            print("position %d is not %d" % (pivot, item))
            if left == pivot:
                pivot = right  # when item is at index len(dataset)-1, left is not moved.
            else:
                left = pivot
                pivot = (left + right) / 2


if __name__ == "__main__":
    wanted = 12345
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 13, 14, 15, 17, 18, 19, 123, 1234, 12345]
    result = main(data, wanted)
    print(result)
