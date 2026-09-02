# ============================================
# 1. GENERATOR FUNCTION (The Recipe)
# ============================================
import types

def count_up_to(n):
    """This is a GENERATOR FUNCTION"""
    print(f"Starting generator for {n}")
    i = 0
    while i < n:
        print(f"About to yield {i}")
        yield i
        print(f"After yielding {i}, continuing")
        i += 1
    print(f"Generator finished for {n}")

# ============================================
# 2. GENERATOR OBJECT (The Chef)
# ============================================
gen = count_up_to(3)  # ← This creates the generator OBJECT

print(f"Type of gen: {type(gen)}")
print(f"Is gen a generator? {isinstance(gen, types.GeneratorType)}")

# Now let's use the generator object
print("First call to next(gen):")
value = next(gen)  # Starts executing!
print(f"Got value: {value}\n")

print("Second call to next(gen):")
value = next(gen)
print(f"Got value: {value}\n")

print("Third call to next(gen):")
value = next(gen)
print(f"Got value: {value}\n")