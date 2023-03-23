n, m = map(int, input().split())
a= list(map(int, input().split()))
b= list(map(int, input().split()))

c = sorted(a + b)
c_dict = dict()

for i, v in enumerate(c):
    c_dict[v]=i

for i in a:
    print(c_dict[i]+1, end=" ")
print()
for i in b:
    print(c_dict[i]+1, end=" ")