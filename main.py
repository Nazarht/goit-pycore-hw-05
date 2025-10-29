from typing import Generator, Callable
import re

def caching_fibonacci():
    cache = {}
    
    def fibonacci(n):
        if n <= 1:
            return n
        
        cache[n] = fibonacci(n-1) + fibonacci(n-2)
        return cache[n]
    
    return fibonacci

def generator_numbers(text: str) -> Generator[int, None, None]:
    for word in text.split():
        try:
            word = re.sub(r'[^0-9.]', '', word)
            yield float(word)
        except ValueError:
            continue
        
def sum_profit(text: str, func: Callable[[int], int]) -> int:
    generator = func(text)
    return sum(generator)