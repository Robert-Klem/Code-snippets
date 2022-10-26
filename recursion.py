n = 6
def factorial(num: int) -> int:
    """
    Function: receive number, return factorial of that number
    """
    facto = 1
    for i in range(1, num + 1 ):
        facto = facto * i
        print(facto) #Kontrola mezivysledku

    return facto

print(f"Iterative:", factorial(n))


def factorial_recursion(num: int) -> int:
    if num > 1:
        return num * factorial_recursion(num - 1)
    else:
        return 1

print(f'Recursive: = {factorial_recursion(n)}')