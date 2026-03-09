# Basic Function Decorator
def tracer(func):
    def wrapper(*args, **kwargs):
        print(f"Calling: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@tracer
def spam(a, b, c):
    return a + b + c

result = spam(1, 2, 3)
print(f"Result: {result}", end="\n\n")

# Class Decorator for Singleton Pattern
def singleton(aClass):
    instance = None
    def onCall(*args, **kwargs):
        nonlocal instance
        if instance is None:
            instance = aClass(*args, **kwargs)
        return instance
    return onCall

@singleton
class Database:
    def __init__(self):
        print("Loading DB...")

db1 = Database()
db2 = Database()
print(db1 is db2, end="\n\n")

# Class Decorator with Delegation
def Private(*privates):
    def onDecorator(aClass):
        class onInstance:
            def __init__(self, *args, **kargs):
                self.wrapped = aClass(*args, **kargs)
            def __getattr__(self, attr):
                if attr in privates:
                    raise TypeError('private attribute fetch: ' + attr)
                return getattr(self.wrapped, attr)
            def __setattr__(self, attr, value):
                if attr == 'wrapped':
                    self.__dict__[attr] = value
                elif attr in privates:
                    raise TypeError('private attribute change: ' + attr)
                else:
                    setattr(self.wrapped, attr, value)
        return onInstance
    return onDecorator

@Private('data')
class Doubler:
    def __init__(self, label, start):
        self.label = label
        self.data = start 
        
d = Doubler('Test', 4)
print(d.label)  
try:
    print(d.data)
except TypeError as e:
    print(e)