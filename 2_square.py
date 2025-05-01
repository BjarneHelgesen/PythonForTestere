
def square(x):
    return x*x

def unit_test():
    assert square(0) == 0
    assert square(1) == 1
    assert square(2) == 4
    assert square(-1) == 1
    print("All unit tests passed!")

unit_test()