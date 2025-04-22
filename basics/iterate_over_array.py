from collections import deque, Counter, namedtuple, defaultdict

# from pyarrow import DictionaryArray
# from pydantic.v1.schema import default_ref_template

# Dictionaries are similar to java hashmap
# Sets are similar to java hashset
# Lists are similar to ArrayList
# tuples in python are immutable list

# deque can be used for both purposes , 
# linkedlist (because it efficient in adding and removing elements) and stack

# for stack use cases we can use both list and deque

# arr = [2, 3, 4, 1, 6, 5]
arr = [5, 4, 3, 2, 1]

for i in range(len(arr)):
    print(arr[i])


print("even numbers")
for i in arr:
    if i % 2 == 0:
        print(i)

# sort without sort method
# bubble
def sort_array(arr: list): 
    n = len(arr)
    for i in range(0, n) :
        for j in range(0, n-1):
            if arr[j] > arr[j+1]:
                x = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = x
            
    for x in arr :
        print(x)

# sort_array(arr)

#arr.sort()
# for i in range(4):
#     print(arr[i])

# binary search

def binary_search(arr:list, x:int) :
    start = 0
    end = len(arr)-1
    while start <= end :
        mid = (start+end)//2

        if (arr[mid] == x): return True

        elif (arr[mid] > x): # go left part
            end = mid-1
        else:
            start = mid+1

    return False


print(binary_search(arr, 1))


# find largest element in the given array

def largest_number(arr: list) :

    n = len(arr)
    max = 0
    for i in range(0, n) :
        if arr[i] > max:
            max = arr[i]

    return max

print("largest number : ")
print(largest_number(arr))

# Second larges number

def second_largest_number(arr: list) :

    n = len(arr)

    if n < 2 :  return None
    max = float('-inf')
    sec_max = float('-inf')
    for i in range(0, n-1) :
        if arr[i] > max:
            sec_max = max
            max = arr[i]

        elif arr[i] > arr[i+1] and arr[i] != max:
            sec_max = arr[i+1]
        

        # elif arr[i]


    return sec_max if sec_max != float('-inf') else None

print("second largest number")
print(second_largest_number(arr))


# find kth largest number using quick select


# sort colors

arr1 = [1, 1, 2, 2 , 0]

# def _sort_colors(arr : list) -> list:




    
# Return unique number
def return_unique_no(arr1: list) -> int :
    unique_no = 0
    dict = {}

    for i in arr1 :
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1

    for key, value in dict.items():
        if value == 1:
            print(key)
    # unique_no = [i for num, count in dict.items() if count == 1]
    return unique_no


print(return_unique_no(arr1))

# while loop in python

while True:
    s=input("Enter something: or ('quite' to exit)")
    if s == 'quite':
        break
    print(f"you entered: {s}")


cnt = 0

while cnt < 10:
    cnt+=1
    if cnt%2 == 0:
        continue
    print(cnt)








