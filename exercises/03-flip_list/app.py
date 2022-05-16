arr = [45, 67, 87, 23, 5,  32, 60]

#your code below:

#arr.sort(reverse = True)
new_list = []
x = 0

for i in range(len(arr),0,-1):
    new_list.append(arr[i-1])
    

print(new_list)
#print("list inicial:"+arr)
#print("list final:"+new_list)