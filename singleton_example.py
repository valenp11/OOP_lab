
class SingletonExample(type):
    #metaclassa pro example
    _instances = {}

    def __call__(cls, *args, **kwards):
        if cls not in cls._instances:
            instance = super().__call__(*args,**kwards)
            cls._instances[cls] = instance
        return cls._instances

class Example(metaclass=SingletonExample):
    def __init__(self):
        self.value = 1

example_1 = Example()
example_2 = Example()

example_1.value = 2
example_2.value = 4

print(example_1.value)
print(example_2.value)
