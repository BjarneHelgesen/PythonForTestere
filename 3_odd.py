
def odd_number(n):
    if n % 2 == 0:
        return False
    return True

def odd(lst):
    oddetall = []
    for number in lst:
        if number % 2 == 1:
            oddetall.append(number)

    return oddetall


def unit_test():
    assert odd_number(0) == False
    assert odd_number(1) == True
    assert odd([]) == []
    assert odd([1]) == [1]
    assert odd([2]) == []
    assert odd([1, 2]) == [1]
    assert odd([1, 2, 3]) == [1, 3]
    print("all unit tests passed")

unit_test()
        