# Defining Hierarchy
class Level1Error(Exception):
    """Base class for Level 1 errors."""
    pass

class Level2Error(Level1Error):
    """Base class for Level 2 errors."""
    pass

class Level3Error(Level2Error):
    """Base class for Level 3 errors."""
    pass

try:
    raise Level3Error("This is a Level 3 error.")
except Level1Error as e:
    print("Caught a Level 1 error:", e, end="\n\n")

# Custom state and display
class CustomError(Exception):
    def __init__(self, line, file):
        self.line = line
        self.file = file
        
    def __str__(self):
        return f"Error on line {self.line} in {self.file}: {self.args[0]}"

try:
    raise CustomError(10, "Error in file.txt")
except CustomError as e:
    print(e, end="\n\n")
    
# Inherited
class InheritedError(Exception):
    def display(self):
        """Display the error message."""
        print("This is an inherited method.", end="\n\n")
        
class SpecificError(InheritedError):
    pass

try:
    raise SpecificError("This is a specific error.")
except SpecificError as e:
    e.display()