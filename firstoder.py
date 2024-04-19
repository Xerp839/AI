from sympy import symbols
from sympy.logic import And, Or, Implies, Not, Equivalent
from sympy.logic.inference import satisfiable
# Define symbols for variables
A, B, C = symbols('A B C')
# Define a first-order logic expression
expression = And(A, Or(B, C))
# Print the expression
print("FOL Expression:", expression)
# Check if the expression is satisfiable
print("Is Satisfiable:", satisfiable(expression))
# You can also define more complex expressions using logical connectives
expression2 = Implies(And(A, B), C)
print("Complex FOL Expression:", expression2)
# Perform logical operations
negation = Not(expression)
print("Negation:", negation)
equivalence = Equivalent(A, B)
print("Equivalence:", equivalence)