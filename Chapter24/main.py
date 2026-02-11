import package.func
package.func.hello()
print(f"Module version: {package.func.version}")

from package import func
func.hello()
print(f"Module version: {func.version}")

import package.func as f
f.hello()
print(f"Module version: {f.version}")