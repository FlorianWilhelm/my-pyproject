def fib(n: int) -> int:
    """Fibonacci example function"""
    assert n > 0
    a, b = 1, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return a
