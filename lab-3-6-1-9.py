my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
#
# Write your code here.
#
for i in range(len(my_list)):
    while(my_list[i] in my_list[i+1:]):
        print(my_list[i], " i: ", i)
        print("sub lista a comparar",my_list[i+1:], range(i+1,len(my_list)))
        print("index del elemento a eliminar: ",
              my_list[i+1:].index(my_list[i])+i+1)
        print("index del elemento a eliminar en la sublista: ",
              my_list[i+1:].index(my_list[i]))              
        del my_list[my_list[i+1:].index(my_list[i])+i+1]
        print("lista sin el elemento ya eliminado: ",my_list)
    if(i+1>=len(my_list)):
        break

print("The list with unique elements only:")
print(my_list)
