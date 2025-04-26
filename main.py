"""
-list[]
    -mutable
    -ordered
    -most used
    -allow duplicates
    -heterogeneous
    -dynamic size
    -append()
    -insert()
    -extend()
    -remove()
    -pop()
    -clear()
    -sort()
    -reverse()
    -index()
    -count()
    -loop
    -len()
    -slicing
"""

#list

fruits = ["apple", "banana", "cherry", "orange"]
fruits2 = ["apple", "banana", "cherry", "orange"]
fruits.pop()
fruits.sort()
print(fruits)
fruits.reverse()
print(fruits)
fruits.extend(fruits2)
print(fruits)
fruits.remove("cherry")
fruits.append("Mango")
fruits.insert(0, "cherry")


print(fruits)
print(fruits[1:4])
print(fruits.pop())
print(fruits.index("cherry"))
print(fruits.count("banana"))
print(len(fruits))

for fruit in fruits:
    print(fruit)
