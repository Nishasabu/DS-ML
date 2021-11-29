n = int (input("how many  fiboncci number you want:"))

n1, n2 = 0, 1
i = 0
if n < 0:
   print("you entered a negative number")
elif n == 1:
     print("fibonacci sequence:" , n1)
else:
    print("fibonacci sequence")
    while i < n:
        print(n1)
        nth = n1 + n2

        n1 = n2
        n2  = nth
        i += 1