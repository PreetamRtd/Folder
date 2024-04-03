import prg
import time 

def bubble_sort(arr):
  n = len(arr)

  for i in range(n):
    # Last i elements are already in place
    for j in range(0, n-i-1):
      if arr[j] > arr[j+1] :
        arr[j], arr[j+1] = arr[j+1], arr[j]


def selection_sort(arr):
  n = len(arr)

  for i in range(n):
    min_idx = i
    for j in range(i+1, n):
      if arr[min_idx] > arr[j]:
        min_idx = j
        
    arr[i], arr[min_idx] = arr[min_idx], arr[i]

# Driver code  
arr = [64, 25, 12, 22, 11]
selection_sort(arr)

print("Sorted array:", arr)

z = int(input("enter how many arr"))
x = []
timearr = []
for i in range(z):
    x.append(i)
    arr = prg.gen()
    print(arr)
    start = time.time()
    selection_sort(arr) # your function
    end = time.time()
    print("afte",arr)
    timetaken = end - start
    timearr.append(timetaken)
prg.plot(x,timearr)
print('h')





