def rotate_by_one(arr):
    if len(arr) == 0:
        return arr
    first = arr.pop(0)
    arr.append(first)
    return arr