def factorial(x):
    
    """This is a recursive function
    to find the factorial of an integer"""

    if x == 1:
        return 1 
    else:
        # recursive call to the function
        return (x * factorial(x-1))

num = int(input("Enter a number: "))
result = factorial(num)

def sum_fact(result):
    strr = str(result)
    list_res = list(map(int, strr.strip()))
    return sum(list_res)

print("The sum of digits in", num,"! is", sum_fact(result))
