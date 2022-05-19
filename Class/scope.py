num = 1


def print_out():
    print(num)

print_out()

def print_outt():
    global num
    num += 1
    print(num)

print_outt()

arg = 6
def func(param):
    param = 5
    print(param)

func(arg)
print(arg)