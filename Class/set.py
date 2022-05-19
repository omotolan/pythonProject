#set doesn't take duplicates
s1 = {1, 2, 3, 4, 5, 6, 7}
s2 = {4, 5, 6, 7, 8, 9,}

s1.add(8)
print(s1)
s1.add(1)
print(s1)
s1.clear()
print(s1)

s1 = {1, 2, 3, 4, 5, 6, 7}
s2 = {4, 5, 6, 7, 8, 9,}

t = s1 & s2 #what's common
print(t)