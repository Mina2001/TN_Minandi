def squares_of_even_numbers(lst):
    return [x**2 for x in lst if x % 2 == 0]

# Example
print(squares_of_even_numbers([1, 2, 3, 4, 5]))