# This __init__.py file makes math_tools folder a package and imports functions from submodules
from .basic import add,subtract,multiply,divide # Importing basic functions
from .advanced import sin_deg, cos_deg, tan_deg # Importing advanced functions

__all__ = ['add', 'subtract', 'multiply', 'divide','sin_deg', 'cos_deg', 'tan_deg'] # Defining the public interface of the math_tools package

print("math_tools package imported successfully!.")

