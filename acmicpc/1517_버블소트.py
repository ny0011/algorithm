def merge(arr, arr_left, arr_right, count):
    i = j = k = 0
    
    while i < len(arr_left) and j < len(arr_right):
        if arr_left[i] <= arr_right[j]:
            arr[k] = arr_left[i]
            i += 1            
        else:
            arr[k] = arr_right[j]     
            move = len(arr_left) + j - k
            count.append(move)
            j +=1
        k+=1
    
    while i < len(arr_left):
        arr[k] = arr_left[i]
        i += 1
        k += 1
        
    while j < len(arr_right):
        arr[k] = arr_right[j]
        j += 1
        k += 1


def merge_sort(arr, count):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]
    merge_sort(left, count)
    merge_sort(right, count)
    merge(arr, left, right, count) 

def count_swap(arr):
    count = []
    merge_sort(arr, count)
    return sum(count)

def main():
    n = int(input())
    arr = list(map(int, input().split(" ")))
    count = count_swap(arr)
    print(count)

main()