from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize

# Dynamic Linking
ext_modules = [
    Extension("cimport", sources=["cimport.pyx"],
              libraries=["m"])
]

setup(
    ext_modules = cythonize(ext_modules)
)
