import PyBCM2835 as bcm


class GC9A01(object):
    def __init__(self, DC=24, RST=25, USE_HORIZONTAL=2):
        self._DC = DC
        self._RST = RST
        self._USE_HORIZONTAL = USE_HORIZONTAL  #Set the display direction 0,1,2,3,4 

        buffer = [] #size = [TFT_WIDTH * TFT_HEIGHT * 2]
        bcm.spi_begin()


    def command(self, cmd):
        bcm.gpio_write(self._DC, LOW)
        bcm.spi_transfer(cmd)

    def data(self, cmd):
        bcm.gpio_write(self._DC, HIGH)
        bcm.spi_transfer(cmd)

    def clear(self):
        i = 0
        for i in range(0,len(buffer)):
            self.buffer[i] = 0
            i+=1
        
    
    def begin(self):
        print("alive")
        bcm.gpio_fsel(self._RST, GPIO_FSEL_OUTP)
        PyBCM2835_gpio_fsel(self._DC, PyBCM2835_GPIO_FSEL_OUTP)
        print("alive")
        bcm.spi_begin()
        bcm.spi_setBitOrder(bcm.SPI_BIT_ORDER_MSBFIRST)     #The default
        bcm.spi_setDataMode(bcm.SPI_MODE0)                  #The default
        bcm.spi_setClockDivider(bcm.SPI_CLOCK_DIVIDER_64)  #The default
        bcm.spi_chipSelect(bcm.SPI_CS0)                     #The default
        bcm.spi_setChipSelectPolarity(bcm.SPI_CS0, LOW)     #the default

        bcm.gpio_write(self._RST, HIGH)
        bcm.delay(10)
        bcm.gpio_write(self._RST, LOW)
        bcm.delay(10)
        bcm.gpio_write(self._RST, HIGH)
        bcm.delay(100)
    
    
    #************* Start Initial Sequence **********# 
        self.command(0xEF)
    
        self.command(0xEB)
        data(0x14) 
        
        self.command(0xFE)			 
        self.command(0xEF) 

        self.command(0xEB)	
        data(0x14) 

        self.command(0x84)			
        data(0x40) 

        self.command(0x85)			
        data(0xFF) 

        self.command(0x86)			
        data(0xFF) 

        self.command(0x87)			
        data(0xFF)

        self.command(0x88)			
        data(0x0A)

        self.command(0x89)			
        data(0x21) 

        self.command(0x8A)			
        data(0x00) 

        self.command(0x8B)			
        data(0x80) 

        self.command(0x8C)			
        data(0x01) 

        self.command(0x8D)			
        data(0x01) 

        self.command(0x8E)			
        data(0xFF) 

        self.command(0x8F)			
        data(0xFF) 


        self.command(0xB6)
        data(0x00) 			
        data(0x00) 

        self.command(0x36)
        
        if(self._USE_HORIZONTAL==0):
            data(0x18)
        elif(self._USE_HORIZONTAL==1):
            data(0x28)
        elif(self._USE_HORIZONTAL==2):
            data(0x48)
        else:
             data(0x88)


        self.command(0x3A)			
        data(0x05) 


        self.command(0x90)			
        data(0x08)
        data(0x08)
        data(0x08)
        data(0x08) 

        self.command(0xBD)			
        data(0x06)
        
        self.command(0xBC)			
        data(0x00)	

        self.command(0xFF)			
        data(0x60)
        data(0x01)
        data(0x04)

        self.command(0xC3)			
        data(0x13)
        self.command(0xC4)			
        data(0x13)

        self.command(0xC9)			
        data(0x22)

        self.command(0xBE)			
        data(0x11) 

        self.command(0xE1)			
        data(0x10)
        data(0x0E)

        self.command(0xDF)			
        data(0x21)
        data(0x0c)
        data(0x02)

        self.command(0xF0)   
        data(0x45)
        data(0x09)
        data(0x08)
        data(0x08)
        data(0x26)
        data(0x2A)

        self.command(0xF1)    
        data(0x43)
        data(0x70)
        data(0x72)
        data(0x36)
        data(0x37)  
        data(0x6F)


        self.command(0xF2)   
        data(0x45)
        data(0x09)
        data(0x08)
        data(0x08)
        data(0x26)
        data(0x2A)

        self.command(0xF3)   
        data(0x43)
        data(0x70)
        data(0x72)
        data(0x36)
        data(0x37) 
        data(0x6F)

        self.command(0xED)	
        data(0x1B) 
        data(0x0B) 

        self.command(0xAE)			
        data(0x77)
        
        self.command(0xCD)			
        data(0x63)		


        self.command(0x70)			
        data(0x07)
        data(0x07)
        data(0x04)
        data(0x0E) 
        data(0x0F) 
        data(0x09)
        data(0x07)
        data(0x08)
        data(0x03)

        self.command(0xE8)			
        data(0x34)

        self.command(0x62)			
        data(0x18)
        data(0x0D)
        data(0x71)
        data(0xED)
        data(0x70) 
        data(0x70)
        data(0x18)
        data(0x0F)
        data(0x71)
        data(0xEF)
        data(0x70) 
        data(0x70)

        self.command(0x63)			
        data(0x18)
        data(0x11)
        data(0x71)
        data(0xF1)
        data(0x70) 
        data(0x70)
        data(0x18)
        data(0x13)
        data(0x71)
        data(0xF3)
        data(0x70) 
        data(0x70)

        self.command(0x64)			
        data(0x28)
        data(0x29)
        data(0xF1)
        data(0x01)
        data(0xF1)
        data(0x00)
        data(0x07)

        self.command(0x66)			
        data(0x3C)
        data(0x00)
        data(0xCD)
        data(0x67)
        data(0x45)
        data(0x45)
        data(0x10)
        data(0x00)
        data(0x00)
        data(0x00)

        self.command(0x67)			
        data(0x00)
        data(0x3C)
        data(0x00)
        data(0x00)
        data(0x00)
        data(0x01)
        data(0x54)
        data(0x10)
        data(0x32)
        data(0x98)

        self.command(0x74)			
        data(0x10)	
        data(0x85)	
        data(0x80)
        data(0x00) 
        data(0x00) 
        data(0x4E)
        data(0x00)					
        
        self.command(0x98)			
        data(0x3e)
        data(0x07)

        self.command(0x35)	
        self.command(0x21)     

        self.command(0x11) 
        bcm.delay(120)
        self.command(0x29) 
        bcm.delay(20)

        self.clear()

if __name__ =='__main__':
    display = GC9A01()
    display.begin()
