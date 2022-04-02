def sort_by_instance(to_sort: list, instance: object) -> int:
    matching = []
    other = []
    for obj in to_sort:
        if isinstance(obj, instance):
            matching.append(obj)
        else:
            other.append(obj)
    return matching, other
