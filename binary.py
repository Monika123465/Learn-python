# example usage

# def binary_search(arr,target):
#     low,high=0 ,len(arr)-1

#     while low<=high:
#         mid=(low+high)//2
#         if  arr[mid]==target:
#             return mid
#         elif arr[mid]<target:
#             low=mid+1
#         else:
#             high=mid-1

#     return -1
    
      
      
      
      
      
# sorted_array=[1,2,3,4,5,6]
# target_value=6

# result=binary_search(sorted_array,target_value)

# if result!=-1:
#     print("target value {target_value} found at index {result}")

# else:
#     print("target value {target_value} not found in the array ")

def binary_search(arr, target):
        low, high = 0, len(arr) - 1
        while low <= high:
         mid = (low + high) // 2 # Calculate the middle index
         if arr[mid] == target:
            return mid # Target found, return the index
         elif arr[mid] < target:
           low = mid + 1 # Target is in the right half
         else:
           high = mid - 1 # Target is in the left hal
           return -1 # Target not found
# Example usage
sorted_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target_value = 6
result = binary_search(sorted_array, target_value)
if result != -1:
     print(f'Target value {target_value} found at index {result}.')
else:
     print(f'Target value {target_value} not found in the array.' )


mytuple=("apple","banana","cherry")
myit=iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))