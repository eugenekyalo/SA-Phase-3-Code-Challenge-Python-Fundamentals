from solutions import add_numbers, is_even, reverse_string, count_vowels, calculate_factorial, sort_by_age, merge_dicts, Car

# Test add_numbers
print(f"add_numbers(5, 3) = {add_numbers(5, 3)}")  # Expected: 8
print(f"add_numbers(-1, 1) = {add_numbers(-1, 1)}")  # Expected: 0

# Test is_even
print(f"is_even(4) = {is_even(4)}")  # Expected: True
print(f"is_even(5) = {is_even(5)}")  # Expected: False

# Test reverse_string
print(f"reverse_string('hello') = {reverse_string('hello')}")  # Expected: 'olleh'
print(f"reverse_string('') = {reverse_string('')}")  # Expected: ''

# Test count_vowels
print(f"count_vowels('hello') = {count_vowels('hello')}")  # Expected: 2
print(f"count_vowels('HELLO') = {count_vowels('HELLO')}")  # Expected: 2

# Test calculate_factorial
print(f"calculate_factorial(5) = {calculate_factorial(5)}")  # Expected: 120
print(f"calculate_factorial(0) = {calculate_factorial(0)}")  # Expected: 1

# Test sort_by_age
print(f"sort_by_age([('Alice', 30), ('Bob', 25)]) = {sort_by_age([('Alice', 30), ('Bob', 25)])}")  # Expected: [('Bob', 25), ('Alice', 30)]

# Test merge_dicts
print(f"merge_dicts({{'a': 1}}, {{'a': 2, 'b': 3}}) = {merge_dicts({'a': 1}, {'a': 2, 'b': 3})}")  # Expected: {'a': 3, 'b': 3}

# Test Car class
car = Car("Toyota", "Corolla", 2020)
car.display_info()  # Expected output: Make: Toyota, Model: Corolla, Year: 2020
