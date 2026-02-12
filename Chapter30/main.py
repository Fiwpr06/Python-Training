class Job:
    def __init__(self, value, data):
        self.data = data
        self.value = value

    def __add__(self, other):
            return Job(self.value + other, self.data)
    
    def __repr__(self):
        return f"Job(value={self.value}, data={self.data})"
    
    def __getattribute__(self, name):
        print(f"Accessing attribute: {name}")
        return object.__getattribute__(self, name)
    
    def __call__(self, *args, **kwds):
        print(f"Calling Job with args: {args} and kwargs: {kwds}")
        
it = Job(5000, ['location', 'position'])
new_job = it + 3000
print(it)
print(new_job)
print(it.data[1])
it(location='New York', position='Developer')
