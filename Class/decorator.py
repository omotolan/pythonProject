def decorator(fn):
    def wrapper(*args, **kwargs):
        print("i am decorating you")
        fn(*args, **kwargs)
        print("okay bye")
    return wrapper()

