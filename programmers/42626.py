MAX=1000000001

def min_heapify(arr):
    heap = list()
    for v in arr:
        heap = heap_push(heap, v)
    return heap

def heap_push(heap, value):
    heap.append(value)
    current = len(heap)-1
    while(current > 0 and heap[current] < heap[(current-1)//2]):
        heap[current], heap[(current-1)//2] = heap[(current-1)//2], heap[current]
        current = (current-1)//2
    return heap

def heap_pop(heap):
    value = heap[0]
    length = len(heap) - 1
    heap[0] = heap[length]
    heap[length] = MAX    
    current = 0
    while (2*current+1 < length):
        if heap[current] < heap[2*current+1] and heap[current] < heap[2*current+2]:
            break;
        elif heap[2*current+2] > heap[2*current+1]:
            heap[current],heap[2*current+1] = heap[2*current+1],heap[current]
            current = 2* current + 1
        else:
            heap[current],heap[2*current+2] = heap[2*current+2],heap[current]
            current = 2* current + 2
    return (value, heap[:length])

def solution(scoville, K):
    heap = min_heapify(scoville)
    answer = 0
    while len(heap) > 1:
        min_one, heap = heap_pop(heap)
        min_two, heap = heap_pop(heap)
        mixed = min_one + min_two * 2
        heap = heap_push(heap, mixed)
        answer += 1
        
        if K <= heap[0]:
            break    
    
    if K > heap[0]:
        return -1
    return answer

