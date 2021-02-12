def dirReduc(arr):
    result = arr.copy()
    reductions = (
        ("NORTH", "SOUTH"),
        ("SOUTH", "NORTH"),
        ("EAST", "WEST"),
        ("WEST", "EAST")
    )

    for i in range(0, len(arr) - 1):
        # print("i:", i, "arr[i]:", arr[i])
        tup = (arr[i], arr[i + 1])

        if tup in reductions:
            # print("in reductions")
            i += 1
        else:
            result.append(arr[i])

    return result
