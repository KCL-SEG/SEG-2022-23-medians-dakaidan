"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""
def median(numbers):
    try:
        numbers.sort()
        length = len(numbers)
        if len(numbers) % 2 == 0:
            return (numbers[length // 2] + numbers[length // 2 - 1]) / 2
        else:
            return numbers[length // 2]
    except TypeError:
        print("Please enter a list of numbers.")
        return None



while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break

print(numbers)
print("The median is", median(numbers))