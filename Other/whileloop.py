# input
a = int(input("Input a:"))
b = int(input("Input b:"))

while a<=b:
    if a%5 == 0:
        print("break!")
        break
    print(a, end = " ")
    a += 1 # a = a + 1
print("end")