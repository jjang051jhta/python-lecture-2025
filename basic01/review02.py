# list [], tutple()
nums = [10, 20, 30, 40, 50]
print(nums[0])
print(nums[0:2])
print(nums[1:3])
print(nums[0::2])  # start:end:step
print(nums[::-1])
print(f"sum : {sum(nums)}")
print(f"max : {max(nums)}")
print(f"min : {min(nums)}")
print(f"avg : {sum(nums) / len(nums)}")

import statistics

print(statistics.mean(nums))

a = [1, 2]
b = [3, 4]
c = a + b
print(c)
d = [a, b]
print(d[0][0])
e = [*a, *b]
print(e)
# a.extend(b)
# print(a)
print(f"len(nums) = {len(nums)}")
strList = list("python")
print(strList)
nums02 = [1, 3, 2, 4, 5, 9, 7, 8, 6]
# nums02.sort() #변형된다.
# print(f"nums02.sort()={nums02}")
sortedNums02 = sorted(nums02)
print(nums02, "===", sortedNums02)
person = {"name": "장성호", "age": 20}
print(person)
print(person["name"])
print(person["age"])
print(person.get("name"))
print(person.get("age"))
print("name" in person)
aa = {"x": 10, "y": 20}
bb = {"z": 30}
cc = aa | bb
dd = {**aa, **bb}
print(dd)
