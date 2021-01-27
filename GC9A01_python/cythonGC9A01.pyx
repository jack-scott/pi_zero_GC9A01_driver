cdef extern from "GC9A01.h":
    void GC9A01_begin()
    void test()
    void GC9A01_pixel(int x,int y, char color)

def py_GC9A01_begin() -> None:
    GC9A01_begin()
    
def py_test() -> None:
    test()

    
