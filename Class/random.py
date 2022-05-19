import random

x = random.randint(0, 10)
print(x)

random.seed(76)
y = random.randint(0, 10)
print(y)

a = random.randrange(0, 10, 2)
print(a)

b = [4, 54, 6, 56, 3, 6, 2, 6]
# random.choice(b)
print(random.choice(b))
random.shuffle(b)
print(b)
