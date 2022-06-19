#include <string>
#include <vector>
using namespace std;

void heap_push(vector<int> &heap, int value)
{
    heap.push_back(value);
    int current = heap.size() - 1;
    while (current > 0)
    {
        int parent_pos = (current - 1) >> 1;
        int parent = heap[parent_pos];
        if (value < parent)
        {
            heap[current] = parent;
            current = parent_pos;
            continue;
        }
        break;
    }
    heap[current] = value;
}

void fix_heap_pop(vector<int> &heap)
{
    int oldest = heap[0];
    int current = 0;
    int length = heap.size();
    int left_pos = 2 * current + 1;
    int right_pos = 2 * current + 2;
    if (right_pos == length)
    {
        if (heap[0] > heap[1])
        {
            swap(heap[0], heap[1]);
            return;
        }
    }

    while (right_pos < length)
    {
        if (oldest < heap[left_pos] and oldest < heap[right_pos])
            break;
        else if (heap[left_pos] < heap[right_pos])
        {
            heap[current] = heap[left_pos];
            current = left_pos;
        }

        else
        {
            heap[current] = heap[right_pos];
            current = right_pos;
        }

        left_pos = 2 * current + 1;
        right_pos = 2 * current + 2;
    }

    heap[current] = oldest;
}

int heap_pop(vector<int> &heap)
{
    int oldest = heap.back();
    heap.pop_back();
    if (heap.empty())
        return oldest;
    int value = heap[0];
    heap[0] = oldest;
    fix_heap_pop(heap);
    return value;
}

int solution(vector<int> scoville, int K)
{
    vector<int> heap;
    for (int i = 0; i < scoville.size(); i++)
    {
        heap_push(heap, scoville[i]);
    }
    scoville = heap;

    int answer = 0;
    while (scoville[0] < K)
    {
        if (scoville.size() < 2)
            return -1;
        int min_one = heap_pop(scoville);
        int min_two = heap_pop(scoville);
        int mixed = min_one + min_two * 2;
        heap_push(scoville, mixed);
        answer += 1;
    }
    return answer;
}

int main()
{
    vector<int> scoville;
    scoville.push_back(1);
    scoville.push_back(2);
    scoville.push_back(3);
    scoville.push_back(9);
    scoville.push_back(10);
    scoville.push_back(12);
    int K = 34;
    solution(scoville, K);
}

/*
효율성  테스트
테스트 1 〉	통과 (21.95ms, 9.35MB)
테스트 2 〉	통과 (46.92ms, 14.9MB)
테스트 3 〉	통과 (214.67ms, 39.7MB)
테스트 4 〉	통과 (17.02ms, 8MB)
테스트 5 〉	통과 (229.15ms, 41.3MB
*/