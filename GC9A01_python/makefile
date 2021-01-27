LIB_DIR = lib

default: cythonGC9A01

cythonGC9A01: setup.py cythonGC9A01.pyx $(LIB_DIR)/libGC9A01.a
	python3 setup.py build_ext --inplace && rm -f GC9A01.c && rm -Rf build

$(LIB_DIR)/libGC9A01.a:
	make -C $(LIB_DIR) libGC9A01.a

clean:
	rm *.so