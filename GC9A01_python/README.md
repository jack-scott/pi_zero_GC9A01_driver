
Information from this website:

https://realpython.com/python-bindings-overview/

https://github.com/realpython/materials/tree/master/python-bindings/overview_article?__s=wwn8t4akz2lx6kaml8k7 

*** Installing

pip3 install --user cython

** Building

To build the cython library you must first build the static C library. To do this:

cd /GC9A01_python/lib
make clean
make

Then you need to build the Python shared object. To do this:

cd /GC9A01_python/
make clean
make

Test the freshly wrapped Python library by running test.py

