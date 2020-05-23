def merge_sort(items: list):
    if len(items) <= 1:
        return

    n = len(items) // 2
    left_side = items[:n]
    right_side = items[n:]
    merge_sort(left_side)
    merge_sort(right_side)
    i = 0
    j = 0
    k = 0
    while i < len(left_side) and j < len(right_side):
        if left_side[i] < right_side[j]:
            items[k] = left_side[i]
            i += 1
        else:
            items[k] = right_side[j]
            j += 1
        k += 1
    while i < len(left_side):
        items[k] = left_side[i]
        k += 1
        i += 1
    while j < len(right_side):
        items[k] = right_side[j]
        k += 1
        j += 1


def hoar_sort(items):
    if len(items) <= 1:
        return

    barrier = items[0]
    left_list = list()
    equals_list = list()
    right_list = list()
    for item in items:
        if item < barrier:
            left_list.append(item)
        elif item > barrier:
            right_list.append(item)
        else:
            equals_list.append(item)
    hoar_sort(left_list)
    hoar_sort(right_list)

    united_list = left_list + equals_list + right_list
    for i, item in zip(range(len(united_list)), united_list):
        items[i] = item
    print(items)


def insert_sort(items: list):
    n = len(items)
    for top in range(1, n):
        k = top
        while k > 0 and items[k] < items[k - 1]:
            items[k], items[k - 1] = items[k - 1], items[k]
            k -= 1


def bubble_sort(items):
    n = len(items)
    for i in range(1, n):
        for j in range(0, n - i):
            if items[j] > items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j]


def choice_sort(items: list):
    n = len(items)
    for i in range(0, n - 1):
        for j in range(i + 1, n):
            if items[i] > items[j]:
                items[i], items[j] = items[j], items[i]


def shell_sort(items: list):
    increment = len(items) // 2


def test(sort):
    items = [6, 12, 9, 4, 11, 3, 15, 2, 7, 13, 1, 5, 14, 8, 10, 0]
    sorted_items = list(range(16))
    sort(items)
    print("Test passed" if sorted_items == items else "Error")


if __name__ == "__main__":
    test(bubble_sort)
    test(insert_sort)
    test(choice_sort)
    test(merge_sort)
    test(hoar_sort)
