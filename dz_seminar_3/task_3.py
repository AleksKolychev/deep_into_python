# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения. 
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность. 
# Достаточно вернуть один допустимый вариант. 
# *Верните все возможные варианты комплектации рюкзака.


def fill_backpack(items, max_weight):
    n = len(items)
    item_set = [[set() for _ in range(max_weight + 1)] for _ in range(n + 1)]
    item_set[0][0] = {()}

    for i in range(1, n + 1):
        item_name, item_weight = items[i - 1]
        for w in range(max_weight + 1):
            if item_weight > w:
                item_set[i][w] = item_set[i - 1][w]
            else:
                for prev_set in item_set[i - 1][w]:
                    item_set[i][w].add(prev_set)
                for prev_set in item_set[i - 1][w - item_weight]:
                    new_set = prev_set + (item_name,)
                    item_set[i][w].add(new_set)

    return item_set[n][max_weight]

items = [
    ('Фонарик', 1),
    ('Палатка', 3),
    ('Одежда', 3),
    ('Спальный мешок', 2),
    ('Аптечка', 1),
    ('Еда', 4),
    ('Вода', 5)
]
max_weight = 5

result = fill_backpack(items, max_weight)
for r in result:
    print(r)
