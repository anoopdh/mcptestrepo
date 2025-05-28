def fibonacci(n):
    """
    Generate Fibonacci series up to n terms
    """
    # Initialize first two terms
    n1, n2 = 0, 1
    count = 0
    
    # Check if n is valid
    if n <= 0:
        print("Please enter a positive integer")
        return
    
    # Generate fibonacci series
    print("Fibonacci sequence up to", n, "terms:")
    while count < n:
        print(n1, end=" ")
        nth = n1 + n2
        # Update values
        n1 = n2
        n2 = nth
        count += 1
    print()  # New line after series

if __name__ == "__main__":
    # Default to 10 terms
    terms = 10
    fibonacci(terms)
