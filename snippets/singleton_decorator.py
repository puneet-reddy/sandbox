#!/usr/bin/env python

class Singleton:
    '''
    A class decorator to make a class a singleton.
    '''
    def __init__(self, cls, *args, **kwargs):
        self._cls = cls

    def Instance(self, *args, **kwargs):
        try:
            return self._instance
        except AttributeError:
            self._instance = self._cls(*args, **kwargs)
            return self._instance

    def __call__(self, *args, **kwargs):
        raise TypeError('Singletons must be accessed through `Instance()`.')

    def __instancecheck__(self, inst):
        return isinstance(inst, self._cls)

if __name__ == '__main__':
    @Singleton
    class TestClass:
        def __init__(self):
            self.val = 1

    t1 = TestClass.Instance()
    t1.val = 100
    t2 = TestClass.Instance()
    print(t1.val)
    print(t2.val)
