def scratch(original_file: str, folder: list):
    result = []
    for audio in folder:
        result.append(f"{original_file} {audio}")
    return result

res = scratch('Room', [1, 2, 3, 4])
print(res)
