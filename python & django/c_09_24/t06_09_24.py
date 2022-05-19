def optional_introduce(func):
    def wrapper(introduce = False):
        if introduce:
            print(func.__name__)
        func()
    return wrapper
@optional_introduce
def _print():
    print('1')
_print(int(input()))
