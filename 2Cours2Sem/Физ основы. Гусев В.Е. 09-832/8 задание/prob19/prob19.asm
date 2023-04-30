         LIST P=12C508
__CONFIG _WDT_OFF & _HS_OSC
         #include <P12C508.INC>
d1nl     EQU   0x20
d1nm     EQU   0x21
d1nn     equ   0x22
nang     equ   0x23
zn0      equ   0x24
zn1      equ   0x25
ch0      equ   0x26
ch1      equ   0x27
ch2      equ   0x28
ch3      equ   0x29
r1       equ   0x2A
ch4      equ   0x30
ch5      equ   0x31
ch6      equ   0x32
ch7      equ   0x33
ch8      equ   0x34
ch9      equ   0x35
ch10     equ   0x36
ch11      equ   0x37
ch12      equ   0x38
ch13      equ   0x39
ch14      equ   0x40
ch15      equ   0x41
ch16      equ   0x42
ch17      equ   0x43
ch18      equ   0x44
ch19      equ   0x45
ch20      equ   0x46
ch21      equ   0x47
ch22      equ   0x48
cr        equ   0x49
r2        equ   0x4A
;programma probnaja iz prob09.asm 04.04.05
;popitka  dobavl.gotovogo faila
         org   0x00
         goto  start
         org   0x04
         goto  srvint
start   
         bsf   STATUS,RP0
         CLRF  TRISB
         movlw 0x1c
         movwf TRISA
         movlw B'00000111'
         movwf OPTION_REG
         bcf   STATUS,RP0
         movlw 0x80
         movwf nang
         clrf  PORTB
         clrf  PORTA
         clrf  d1nl
         clrf  d1nm
         clrf  d1nn
         clrf  r1
         clrf  r2
         movlw 0x3F
         movwf ch0
         movwf cr
         movlw 0x06
         movwf ch1
         movlw 0x5B
         movwf ch2
         movlw 0x4F
         movwf ch3
         movlw 0x66
         movwf ch4
         movlw 0x6D
         movwf ch5
         movlw 0x7D
         movwf ch6
         movlw 0x07
         movwf ch7
         movlw 0x7F
         movwf ch8
         movlw 0x6F
         movwf ch9
         movlw 0x77
         movwf ch10
         movlw 0x7F
         movwf ch11
         movlw 0x39
         movwf ch12
         movlw 0x3F
         movwf ch13
         movlw 0x79
         movwf ch14
         movlw 0x71
         movwf ch15
         movlw 0x3D
         movwf ch16
         movlw 0x76
         movwf ch17
         movlw 0x30
         movwf ch18
         movlw 0x38
         movwf ch19
         movlw 0x3F
         movwf ch20
         movlw 0x73
         movwf ch21
         movlw 0x6D
         movwf ch22
         movlw B'10100000'
         movwf INTCON
         movlw B'11111111'
         ;movwf d1nm
         movwf PORTB
         bcf STATUS,0
         movfw nang
         ;movwf PORTA
update: 
         goto  update
;obslug preriv
srvint   movwf zn0
         swapf STATUS,W
         movwf zn1
         bcf   INTCON,T0IF
         ;tut d1nn pociklim v m34 
         incf  d1nn
         movfw d1nn
         sublw 0x10
         btfss STATUS,2
         goto  m34
         clrf  d1nn
         incf  d1nl
         movfw d1nm
         sublw 0x03
         btfss STATUS,2
         incf d1nm
         movfw d1nl
         sublw 0x01
         btfsc STATUS,2
         goto  m1
         movfw d1nl
         sublw 0x02
         btfsc STATUS,2
         goto  m2
         movfw d1nl
         sublw 0x03
         btfsc STATUS,2
         goto  m3
         movfw d1nl
         sublw 0x04
         btfsc STATUS,2
         goto  m4
         movfw d1nl
         sublw 0x05
         btfsc STATUS,2
         goto  m5
         movfw d1nl
         sublw 0x06
         btfsc STATUS,2
         goto  m6
         movfw d1nl
         sublw 0x07
         btfsc STATUS,2
         goto  m7
         movfw d1nl
         sublw 0x08
         btfsc STATUS,2
         goto  m8
         movfw d1nl
         sublw 0x09
         btfsc STATUS,2
         goto  m9
         movfw d1nl
         sublw 0x0A
         btfsc STATUS,2
         goto  m10
         movfw d1nl
         sublw 0x0B
         btfsc STATUS,2
         goto  m11
         movfw d1nl
         sublw 0x0C
         btfsc STATUS,2
         goto  m12
         movfw d1nl
         sublw 0x0D
         btfsc STATUS,2
         goto  m13
         movfw d1nl
         sublw 0x0E
         btfsc STATUS,2
         goto  m14
         movfw d1nl
         sublw 0x0F
         btfsc STATUS,2
         goto  m15
         movfw d1nl
         sublw 0x10
         btfsc STATUS,2
         goto  m16
         movfw d1nl
         sublw 0x11
         btfsc STATUS,2
         goto  m17
         movfw d1nl
         sublw 0x12
         btfsc STATUS,2
         goto  m18
         movfw d1nl
         sublw 0x13
         btfsc STATUS,2
         goto  m19
         movfw d1nl
         sublw 0x14
         btfsc STATUS,2
         goto  m20
         movfw d1nl
         sublw 0x15
         btfsc STATUS,2
         goto  m21
         movfw d1nl
         sublw 0x16
         btfsc STATUS,2
         goto  m22
         movfw d1nl
         sublw 0x17
         btfsc STATUS,2
         goto  m23                  
         goto  m33
m1:     
         movfw ch0
         goto m33
        
m2:      movfw ch1
         goto m33
m3:      
         movfw ch2
         goto m33
m4:      
         movfw ch3
         goto m33
m5:      
         movfw ch4
         goto m33
m6:      
         movfw ch5
         goto m33
m7:      
         movfw ch6
         goto m33
m8:      
         movfw ch7
         goto m33
m9:      
         movfw ch8
         goto m33
m10:      
         movfw ch9
         goto m33
m11:      
         movfw ch10
         goto m33
m12:      
         movfw ch11
         goto m33
m13:      
         movfw ch12
         goto m33
m14:      
         movfw ch13
         goto m33
m15:      
         movfw ch14
         goto m33
m16:      
         movfw ch15
         goto m33
m17:      
         movfw ch16
         goto m33
m18:      
         movfw ch17
         goto m33
m19:      
         movfw ch18
         goto m33
m20:      
         movfw ch19
         goto m33
m21:      
         movfw ch20
         goto m33
m22:      
         movfw ch21
         goto m33
m23:      
         movfw ch22
         clrf d1nl
m33:
         movwf PORTB
         movfw d1nm
         sublw 0x03
         btfsc STATUS,2
         goto  m50
         goto  m34     
m50:     
         btfsc r2,0
         goto m61   
         bsf   r2,0
         goto m62
m61:     
         bcf   r2,0
m62:
         btfss r2,0
         goto m60 
         incf r1
         movfw r1
         sublw 0x08
         btfss STATUS,0
         goto m54
         goto m55
m54:
         movfw r1
         sublw 0x09
         btfss STATUS,2 
         goto  m56
         movfw  ch1
         movwf  cr
m56:
         movfw r1
         sublw 0x11 
         btfss STATUS,2
         goto  m55
         movfw  ch0
         movwf  cr
         movlw 0x01
         movwf r1                  
m55:
         bsf PORTA,0
         btfsc cr,0
         goto m52
         goto m51
m51:
         bcf PORTA,1             
         bcf STATUS,0
         goto  m53
m52:
         bsf PORTA,1
         bsf STATUS,0 
m53:         
         rrf cr
         goto m34
m60:     
         bcf PORTA,0
m34:     
         swapf zn1,W
         movwf STATUS
         swapf zn0,1
         swapf zn0,W 

         retfie
         END
