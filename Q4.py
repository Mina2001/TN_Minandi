def sort_dict_by_values(d):
    return dict(sorted(d.items(), key=lambda item: item[1]))

print(sort_dict_by_values({'a': 3, 'b': 1, 'c': 2}))  # Output: {'b': 1, 'c': 2, 'a': 3}
