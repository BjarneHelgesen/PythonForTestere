#name = input("What's your name?")
#print("Hello", name)

def calculate(tall_1, tall_2, operator):
    if operator == "+":
        return tall_1 + tall_2
    if operator == "-":
        return tall_1 - tall_2
    if operator == "*":
        return tall_1 * tall_2
    if operator == "/":
        return tall_1 / tall_2
    
    return "Invalid operator"

def unit_test():
    # Test the calculate function with some test cases
    assert calculate(1, 2, "+") == 3
    assert calculate(5, 3, "-") == 2
    assert calculate(2, 3, "*") == 6
    assert calculate(6, 2, "/") == 3.0
    print("All test cases passed")

unit_test()
tall_1 = int(input("Tall 1:"))
tall_2 = input("Tall 2:")
tall_2 = int(tall_2)
operator = input("Operator:")
result = calculate(tall_1, tall_2, operator)
print("Result:", result)


