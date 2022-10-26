#A simple calculator to do basic operators

def solver():
    try:
        problem = input('Please enter problem you want to solve: ' )
        separated =problem.split()
        number_1 = int(separated[0])
        operator = separated[1]
        number_2 = int(separated[2])
        if operator == "+":
            return number_1 + number_2
        elif operator == "-":
            return number_1 - number_2
        elif operator == "*":
            return number_1 * number_2
        else:
            return number_1 / number_2
    except BaseException as e:
        print(e)
        return f'Try it again. The correct input is: int "operator" int'
