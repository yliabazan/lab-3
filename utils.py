# utils.py

def calculate_factorial(n):
    """
    Calculate the factorial of a given number.

    Parameters:
    - n (int): The number for which factorial is to be calculated.

    Returns:
    - int: The factorial of the given number.
    """
    if n == 0 or n == 1:
        return 1
    else:
        return n * calculate_factorial(n - 1)

def is_prime(number):
    """
    Check if a given number is prime.

    Parameters:
    - number (int): The number to be checked for primality.

    Returns:
    - bool: True if the number is prime, False otherwise.
    """
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def is_power_of_5(number):
    """
    Check if a given number is a power of 5.

    Parameters:
    - number (int): The number to be checked.

    Returns:
    - bool: True if the number is a power of 5, False otherwise.
    """
    if number <= 0:
        return False
    while number % 5 == 0:
        number //= 5
    return number == 1

def is_power_of_2(number):
    """
    Check if a given number is a power of 2.

    Parameters:
    - number (int): The number to be checked.

    Returns:
    - bool: True if the number is a power of 2, False otherwise.
    """
    if number <= 0:
        return False
    while number % 2 == 0:
        number //= 2
    return number == 1
