def add(a: int, b: int) -> int:
    return a + b


print(add(3, 2))


# positional argument
def addd(a: int, b: str) -> tuple[int, str]:
    return a, b


print(addd(2, "3"))


# default argument
def add(a=2, b="color") -> tuple[int, str]:
    return a, b


print(add(2, "tree"))


def add(a: int, b="color") -> tuple[int, str]:
    return a, b


print(add(a=10, b="tree"))


def mutable_ish(a=[]):
    a.append("Python")
    return a


print(mutable_ish())
print(mutable_ish())
print(mutable_ish([1, 2, 3]))
print(mutable_ish())


# to overcome the mutable function up
def mutable_ish(a=None):
    if a is None:
        a = []
    a.append("python")
    return a


print(mutable_ish())


# unlimited params
def plus(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total


print(plus(1, 2, 3, 5, 6, 7, 8, 5))


def true_false(age):
    if age >= 18:
        return True
    # else:
    return False


def dict_pack_unpack(**kwargs):
    print(kwargs)

dict_pack_unpack(name = "shola", age=45, sex = "male")

def dict_pack_unpackk(*args, **kwargs):
    print("Kwargs", kwargs)
    print("Args", args)

dict_pack_unpackk(4, 5, "goal", name = "shola", age=45, sex = "male")
