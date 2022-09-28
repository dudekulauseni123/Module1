#include <avr/io.h>
#include <stdbool.h>
int main (void)
{

	 bool U=1,V=0,W=0,X=0,Y;
	  DDRB =  0b00100000;  
	  Y = ((!U&&V)||(!V&&U))&&((!W&&!X)||(W&&!X));
	    PORTB |= (Y<< 5);
	     return 0;
}
