def per(acc, arr):
    if len(arr) == 0:
        result.append(acc)
        return

    for idx in range(len(arr)):
        new = arr[idx]
        arr[idx], arr[-1] = arr[-1], arr[idx]
        per(acc + [new], arr[:-1])
        arr[idx], arr[-1] = arr[-1], arr[idx]

result = []
per([], [1, 2, 3])
