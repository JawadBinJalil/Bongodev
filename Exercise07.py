def FizzBuzz(num):
    if num%3==0:
        return "Fizz"
    elif num%5==0:
        return "Buzz"
    elif num%3==0 and num%5==0:
        return "FizzBuzz"
    else:
        return "Not a Fizz-buzz number"
    
n=int(input())
Result=FizzBuzz(n)
print(Result)