# complex (complex numbers)
# --------------------------
# Complex numbers are numbers with a real and imaginary part.
# In Python, they are written as <real> + <imaginary>j (e.g., 3 + 4j).
# The real part can be accessed with .real, and the imaginary part with .imag.
# Use case: Complex numbers are commonly used in scientific computing, engineering, signal processing, and mathematics where calculations involve imaginary numbers (such as electrical circuit analysis or Fourier transforms).
# Example:
c = 3 + 4j
print("Complex number:", c)
print("Real part:", c.real)
print("Imaginary part:", c.imag)

# tuple
# -----
# Tuples are immutable sequences, typically used to store collections of heterogeneous data.
# Once created, the elements of a tuple cannot be changed.
# Tuples are defined using parentheses ().
# Use case: Tuples are used when you want to ensure the data cannot be modified, such as representing fixed collections (coordinates, RGB colors, database records) or as keys in dictionaries.
# Example:
t = (1, "apple", 3.14)
print("Tuple:", t)
print("First element:", t[0])

# Set Types:
# ----------
# set
# ---
# A set is an unordered collection of unique elements.
# Sets are mutable, but the elements must be immutable.
# Sets are defined using curly braces {} or the set() constructor.
# Use case: Sets are useful for membership testing, removing duplicates from a collection, and performing mathematical set operations like union, intersection, and difference.
# Example:
s = {1, 2, 3, 2}
print("Set:", s)  # Output: {1, 2, 3}

# frozenset
# ---------
# A frozenset is an immutable version of a set.
# Once created, elements cannot be added or removed.
# Useful as dictionary keys or set elements.
# Use case: Frozensets are used when you need a set that must not change, for example, as keys in dictionaries or elements of other sets.
# Example:
fs = frozenset([1, 2, 3, 2])
print("Frozenset:", fs)

# Binary Types:
# -------------
# bytes
# -----
# Bytes are immutable sequences of bytes (integers in the range 0 <= x < 256).
# Used for binary data, such as files or network resources.
# Defined with a b prefix (e.g., b'hello').
# Use case: Bytes are used when working with binary data, such as reading/writing files, network communication, or cryptographic operations.
# Example:
b = b'hello'
print("Bytes:", b)

# bytearray
# ---------
# Bytearrays are mutable sequences of bytes.
# You can modify their contents after creation.
# Use case: Bytearrays are used when you need to manipulate binary data in place, such as editing file contents or constructing binary protocols.
# Example:
ba = bytearray(b'hello')
ba[0] = 72  # Change 'h' (104) to 'H' (72)
print("Bytearray:", ba)

# memoryview
# ----------
# A memoryview object allows Python code to access the internal data of an object that supports the buffer protocol (like bytes or bytearray) without copying.
# Useful for large data manipulation and slicing.
# Use case: Memoryview is used for efficient handling of large binary data sets, such as image processing or scientific computing, where copying data would be inefficient.
# Example:
mv = memoryview(b'hello')
print("Memoryview (as bytes):", mv.tobytes())



# UI => Backend => database 
# # API level
# database => backend => ui


# # authentication