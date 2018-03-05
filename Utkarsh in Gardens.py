#https://www.hackerearth.com/fr/practice/algorithms/graphs/graph-representation/practice-problems/algorithm/utkarsh-in-gardens-february-easy/

cities = int(input())

matrix = [list(map(int, input().split())) for _ in range(cities)]

path = [None]*5
count = 0

for i1 in range(cities):
    path[0] = i1
    for i2 in range(i1,cities):
        if matrix[i1][i2] == 1:
            path[1] = i2
            for i3 in range(i2,cities):
                if matrix[i2][i3] == 1:
                    path[2] = i3
                    for i4 in range(i3,cities):
                        if matrix[i3][i4] == 1:
                            path[3] = i4
                            if matrix[i4][i1] == 1:
                                count += 1

print(count)