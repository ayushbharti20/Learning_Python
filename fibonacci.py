# Fibonacci sequence 
def fibonacci(n):
    a, b = 0, 1
    sequence = []
    for _ in range(n):# _ is used when the variable is not needed
        sequence.append(a)
        a, b = b, a + b
    return sequence

print(f"__name__ value in fibonacci.py: {__name__}")

if __name__ == "__main__":
    print("This is executed when fibonacci.py is run directly")






