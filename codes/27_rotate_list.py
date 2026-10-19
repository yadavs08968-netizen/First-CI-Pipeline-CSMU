
"""Program 27: Rotate a list by k positions."""


def rotate_list(items, k):
    """Return a new list rotated right by k positions."""
    if not items:
        return []

    k = k % len(items)

    return items[-k:] + items[:-k] if k != 0 else items.copy()
