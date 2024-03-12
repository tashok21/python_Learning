def climbStairs(n):
    if n == 1:
        return 1
    if n == 2:
        return 2

    first, second = 1, 2
    for i in range(3, n + 1):
        first, second = second, first + second

    return second

# Test the function with different values of n
n = 5  # Example: Change this value to test different numbers of steps
print(f"Number of ways to climb {n} steps: {climbStairs(n)}")
