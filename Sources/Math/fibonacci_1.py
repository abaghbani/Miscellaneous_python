import time as tt
import functools

# saving all function calls
@functools.lru_cache(maxsize=31)
def fib(n):
  if n <= 1:
    return n
  return fib(n-1) + fib(n-2)

t1 = tt.time()
fib(30)
print (f"Time taken: {tt.time() - t1}")
print (fib.cache_info())
