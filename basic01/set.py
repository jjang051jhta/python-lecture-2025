set01 = {1, 2, 3, 1, 2, 3}  # set은 중복을 허용하지 않는다.
print(set01)
set02 = set("Hello")
print(set02)
set03 = set([1, 2, 3, 1, 2, 3])
print(set03)
set04 = set([1, 2, 3, 4, 5, 6])
set05 = set([4, 5, 6, 7, 8, 9])
# 교집합
intersectionSet = set04 & set05
intersectionSet = set04.intersection(set05)
unionSet = set04 | set05
unionSet = set04.union(set05)
differenceSet = set04 - set05
differenceSet = set04.difference(set05)
print(f"intersection==={intersectionSet}")
print(f"union==={unionSet}")
print(f"difference==={differenceSet}")
set05.add(10)
print(set05)
set05.update([11, 12, 13, 14, 15])
print(set05)
set05.remove(11)
print(set05)
# set05.remove(100)  remove는 없으면 오류  discard는 오류 안남
print(set05)
set05.clear()
print(set05)
