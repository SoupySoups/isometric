import src.utils.data_types as data_types
import math


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


def sort_tile_distance(tile_layers, insert=[]):
    layers = []
    belows = []
    aboves = []
    for z, layer in enumerate(tile_layers):
        scores = []
        for y, row in enumerate(layer.data):
            for x, tile in enumerate(row):
                scores.append(
                    {
                        "score": x + y,
                        "data": {"position": data_types.Point(x, y, z), "object": tile},
                    }
                )

        for obj in insert:
            obj_3d = obj.threeD_point
            obj_z = math.floor(obj_3d.z)
            if obj_z == z:
                scores.append(
                    {
                        "score": obj_3d.x + obj_3d.y,
                        "data": {
                            "position": data_types.Point(obj_3d.x, obj_3d.y, obj_3d.z),
                            "object": obj,
                        },
                    }
                )
            elif obj_z < 0:
                belows.append(
                    {
                        "score": obj_3d.x + obj_3d.y,
                        "data": {
                            "position": data_types.Point(obj_3d.x, obj_3d.y, obj_3d.z),
                            "object": obj,
                        },
                    }
                )
            elif obj_z > len(tile_layers):
                aboves.append(
                    {
                        "score": obj_3d.x + obj_3d.y,
                        "data": {
                            "position": data_types.Point(obj_3d.x, obj_3d.y, obj_3d.z),
                            "object": obj,
                        },
                    }
                )

        layers += [d["data"] for d in quicksort_on_score(scores)]

    return belows + layers + aboves
