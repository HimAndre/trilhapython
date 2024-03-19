list = [1,"py",[40,30,33,54,75]]

l2 = list.copy()
print(list)

print(id(l2), id(list))
#comprovação que é realizado a copia da list contudo é atribuido um novo id.

l2[0] = 2 

print(l2)
print(list)
