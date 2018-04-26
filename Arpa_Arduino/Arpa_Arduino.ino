/**
 * Version Final 
 * 
 * El programa genera un pulso a 38khz para ser puesta sobre un led emisor infrarojo.
 * Luego con 7 sensores de IR que solo activan la salida(con 0) 
 * cuando perciben luz a 38Khz se envia por Serial el estado de cada led.
 * 
 * 
 * 
 * 
 *  Pulsador a 38khz 
 *  Salida en Pin 11
 *  Entradas pin 2 al 8
 *  //Codigo sacado de:
//http://forum.arduino.cc/index.php/topic,10555.0.html
 * 
 * Martes 17 de abril del 2018
 * */
// defines for setting and clearing register bits
#ifndef cbi
#define cbi(sfr, bit) (_SFR_BYTE(sfr) &= ~_BV(bit))
#endif
#ifndef sbi
#define sbi(sfr, bit) (_SFR_BYTE(sfr) |= _BV(bit))
#endif

#define SYSCLOCK 16000000  // main system clock (Hz)
#define PULSECLOCK 38000  // Hz
#define IROUT 11

int IRPins[] = {
  2, 3, 4, 5, 6, 7,8
}; 

uint8_t timer2top(unsigned long freq) ;

void setup() {
 Serial.begin(115200) ;
  
 cbi(TCCR2A,COM2A1) ; // connect OC2A (COM2A0 = 1)
 sbi(TCCR2A,COM2A0) ;
 
 cbi(TCCR2B,WGM22) ;  // CTC mode for TIMER2
 sbi(TCCR2A,WGM21) ;
 cbi(TCCR2A,WGM20) ;
 
 TCNT2 = 0 ;
 
 cbi(ASSR,AS2) ;  // use system clock for timer 2
 
 OCR2A = 255 ;   // set TOP to 255 for now
 
 cbi(TCCR2B,CS22) ;  // TIMER2 prescale = 1
 cbi(TCCR2B,CS21) ;
 sbi(TCCR2B,CS20) ;
 
 cbi(TCCR2B,FOC2A) ;  // clear forced output compare bits
 cbi(TCCR2B,FOC2B) ;

  for(int i=0;i<7;i++){
     pinMode(IRPins[i] , INPUT_PULLUP); 
  }
 

 
 pinMode(IROUT, OUTPUT) ;  // set OC2A to OUPUT  
 OCR2A = timer2top(PULSECLOCK) ; 
 sei() ;
}

// main loop
void loop() {
 
//Marco con 0 los que estan interrumpidos
for(int j=0;j<7;j++){
    if(digitalRead(IRPins[j])==LOW){
      Serial.print("1");
    }else{
      Serial.print("0");  
    }
}

Serial.println();



   delay(100);
 
}

// return TIMER2 TOP value per given desired frequency (Hz)
uint8_t timer2top(unsigned long freq) {
 return((byte)((unsigned long)SYSCLOCK/2/freq) - 1) ;
}



