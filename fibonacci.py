def fibonacci(n):
    """
    Generate Fibonacci series up to n terms
    Args:
        n (int): Number of terms to generate
    Returns:
        list: List containing the Fibonacci series
    """
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    fib_series = [0, 1]
    for i in range(2, n):
        fib_series.append(fib_series[i-1] + fib_series[i-2])
    return fib_series

def main():
    try:
        n = int(input("Enter the number of terms for Fibonacci series: "))
        if n < 0:
            print("Please enter a non-negative number")
            return
        
        result = fibonacci(n)
        print(f"\nFibonacci series with {n} terms:")
        print(result)
        
    except ValueError:
        print("Please enter a valid integer")

if __name__ == "__main__":
    main()
