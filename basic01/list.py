even = [2, 4, 6, 8, 10]
odd = [1, 3, 5, 7, 9]
animals = ["rabbit", "lion", "bear"]
blankList = list()
print(odd)
print(odd[0])
print(odd[0:2])  #  a <= 출력되는 범위 < b

print(odd + even)
print(odd * 2)
odd[2] = 19
print(odd)
del odd[2]
print(odd)
print(odd[2])
odd.append(11)
print(odd)
for item in animals:
    print(item)
print(len(animals))
animals.append("dog")
animals.append("dog")
animals.append("dog")
print(animals)
animals.insert(1, "cat")
print(animals)
popAnimal = animals.pop()
print(popAnimal)
print(animals.count("dog"))
# animals.clear()
animals.remove("lion")
print(animals)
nums = [1, 3, 4, 9, 2, 7, 10, 5, 11]
nums.sort()
print(nums)
nums.sort(reverse=True)
print(nums)
nums02 = odd + even
print(nums02)
print(odd)
odd += even
print(odd)
odd.extend(even)
print(odd)

nums = [1, 2, 2, 3, 3, 4]
nums02 = list(set(nums))
print(nums02)
