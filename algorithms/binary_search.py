def main(data, search):
    left = 0
    right = len(data) - 1
    pivot = (left + right) / 2

    while left != right:
        print("left: %d" % (left))
        print("right: %d" % (right))
        print("pivot: %d" % (pivot))

        if data[pivot] == search:
            return "Searched item is at position %s" % (pivot)

        elif search < data[pivot]:
            print("position %d is not %d" % (pivot, search))
            if left != pivot:  #when search is at index 0, right is not moved.
                right = pivot

            pivot = (left + right) / 2

        elif search > data[pivot]:
            print("position %d is not %d" % (pivot, search))
            if left == pivot:
                pivot = right #when search is at index len(data)-1, left is not moved.
            else:
                left = pivot
                pivot = (left + right) / 2

if __name__ == "__main__":
    search = 12345
    data = [1,2,3,4,5,6,7,8,9,12,13,14,15,17,18,19,123,1234,12345]
    result = main(data, search)

    print result