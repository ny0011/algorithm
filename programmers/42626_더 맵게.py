def heap_push(heap, value):
    heap.append(value)
    current = len(heap)-1
    while current > 0 :
        parent_pos = (current-1)>>1
        parent = heap[parent_pos]
        if (value < parent):
            heap[current] = parent
            current = parent_pos
            continue
        break
    heap[current] = value

def fix_heap_pop(heap):
    oldest = heap[0]
    current = 0
    length = len(heap) 
    left_pos = 2*current+1 
    right_pos = 2*current+2
    if right_pos == length :
        if heap[0] > heap[1]:
            heap[0], heap[1] = heap[1], heap[0]
            return
    while right_pos < length:
        if oldest < heap[left_pos] and oldest < heap[right_pos]:
            break;
        elif heap[left_pos] < heap[right_pos]:
            heap[current] = heap[left_pos]
            current = left_pos
        else:
            heap[current] = heap[right_pos]
            current = right_pos
        left_pos = 2*current+1 
        right_pos = 2*current+2
    heap[current] = oldest


def heap_pop(heap):
    oldest = heap.pop()
    if heap:
        value = heap[0]
        heap[0] = oldest
        fix_heap_pop(heap)
        return value
    return oldest

def solution(scoville, K):
    heap = sorted(scoville)
    answer = 0
    while heap[0] < K:
        if len(heap) < 2:
            return -1
        min_one = heap_pop(heap)
        min_two = heap_pop(heap)
        mixed = min_one + min_two * 2
        heap_push(heap, mixed)
        answer += 1

    return answer

'''
효율성  테스트
테스트 1 〉	실패 (시간 초과)
테스트 2 〉	실패 (시간 초과)
테스트 3 〉	통과 (9223.14ms, 64.8MB)
테스트 4 〉	실패 (시간 초과)
테스트 5 〉	통과 (9720.70ms, 67.6MB)
'''