N = int(input())
array = []
for i in range(N):
    array.append(int(input()))
    
array = sorted(array, reverse=True)

for a in array:
    print(a, end=' ')