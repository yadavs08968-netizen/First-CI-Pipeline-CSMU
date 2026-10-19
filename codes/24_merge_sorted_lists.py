"""Program 24: Merge two sorted lists."""


def merge_sorted_lists(list1, list2):
    """Return a new sorted list containing elements from both sorted lists."""
    merged = []
    i = 0
    j = 0

    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            merged.append(list1[i])
            i += 1
        else:
            merged.append(list2[j])
            j += 1

    while i < len(list1):
        merged.append(list1[i])
        i += 1

    while j < len(list2):
        merged.append(list2[j])
        j += 1

    return merged


if __name__ == "__main__":
    first = list(map(int, input("Enter the first sorted list: ").split()))
    second = list(map(int, input("Enter the second sorted list: ").split()))
    print("Merged list:", merge_sorted_lists(first, second))