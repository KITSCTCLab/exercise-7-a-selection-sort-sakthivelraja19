def selectionSort(array, size)->list:
   
    for i in range(0,size):
        smallest = array[i]
        for x in range(i+1,size):
            if array[i]>array[x]:
                smallest = x
                array[smallest],array[i] = array[i],array[smallest]
    return array
               
         
       

 

# Do not change the following code
input_data = input()
data = []
for item in input_data.split(', '):
  if item.isnumeric():
    data.append(int(item))
  elif item.lstrip("-").isnumeric():
    data.append(int(item))
print(selectionSort(data, len(data)))
