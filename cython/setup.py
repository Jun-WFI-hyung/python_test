#setup.py
from setuptools import setup
from Cython.Build import cythonize

setup(
    name='intg_cython',
    ext_modules=cythonize("cython_test.pyx"),
    zip_safe=False,
)