/***************************************************
//Web: http://www.buydisplay.com
EastRising Technology Co.,LTD
Examples for ER-TFTM1.28-1
Display is Hardward SPI 4-Wire SPI Interface 
Tested and worked with: 
Works with Raspberry pi
****************************************************/

#include <bcm2835.h>
#include <stdio.h>
#include <time.h>
#include "GC9A01.h"

char value[10] = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'};
int main(int argc, char **argv)
{
    time_t now;
    struct tm *timenow;
    FILE *pFile ;
    /* 1 pixel of 888 bitmap = 3 bytes */
    size_t pixelSize = 3;
    unsigned char bmpBuffer[TFT_WIDTH * TFT_HEIGHT * 3];

    if(!bcm2835_init())
    {
        return -1;
    }

 


  
    GC9A01_begin();
    GC9A01_mono_bitmap(57, 57, mono_bmp, 128, 128, GREEN);
    GC9A01_display();
    bcm2835_delay(2000);


   
    pFile = fopen("pic1.bmp", "r");

   if (pFile == NULL) {
        printf("file not exist\n");
        return 0;
    }
  
    fseek(pFile, 54, 0);
    fread(bmpBuffer, pixelSize, TFT_WIDTH * TFT_HEIGHT, pFile);
    fclose(pFile);

    GC9A01_bitmap24(0, 0, bmpBuffer, 240, 240);
    GC9A01_display();
    bcm2835_delay(2000);



   pFile = fopen("pic2.bmp", "r");

   if (pFile == NULL) {
        printf("file not exist\n");
        return 0;
    }

    fseek(pFile, 54, 0);
    fread(bmpBuffer, pixelSize, TFT_WIDTH * TFT_HEIGHT, pFile);
    fclose(pFile);

    GC9A01_bitmap24(0, 0, bmpBuffer, 240, 240);
    GC9A01_display();
    bcm2835_delay(2000);

   pFile = fopen("pic3.bmp", "r");

   if (pFile == NULL) {
        printf("file not exist\n");
        return 0;
    }

    fseek(pFile, 54, 0);
    fread(bmpBuffer, pixelSize, TFT_WIDTH * TFT_HEIGHT, pFile);
    fclose(pFile);

    GC9A01_bitmap24(0, 0, bmpBuffer, 240, 240);
    GC9A01_display();
    bcm2835_delay(2000);

   pFile = fopen("pic4.bmp", "r");

   if (pFile == NULL) {
        printf("file not exist\n");
        return 0;
    }

    fseek(pFile, 54, 0);
    fread(bmpBuffer, pixelSize, TFT_WIDTH * TFT_HEIGHT, pFile);
    fclose(pFile);

    GC9A01_bitmap24(0, 0, bmpBuffer, 240, 240);
    GC9A01_display();
    bcm2835_delay(2000);

   pFile = fopen("pic5.bmp", "r");

   if (pFile == NULL) {
        printf("file not exist\n");
        return 0;
    }

    fseek(pFile, 54, 0);
    fread(bmpBuffer, pixelSize, TFT_WIDTH * TFT_HEIGHT, pFile);
    fclose(pFile);

    GC9A01_bitmap24(0, 0, bmpBuffer, 240, 240);
    GC9A01_display();
    bcm2835_delay(2000);


   pFile = fopen("pic6.bmp", "r");

   if (pFile == NULL) {
        printf("file not exist\n");
        return 0;
    }

    fseek(pFile, 54, 0);
    fread(bmpBuffer, pixelSize, TFT_WIDTH * TFT_HEIGHT, pFile);
    fclose(pFile);

    GC9A01_bitmap24(0, 0, bmpBuffer, 240, 240);
    GC9A01_display();
    bcm2835_delay(2000);


    GC9A01_clear();
    printf("TFT example. Press Ctrl + C to exit.\n");

    uint16_t i=100;
    while(1)
    {
        time(&now);
        timenow = localtime(&now);

        GC9A01_mono_bitmap(45, 40, Signal816, 16, 8, GOLDEN); 
        GC9A01_mono_bitmap(75, 40, Msg816, 16, 8, GOLDEN); 
        GC9A01_mono_bitmap(95, 40, Bluetooth88, 8, 8, GOLDEN); 
        GC9A01_mono_bitmap(115, 40, GPRS88, 8, 8, GOLDEN); 
        GC9A01_mono_bitmap(135, 40, Alarm88, 8, 8, GOLDEN); 
        GC9A01_mono_bitmap(165, 40, Bat816, 16, 8, GOLDEN); 

        GC9A01_string(40, 170, "MUSIC", 16, 0, WHITE); 
     	GC9A01_string(95, 170, "EastRising", 16, 1, CYAN); 
        GC9A01_string(180, 170, "MENU", 16, 1, GOLDEN); 


        GC9A01_char3216(0, 100, value[timenow->tm_hour / 10],RED);
        GC9A01_char3216(30,100, value[timenow->tm_hour % 10],RED);
        GC9A01_char3216(60, 100, ':' , WHITE);
        GC9A01_char3216(90, 100, value[timenow->tm_min / 10], GREEN);
        GC9A01_char3216(120, 100, value[timenow->tm_min % 10], GREEN);
        GC9A01_char3216(150, 100, ':' , WHITE);
        GC9A01_char3216(180, 100, value[timenow->tm_sec / 10],  BLUE);
        GC9A01_char3216(210, 100, value[timenow->tm_sec % 10],  BLUE);

        GC9A01_string(48, 130, "www.buydisplay.com", 16, 1, i); 
	i+=1000; if(i>=65536)i=1000;
    
        GC9A01_display();
      
    }
    bcm2835_spi_end();
    bcm2835_close();
    return 0;
}

