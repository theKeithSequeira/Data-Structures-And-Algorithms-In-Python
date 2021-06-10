from typing import List
from random import sample

def insertion_sort(arr:List[int]):
    n:int=len(arr)
    for j in range(1,n):
        for i in range(j,0,-1):
            if arr[i-1] >arr[i]:
                arr[i],arr[i-1]=arr[i-1],arr[i]

num:int=int(input("Enter the number of elements:"))
arr=sample(range(1,100),num)
print(f"The randomly generated elements are: {arr}")
insertion_sort(arr)
print(f"The elements sorted by insertion sort are:{arr}")

