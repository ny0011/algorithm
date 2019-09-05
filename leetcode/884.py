class Solution:
    def uncommonFromSentences(self, A, B):
        # 문장에서 단어가 1번만 나오면 uncommon.
        # 문제를 이해하지 못했다.....ㅠ
        print(A.split(), B.split())
        sentences = A.split() + B.split()
        print(sentences)
        wordSet = set(sentences)
        ret = [ i for i in wordSet]*2
        ret.sort()
        ret.reverse()
        print(ret.count("this"))
        for i in sentences:
            if ret.count(i) != 0 :
                ret.remove(i)
        return ret

