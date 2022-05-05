blocks = int(input("Enter the number of blocks: "))
height=0
counter=0
while(counter+height+1<=blocks):
    height+=1
    counter=counter+height
    
#
# Write your code here.
#	

print("The height of the pyramid:", height)
