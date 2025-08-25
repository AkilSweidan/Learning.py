x = float(input("enter the first number : "))
y = float(input("enter the second number : "))
z = float(x) + float(y)
print(x , end = " ")
print(" + " , end = " ")
print(y , end= " ")
print("= " , end = " ")
print(f"{z: ,}")
print("Round form : " , end = " ")
print(round(z))


def sqFirst():
    print("The sqauer of the first number is : " , sqaure(float(x)))


def sqSecond():
    print("The sqauer of the Second number is : " , sqaure(float(y)))



def main():
    print("The sqaure of the sum is  : " , sqaure(z))


def sqaure(n):
    return pow(n , 2)


sqFirst()
sqSecond()
main()