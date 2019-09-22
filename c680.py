T = int(input())
ans = input()
person = int(input())
for i in range(person):
    pa = input()
    ai = [j for j in range(min(T, len(pa))) if ans[j] == pa[j]]
    print(100 // T * len(ai))
