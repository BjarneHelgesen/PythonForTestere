def miles_to_km(miles):
    return miles * 1.6

def unit_test():
    assert miles_to_km(0) == 0
    assert miles_to_km(1) == 1.6
    assert miles_to_km(-1) == -1.6
    print("All unit tests passed")

unit_test()

miles = float(input("Enter distance in miles: "))
km = miles_to_km(miles)
print(miles, "miles is", km, "kilometers") 
