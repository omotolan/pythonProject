name = "tolani"

print(type(name))
print(name)
# length of string
print(len(name))
print(len("\"akinsola\""))
last_name = "akinsola"
intro = "my name is akinsola tolani. i am a graduate \
of university of ilorin. i am currently learning softwre\
 engineering at semicolon"
print(intro)
new_intro = """my name is akinsola tolani. i am a graduate \
        of university of ilorin. i am currently learning software\
        engineering at semicolon"""
print(new_intro)

full_name = name + " " + last_name
print(full_name)

print(full_name[0])

# you can also get index with a negative sign
print(full_name[-1])
print(full_name[-2])

# slicing i.e getting a substring from a string
# if you ommitt the first index, python will assume index 0 and vice versa
print(full_name[0:9])

# strings are immutable
goat = "messi"
#  goat[2] = "t"  will throw an error
goat = "p" + goat[1:]
print(goat)

print(goat.upper())
print(full_name.lower())

# trim or remove white spaces
school = "semicolon      "
print(school.rstrip())  # lstrip, strip

print(school.endswith("o"))
print(school.startswith("s"))

age = input("hold old are you: ")
print(age)

prompt = "what is your password?"
password = input(prompt)
password = password[0]
print(password.upper())

# cnverting string to number cause python coolects input as strings
num = input("enter a number: ")
num = int(num) * 5
print(num)

num = int(input("enter a number: "))
print(num * num)
# number = int(input("enter a num: "))
print("the product of " + str(num) + " * " + str(num) + " is " + str(num * num))
print("the product of ", str(num), " * ", str(num), " is ", str(num * num))
print(f"the product of   {num}  *  {num}  is  {num * num}")

# finding  string in a string
some_string = "I'm telling you the truth; nothing but the truth!"
print(some_string.find("you"))

# replacing string in a string
print(some_string.replace("truth", "lies"))

# task
word = input("say something: ")
word = word.replace("o", "9")
word = word.replace("e", "1")
print(word)