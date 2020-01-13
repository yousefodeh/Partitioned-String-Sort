import re
def partition(arr,low,high): 
    i = ( low-1 )        
    pivot = arr[high]      
    for j in range(low , high):   
        if   arr[j] < pivot:   
            i = i+1 
            arr[i],arr[j] = arr[j],arr[i] 
    arr[i+1],arr[high] = arr[high],arr[i+1] 
    return ( i+1 ) 
def quickSort(arr,low,high): 
    if low < high:     
        pi = partition(arr,low,high)     
        quickSort(arr, low, pi-1) 
        quickSort(arr, pi+1, high) 
def split(word): 
    return [char for char in word]  
def escape_commas(obj):
        return re.sub(',', '', str(obj))
x=[]
input1=[]
out=[]


with open('input.txt') as f:
    content = f.readlines()
input1 = [x.strip() for x in content] 

for i in range(len(input1)):
    z=[]
    x.append(re.split('(\d+)', input1[i]))
    for i in range(len(x[0])):
        z.append(split(x[0][i]))
    for i in range(len(x[0])):
          n = len(z[i]) 
          quickSort(z[i],0,n-1) 
    list1 = [x for x in z if x != []] 
    joined = ''.join(''.join(map(escape_commas, row)) for row in list1)
    x=[]
    out.append(joined)

with open('my-output.txt', 'w') as f:
    for item in out:
        f.write("%s\n" % item)   



