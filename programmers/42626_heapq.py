import heapq

def solution(scoville, K):
    answer = 0
    scoville.sort()
    while scoville[0] < K:
        if len(scoville) <= 1:
            return -1
        else:
            small = heapq.heappop(scoville)
            small2 = heapq.heappop(scoville)
            heapq.heappush(scoville, (small + (small2 * 2)))
            answer += 1
    return answer

'''
heapq(min heap)를 사용하면 가장 앞에 있는 값이 항상 제일 작은 값이 됨.
heapq에서 두번 pop을 한 후 새로 섞은 값을 push 하면 됨.
pop : O(logn)
push : O(logn)
가 되어 총 시간복잡도는 O(nlogn) 

효율성  테스트
테스트 1 〉	통과 (169.62ms, 16MB)
테스트 2 〉	통과 (401.35ms, 21.9MB)
테스트 3 〉	통과 (1579.71ms, 49.8MB)
테스트 4 〉	통과 (139.96ms, 15MB)
테스트 5 〉	통과 (1705.01ms, 51.9MB)
'''