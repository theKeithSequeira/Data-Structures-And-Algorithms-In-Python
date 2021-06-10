from typing import List
import random

def bubble_sort(arr:List[int]):
    n:int=len(arr)
    swap_check:bool=False
    swap_count:int=0
    comp_count:int=0
    for pass_count in range(1,n):
        swap_check=False
        comp_count+=1
        for i in range(n-pass_count):
            if arr[i]>arr[i+1]:
                arr[i],arr[i+1]=arr[i+1],arr[i]
            swap_count+=1
            swap_check=True
        if swap_check is False:
            break
    
    print(f"Swap Count:{swap_count}, Comparison Count:{comp_count}")


num:int=int(input("Enter the number of elements:"))
print("The randomly generated elemnts are:")
arr:List[int]=random.sample(range(1,100),num)
print(arr)
bubble_sort(arr)
print("The elements now sorted by bubblesort are:")
print(arr)
