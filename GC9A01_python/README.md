
Information from this website:

https://realpython.com/python-bindings-overview/

https://github.com/realpython/materials/tree/master/python-bindings/overview_article?__s=wwn8t4akz2lx6kaml8k7 

*** Installing
    From this link https://groups.google.com/g/bcm2835/c/OwFi5NrYnPE 
    Need to set some stuff before installing bcm2835 to use it without sudo you need to:
    sudo apt-get install libcap2 libcap-dev
    sudo usermod -a -G kmem $USER
    echo 'SUBSYSTEM=="mem", KERNEL=="mem", GROUP="kmem", MODE="0660"' | sudo tee /etc/udev/rules.d/98-mem.rules
    sudo reboot

  1, install the C libraries of bcm2835, see: http://www.airspayce.com/mikem/bcm2835/
    cd ~
    wget http://www.airspayce.com/mikem/bcm2835/bcm2835-1.68.tar.gz
    tar zxvf bcm2835-1.68.tar.gz
    cd bcm2835-1.68
    Then need to open src/bcm2835.h and uncomment `define BCM2835_HAVE_LIBCAP`

    ./configure
    make
    sudo make check
    sudo make install

    ##### DONT NEED THIS ######
    Testing building as a shared object for the python library
    cd ~
    wget http://www.airspayce.com/mikem/bcm2835/bcm2835-1.68.tar.gz
    tar zxvf bcm2835-1.68.tar.gz
    cd bcm2835-1.68/src
    make libbcm2835.a
    gcc -shared bcm2835.o -o libbcm2835.so
    sudo cp libbcm2835.so /usr/local/lib/
    sudo cp bcm2835.h /usr/local/include/

    #######################

    To give a compiled application the permisions run 
    sudo setcap cap_sys_rawio+ep myappname

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

<!-- TODO - currently running into a problem where the C excecutable will only run as sudo (due to bcm2835), this is a problem as the Python file will not take sudo. 
- Have tried several steps to remove this but currenltly struggling to get libcap to be found when compiling bcm2835
    - This works now as far as i can tell. I had to fix the check by adding -lcap to the libraries
- The problem is now setting the capabilites for the compiled example code. Maybe the groups are set wrong?
Maybe the makefile isnt properly linking -lcap? -->