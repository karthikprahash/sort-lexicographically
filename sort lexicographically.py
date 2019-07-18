# sort-lexicographically
i=int(input())
p=list(map(str,input().split()))[:i]
p.sort(key=len)
for i in p:
    print(i,end=' ')

