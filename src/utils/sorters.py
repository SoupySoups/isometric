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
    behinds = []
    aboves = []
    unused = insert
    # Sort inbounds objects
    for z, layer in enumerate(tile_layers):
        scores = (
            []
        )  # Will store each object with a score representing distance from camera
        # Calculate tile scores
        for y, row in enumerate(layer.data):
            for x, tile in enumerate(row):
                scores.append(
                    {
                        "score": x + y,
                        "data": {"position": data_types.Point(x, y, z), "object": tile},
                    }
                )

        # Calculate object scores if they are within map bounds
        for obj in insert:
            obj_3d = obj.threeD_point
            if math.floor(obj_3d.z) == z:
                scores.append(
                    {
                        "score": obj_3d.x + obj_3d.y,
                        "data": {
                            "position": data_types.Point(obj_3d.x, obj_3d.y, obj_3d.z),
                            "object": obj,
                        },
                    }
                )
                unused.remove(obj)

        # Sort scores
        layers += [d["data"] for d in quicksort_on_score(scores)]

    # Sort out of bounds objects
    for obj in unused:
        obj_3d = obj.threeD_point
        if obj_3d.x < 0 or obj_3d.y < 0 or obj_3d.z < 0:
            behinds.append(
                {
                    "score": obj_3d.x + obj_3d.y,
                    "data": {
                        "position": data_types.Point(obj_3d.x, obj_3d.y, obj_3d.z),
                        "object": obj,
                    },
                }
            )
        else:
            aboves.append(
                {
                    "score": obj_3d.x + obj_3d.y,
                    "data": {
                        "position": data_types.Point(obj_3d.x, obj_3d.y, obj_3d.z),
                        "object": obj,
                    },
                }
            )

    # Combine out of bounds objects with in bounds objects
    layers = (
        [d["data"] for d in quicksort_on_score(behinds)]
        + layers
        + [d["data"] for d in quicksort_on_score(aboves)]
    )

    return layers
