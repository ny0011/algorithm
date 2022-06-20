#include <string>
#include <vector>
#include <queue>
using namespace std;

int solution(vector<int> scoville, int K)
{
    priority_queue<int, vector<int>, greater<int>> heap;
    for (int i = 0; i < scoville.size(); i++)
    {
        heap.push(scoville[i]);
    }

    int answer = 0;
    while (heap.top() < K)
    {
        if (heap.size() < 2)
            return -1;
        int min_one = heap.top(); heap.pop();
        int min_two = heap.top(); heap.pop();
        int mixed = min_one + min_two * 2;
        heap.push(mixed);
        answer += 1;
    }
    return answer;
}