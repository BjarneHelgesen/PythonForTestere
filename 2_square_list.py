
def square_list(numbers):
    squares = []
    for i in numbers:
        squares.append( i*i) 
    return squares

numbers = [1,2,3,4,5,6]

for i in numbers:
    print(i)
numbers[1] = 20

print(square_list(numbers))

ofte_brukt = range(5)
for i in ofte_brukt:
    print(i)