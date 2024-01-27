import math

def solvequadratic(a, b, c):
    
    d = b**2 - 4*a*c
    
    
    if d >= 0:
        root1 = (-b + math.sqrt(d)) / (2*a)
        root2 = (-b - math.sqrt(d)) / (2*a)
        
        return root1, root2
    else:
        return None

# Example usage
a = 9
b = 7
c = 6

solutions = solvequadratic(a, b, c)

if solutions:
    print(f"The solutions are: {solutions[0]} and {solutions[1]}")
else:
    print("No real solutions.")
