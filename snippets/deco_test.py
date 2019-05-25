#!/usr/bin/env python3

# Injecting variables into a function's namespace by messing with __globals__
# This is not thread safe!
# TODO: Add a mutex just to be on the safe side

d = {'x': 'y'}

def test_deco(func):
    def wrapper(*args, **kwargs):
        sentinel = func.__globals__.get('d', 'some_sort_of_sentinel')
        func.__globals__['d'] = {'a': 'b'}
        try:
            result = func(*args, **kwargs)
        finally:
            if sentinel == 'some_sort_of_sentinel':
                del func.__globals__['d']
            else:
                func.__globals__['d'] = sentinel
        return result
    return wrapper

@test_deco
def test():
    print('d:', d)
    print("This messes with globals.")


def cleaner_way(func):
    def wrapper(*args, **kwargs):
        kwargs['d'] = {'a', 'b'}
        return func(*args, **kwargs)
    return wrapper

@cleaner_way
def test2(*args, **kwargs):
    print(kwargs)
    print(d)
    print('This does not mess with globals')

test()
test2()
