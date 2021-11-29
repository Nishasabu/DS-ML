list1 = [5, 10, 15, 20, 25, 30]
list2 = [2, 4, 6, 8, 10, 12]
print ( " Python Original list 1: " + str (list1))
print ( "Python Original list 2: " + str (list2))
result = []
for x in range (0, len (list1)):
    result.append( list1[x] + list2[x])
print ( " Addition of the list list1 and list2 is: " + str (result))
