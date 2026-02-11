import module

module.hello()
print(f"Module version: {module.version}")

import sys
for path in sys.path:
    print(f"Module search path: {path}")
    
print("sys" in sys.modules)
print("module" in sys.modules)