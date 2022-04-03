import src.utils.data_types as data_types


def sort_by_instance(to_sort: list, instance: object) -> int:
    matching = []
    other = []
    for obj in to_sort:
        if isinstance(obj, instance):
            matching.append(obj)
        else:
            other.append(obj)
    return matching, other


def quicksort_on_score(array: dict, key="score"):
    if len(array) < 2:
        return array

    low, same, high = [], [], []

    pivot = array[int(len(array) / 2)]

    for item in array:
        if item[key] < pivot[key]:
            low.append(item)
        elif item[key] == pivot[key]:
            same.append(item)
        elif item[key] > pivot[key]:
            high.append(item)

    return quicksort_on_score(low) + same + quicksort_on_score(high)


def sort_tile_distance(tile_layers):
    scores = []
    for z, layer in enumerate(tile_layers):
        for y, row in enumerate(layer.data):
            for x in range(len(row)):
                scores.append({"score": x + y + z, "pos": data_types.Point(x, y, z)})

    return [d["pos"] for d in quicksort_on_score(scores)]
