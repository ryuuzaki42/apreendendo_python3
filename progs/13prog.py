
print("Print val betwen A and B")
a = int(input("Value of A: "))
b = int(input("Value of B: "))

while a <= b:
    print(a)
    a += 1

print("Print AGV betwen N number")
count = int(input("Count of number: "))

total = 0
i = 1
while i <= count:
    #val = int(input("Value of B: ", i)) # TypeError: input expected at most 1 argument, got 2
    val = int(input("Value of {}: ".format(i)))

    total += val
    i += 1

media = total / count
print("Media:", media)
