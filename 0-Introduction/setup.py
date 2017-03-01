from distutils.core import setup
from Cython.Build import cythonize

setup(
  name = "Check speed",
  ext_modules = cythonize("check_speed.pyx")
)
