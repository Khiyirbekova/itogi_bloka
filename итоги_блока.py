def filter_strings(arr):
    new_arr = []
    for s in arr:
        if len(s) <= 3:
            new_arr.append(s)
    return new_arr

# Ввод массива строк
arr = input("Введите массив строк через запятую: ").split(", ")

result = filter_strings(arr)
print(result)
