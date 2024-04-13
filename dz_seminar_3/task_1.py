# Дан список повторяющихся элементов. 
# Вернуть список с дублирующимися элементами. 
# В результирующем списке не должно быть дубликатов.


def get_duplicates(input_list):
    seen = set()
    duplicates = set()
    
    for item in input_list:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
    
    return list(duplicates)

input_list = [1, 2, 2, 3, 4, 4, 5, 2, 2]
duplicates_list = get_duplicates(input_list)
print(duplicates_list)