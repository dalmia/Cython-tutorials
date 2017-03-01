from libc.stdlib cimport atoi
from libc.math cimport sin
from cpython.version cimport PY_VERSION_HEX

# Using atoi
cdef parse_charptr(char* s):
    assert s is not NULL
    return atoi(s)

# Check CPython version
print PY_VERSION_HEX >= 0x030200F0

# math library
cdef double f(double x):
    return sin(x * x)
