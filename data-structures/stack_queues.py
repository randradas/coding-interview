from collections import deque

def process_with_stack(numbers):
    """Return a list items read from a stack"""

    l = deque()
    result = []

    for n in numbers:
        l.append(n)

    while len(l) > 0:
        result.append(l.pop())

    return result


def process_with_queue(numbers):
    """Return a list items read from a queue"""

    l = deque()
    result = []

    for n in numbers:
        l.append(n)

    while len(l) > 0:
        result.append(l.popleft())

    return result


def main(numbers):
    stack_result = process_with_stack(numbers)
    queue_result = process_with_queue(numbers)

    print("original: %s" % (numbers))
    print("stack_result: %s" % (stack_result))
    print("queue_result: %s" % (queue_result))


if __name__ == "__main__":
    main([123,123112,1123123,112311123123,1121,1,1,2,4,5,3,1,2,3,1,1,2,3,4,6,69,76,76,78,78,78,4545])