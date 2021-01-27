from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize

examples_extension = Extension(
    name="cythonGC9A01",
    sources=["cythonGC9A01.pyx"],
    libraries=["GC9A01", "bcm2835"],
    library_dirs=["lib"],
    include_dirs=["lib"]
)
setup(
    name="cythonGC9A01",
    ext_modules=cythonize([examples_extension])
)