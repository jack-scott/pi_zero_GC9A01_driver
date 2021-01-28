default: libGC9A01.a

all: libGC9A01.a example.o

libGC9A01.a: GC9A01.o 
	ar rcs $@ $^

example:example.o GC9A01.o
	gcc -Wall -lcap -o example example.o GC9A01.o  -lbcm2835 

GC9A01.o:GC9A01.c GC9A01.h
	gcc -static -Wall -lcap -c GC9A01.c -lbcm2835 

example.o:example.c GC9A01.h 
	gcc -Wall -lcap -c example.c -lbcm2835  

clean:
	rm *.o & rm *.a & rm example
