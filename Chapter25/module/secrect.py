__all__ = ['secret_function', '_internal_accessible']

def secret_function():
    """This is a secret function that should be accessible."""
    return "This is a secret function!"

def _private_function():
    """This is a private function that should not be accessible."""
    return "This is a private function!"

def _internal_accessible():
    """This function is accessible but not intended for public use."""
    return "This is an internally accessible function!"
