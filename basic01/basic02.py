items = [("apple", 3), ("banana", 1), ("orange", 5),("berry", 2)]

# 반복문으로 직접 정렬
for i in range(len(items)):
    for j in range(len(items) - 1):
        # 두 번째 값(점수)을 기준으로 비교
        if items[j][1] > items[j+1][1]:
            items[j], items[j+1] = items[j+1], items[j]
print(items)

matrix = [[1,2,3],[4,5,6],[7,8,9]]

row_sums = []
total = 0

for row in matrix:
    s = 0
    for n in row:
        s += n
    row_sums.append(s)
    total += s

print("행별 합:", row_sums)
print("전체 합:", total)
