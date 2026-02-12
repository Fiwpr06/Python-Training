class Person:
    """Create a person with name, job, and pay attributes and methods to manipulate them."""
    def __init__(self, name, job = None, pay = 0):
        self.name = name
        self.job = job
        self.pay = pay

    def last_name(self):
        return self.name.split()[-1]
    
    def give_raise(self, percent):
        self.pay = int(self.pay * (1 + percent))
        
    def __repr__(self):
        return f"Person('{self.name}', '{self.job}', {self.pay})"

class Manager(Person):
    """A Person customized for managers, with a default job of 'mgr' and an overridden give_raise method."""
    def __init__(self, name, pay):
        super().__init__(name, 'mgr', pay)    
        
    def give_raise(self, percent, bonus=0.10):
        super().give_raise(percent + bonus)

if __name__ == "__main__":
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', 'Dev', 100000)
    
    print(bob)
    print(sue)
    print(bob.name, bob.pay)
    print(sue.name, sue.pay)
    print(bob.last_name(), sue.last_name())
    sue.give_raise(0.10)
    print(sue)
    
    pat = Manager('Pat Jones', 50000)
    pat.give_raise(0.10)
    print(pat.last_name())
    print(pat)