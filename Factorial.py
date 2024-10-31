def factorial1(n):
    if n == 0 :
        return 1
    else :
        return n * factorial1(n-1)
# We use this part to print
print(factorial1(3))
