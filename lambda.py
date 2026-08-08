# For me weird shit, but kinda interesting
# Lambda functions

x = lambda a : a + 10
print(x(5))

def lamd_func(n):
    return lambda a : a ** n

square_num = lamd_func(2)

print(f"Square is: {square_num(3)}")
