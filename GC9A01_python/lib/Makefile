default: libGC9A01.a

libGC9A01.a: GC9A01.o
	ar rcs $@ $^

GC9A01.o:GC9A01.c GC9A01.h
	gcc -static -Wall -c GC9A01.c -lbcm2835

clean:
	rm *.o *.a
