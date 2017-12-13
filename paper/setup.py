from distutils.core import setup
from Cython.Build import cythonize

setup(
    name = 'irt app',
    ext_modules = cythonize("irt.pyx"),
)