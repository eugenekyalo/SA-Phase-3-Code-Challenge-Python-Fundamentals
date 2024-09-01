# Function to add two numbers
def add_numbers(num1, num2):
    """
    Returns the sum of num1 and num2.
    """
    return num1 + num2

# Function to check if a number is even
def is_even(number):
    """
    Returns True if the number is even, otherwise False.
    """
    return number % 2 == 0

# Function to reverse a string
def reverse_string(text):
    """
    Returns the reversed version of the input string.
    """
    return text[::-1]

# Function to count the number of vowels in a string
def count_vowels(text):
    """
    Returns the count of vowels (a, e, i, o, u) in the input string, 
    ignoring case sensitivity.
    """
    vowels = 'aeiou'
    return sum(1 for char in text.lower() if char in vowels)

# Function to calculate the factorial of a non-negative integer
def calculate_factorial(n):
    """
    Returns the factorial of the input non-negative integer n.
    The factorial of n is the product of all positive integers less than or equal to n.
    """
    if n == 0:
        return 1
    else:
        return n * calculate_factorial(n - 1)

# Decorator function to print a message before calling the original function
def decorator_func(func):
    """
    A decorator function that prints "Decorator Applied" before calling the original function.
    """
    def wrapper(*args, **kwargs):
        print("Decorator Applied")
        return func(*args, **kwargs)
    return wrapper

# Function to apply a decorator to a given function
def apply_decorator(func):
    """
    Applies the decorator_func to the provided function.
    """
    decorated_func = decorator_func(func)
    return decorated_func

# Function to sort a list of tuples by the second element (age)
def sort_by_age(lst):
    """
    Sorts a list of tuples by the second element (age) in ascending order.
    """
    return sorted(lst, key=lambda x: x[1])

# Function to merge two dictionaries, summing values for common keys
def merge_dicts(dict1, dict2):
    """
    Merges two dictionaries into one. If there are common keys, their values are summed up.
    """
    merged = dict1.copy()
    for key, value in dict2.items():
        if key in merged:
            merged[key] += value
        else:
            merged[key] = value
    return merged

# Class to represent a Car with make, model, and year
class Car:
    def __init__(self, make, model, year):
        """
        Initializes a new Car instance with make, model, and year attributes.
        """
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        """
        Prints the car's make, model, and year.
        """
        print(f"Make: {self.make}, Model: {self.model}, Year: {self.year}")
