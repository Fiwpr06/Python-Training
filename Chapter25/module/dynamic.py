_dynamic_data = {
    "name": "Dynamic Module",
    "version": "1.0",
    "description": "This module demonstrates dynamic imports in Python."
}

def __getattr__(name):
    if name in _dynamic_data:
        return _dynamic_data[name]
    raise AttributeError(f"Module '{__name__}' has no attribute '{name}'")

def __dir__():
    return list(_dynamic_data)