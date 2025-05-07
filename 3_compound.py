
def compound_interest(amount, rate, years):
    for year in range(years):
        amount = amount + amount*rate 
    return amount

def unit_test():
    assert compound_interest(0, 0, 0) == 0
    assert compound_interest(1000, 0, 0) == 1000
    assert compound_interest(1000, 0.05, 0) == 1000
    assert compound_interest(1000, 0.05, 1) == 1050
    assert compound_interest(1000, 0.05, 2) == 1102.5
    assert compound_interest(1000, 0.05, 3) == 1157.625



    print("Alle unit tests passed")


unit_test()