def linear_search(arr, x):
  
  for i in range(len(arr)):
    if arr[i] == x:
      return i

  return -1

# Example usage  
arr = [20, 5, 7, 25, 10, 45, 50, 100] 
x = 25

result = linear_search(arr, x) 

if result != -1:
  print("Element found at index", result)
else:
  print("Element not found")