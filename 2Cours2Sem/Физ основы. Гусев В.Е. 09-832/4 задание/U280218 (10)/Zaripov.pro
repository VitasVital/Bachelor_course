CoDeSys+4   �         �         @        @   2.3.9.9�    @   ConfigExtension�          CommConfigEx7   
          CommConfigExEnd   ME�                  IB                    % QB                    %   ME_End   CM�      CM_End   CT�   ��������   CT_End   ConfigExtensionEnd?    @                                     ��^ +    @      ��������             ��K        �$   @   D   C:\Program Files (x86)\3S Software\CoDeSys V2.3\Library\STANDARD.LIB          CONCAT               STR1               ��              STR2               ��                 CONCAT                                         �9BC  �   ����           CTD           M             ��           Variable for CD Edge Detection      CD            ��           Count Down on rising edge    LOAD            ��	           Load Start Value    PV           ��
           Start Value       Q            ��           Counter reached 0    CV           ��           Current Counter Value             �9BC  �   ����           CTU           M             ��            Variable for CU Edge Detection       CU            ��       
    Count Up    RESET            ��	           Reset Counter to 0    PV           ��
           Counter Limit       Q            ��           Counter reached the Limit    CV           ��           Current Counter Value             �9BC  �   ����           CTUD           MU             ��            Variable for CU Edge Detection    MD             ��            Variable for CD Edge Detection       CU            ��
       
    Count Up    CD            ��           Count Down    RESET            ��           Reset Counter to Null    LOAD            ��           Load Start Value    PV           ��           Start Value / Counter Limit       QU            ��           Counter reached Limit    QD            ��           Counter reached Null    CV           ��           Current Counter Value             �9BC  �   ����           DELETE               STR               ��              LEN           ��	              POS           ��
                 DELETE                                         �9BC  �   ����           F_TRIG           M             ��                 CLK            ��           Signal to detect       Q            ��	           Edge detected             �9BC  �   ����           FIND               STR1               ��	              STR2               ��
                 FIND                                     �9BC  �   ����           INSERT               STR1               ��	              STR2               ��
              POS           ��                 INSERT                                         �9BC  �   ����           LEFT               STR               ��              SIZE           ��                 LEFT                                         �9BC  �   ����           LEN               STR               ��                 LEN                                     �9BC  �   ����           MID               STR               ��              LEN           ��	              POS           ��
                 MID                                         �9BC  �   ����           R_TRIG           M             ��                 CLK            ��           Signal to detect       Q            ��	           Edge detected             �9BC  �   ����           REPLACE               STR1               ��	              STR2               ��
              L           ��              P           ��                 REPLACE                                         �9BC  �   ����           RIGHT               STR               ��              SIZE           ��                 RIGHT                                         �9BC  �   ����           RS               SET            ��              RESET1            ��	                 Q1            ��                       �9BC  �   ����           RTC           M             ��              DiffTime            ��                 EN            ��              PDT           ��                 Q            ��              CDT           ��                       �9BC  �   ����           SEMA           X             ��                 CLAIM            ��
              RELEASE            ��                 BUSY            ��                       �9BC  �   ����           SR               SET1            ��              RESET            ��                 Q1            ��                       �9BC  �   ����           TOF           M             ��           internal variable 	   StartTime            ��           internal variable       IN            ��       ?    starts timer with falling edge, resets timer with rising edge    PT           ��           time to pass, before Q is set       Q            ��       2    is FALSE, PT seconds after IN had a falling edge    ET           ��           elapsed time             �9BC  �   ����           TON           M             ��           internal variable 	   StartTime            ��           internal variable       IN            ��       ?    starts timer with rising edge, resets timer with falling edge    PT           ��           time to pass, before Q is set       Q            ��       0    is TRUE, PT seconds after IN had a rising edge    ET           ��           elapsed time             �9BC  �   ����           TP        	   StartTime            ��           internal variable       IN            ��       !    Trigger for Start of the Signal    PT           ��       '    The length of the High-Signal in 10ms       Q            ��           The pulse    ET           ��       &    The current phase of the High-Signal             �9BC  �   ����    B   C:\Program Files (x86)\3S Software\CoDeSys V2.3\Library\IECSFC.LIB          SFCACTIONCONTROL     
      S_FF                 RS    ��              L_TMR                    TON    ��              D_TMR                    TON    ��              P_TRIG                 R_TRIG    ��              SD_TMR                    TON    ��              SD_FF                 RS    ��              DS_FF                 RS    ��              DS_TMR                    TON    ��              SL_FF                 RS    ��              SL_TMR                    TON    ��           
      N            ��           Non stored action qualifier    R0            ��       #    Overriding reset action qualifier    S0            ��           Set (stored) action qualifier    L            ��	           Time limited action qualifier    D            ��
           Time delayed action qualifier    P            ��           Pulse action qualifier    SD            ��       *    Stored and time delayed action qualifier    DS            ��       %    Delayed and stored action qualifier    SL            ��       *    Stored and time limited action qualifier    T           ��           Current time       Q            ��       1    Associated action is executed, if Q equals TRUE             PI>D  �    ����    G   C:\Program Files (x86)\3S Software\CoDeSys V2.3\Library\ANALYZATION.LIB          ANALYZEEXPRESSION               InputExp            ��           	   DoAnalyze            ��              	   ExpResult            ��           	   OutString               ��                       ��7  �    ����           APPENDERRORSTRING               strOld               ��              strNew               ��                 AppendErrorString                                         ��7  �    ����                  PLC_PRG           S1                   SIGNAL    ,               S2                   SIGNAL    ,                                1,M  @    ����           SEQUENCE           delay                 WAIT    - 	              INIT                           _INIT                        
   FIRST_LAMP                            _FIRST_LAMP                            SECOND_LAMP                            _SECOND_LAMP                         
   THIRD_LAMP                            _THIRD_LAMP                            FOURTH_LAMP                            _FOURTH_LAMP                            THIRD_REV_LAMP                            _THIRD_REV_LAMP                            SECOND_REV_LAMP                            _SECOND_REV_LAMP                               start            -                  signal           -                        ?�/K  @    ����           SIGNAL               status           +                  first            +               second            +               third            +               fourth            + 	                       �+M  @    ����           SIGNALS               status           2                  first            2               second            2               third            2               fourth            2 	                       ?�/K  @    ����           WAIT           ZAB                   TP    3 	                 TIME_IN           3                  OK            3                        ?�/K  @    ����            
 �   3   2   -   '   ,   .   0   +   ( �&      K   �&     K   �&     K   �&     K   '                 '         +     ��localhost 2.3\CoDeSys exe �<)��   ���|�         ��                        X���D ������   ��@   ���?      ���?   <�S�� t�� �y� t� _Y� �� 3�� `��      �� ��D     4       �'  @��� t�� �y� ��  �� 	   `��� ƅ�                  @����     �  �      Q�s/����� `��S            Serial (RS232) Zaripov.pro comn 3S Serial RS232 driver    Q  �  Port                COM1    COM2    COM3    COM4    COM5    COM6    COM7    COM8    COM9 	   COM10 
   COM11    COM12    COM13    COM14    COM15    COM16    COM17    COM18    COM19    COM20    COM21    COM22    COM23    COM24    COM25    COM26    COM27    COM28    COM29    COM30    COM31    COM32 Y   �  Baudrate      �    �  4800 �%  9600  K  19200  �  38400  �  57600  � 115200 4   �  Parity                No    Even    Odd 3   �  Stop bits                1    1,5    2 7   d   Motorola byteorder                No    Yes 1   �  Flow Control                Off    On �         �      Q�s/����� `��S            Serial (RS232)  com2 3S Serial RS232 driver    Q  �  Port                 COM1    COM2    COM3    COM4    COM5    COM6    COM7    COM8    COM9 	   COM10 
   COM11    COM12    COM13    COM14    COM15    COM16    COM17    COM18    COM19    COM20    COM21    COM22    COM23    COM24    COM25    COM26    COM27    COM28    COM29    COM30    COM31    COM32 Y   �  Baudrate      �    �  4800 �%  9600  K  19200  �  38400  �  57600  � 115200 4   �  Parity                No    Even    Odd 3   �  Stop bits                1    1,5    2 7   d   Motorola byteorder                No    Yes 1   �  Flow Control                Off    On �      Q�s/����� `��S            Serial (RS232) Zaripov.pro comn 3S Serial RS232 driver    Q  �  Port                COM1    COM2    COM3    COM4    COM5    COM6    COM7    COM8    COM9 	   COM10 
   COM11    COM12    COM13    COM14    COM15    COM16    COM17    COM18    COM19    COM20    COM21    COM22    COM23    COM24    COM25    COM26    COM27    COM28    COM29    COM30    COM31    COM32 Y   �  Baudrate      �    �  4800 �%  9600  K  19200  �  38400  �  57600  � 115200 4   �  Parity                No    Even    Odd 3   �  Stop bits                1    1,5    2 7   d   Motorola byteorder                No    Yes 1   �  Flow Control                Off    On   K        @   ��^�G      , � � ^                     CoDeSys 1-2.2   ����  ��������                                �      
   �         �         �          �                    "          $                                                   '          (          �          �          �          �          �         �          �          �          �         �          �          �          �          �         �      �   �       P  �          �         �       �  �                    ~          �          �          �          �          �          �          �          �          �          �          �          �          �          �          �          �          �       @  �       @  �       @  �       @  �       @  �       @  �         �         �          �       �  M         N          O          P          `         a          t          y          z          b         c          X          d         e         _          Q          \         R          K          U         X         Z         �          �         �      
   �         �         �         �         �         �          �          �         �      �����          �          �      (                                                                        "         !          #          $         �          ^          f         g          h          i          j          k         F          H         J         L          N         P         R          U         S          T          V          W          �          �          l          o          p          q          r          s         u          �          v         �          �      ����|         ~         �         x          z      (   �          �         %         �          �          �         @         �          �          �         &          '          �          	                   �          �          �         �          �         �          �          �          �          �          �          �          �          �          �          �          �                            I         J         K          	          L         M          �                             �          P         Q          S          )          	          	          �          ������������������������  ��������                                                   �  	   	   Name                 ����
   Index                 ��         SubIndex                 �          Accesslevel          !         low   middle   high       Accessright          1      	   read only
   write only
   read-write       Variable    	             ����
   Value                Variable       Min                Variable       Max                Variable          5  
   	   Name                 ����
   Index                 ��         SubIndex                 �          Accesslevel          !         low   middle   high       Accessright          1      	   read only
   write only
   read-write    	   Type          ~         INT   UINT   DINT   UDINT   LINT   ULINT   SINT   USINT   BYTE   WORD   DWORD   REAL   LREAL   STRING    
   Value                Type       Default                Type       Min                Type       Max                Type          5  
   	   Name                 ����
   Index                 ��         SubIndex                 �          Accesslevel          !         low   middle   high       Accessright          1      	   read only
   write only
   read-write    	   Type          ~         INT   UINT   DINT   UDINT   LINT   ULINT   SINT   USINT   BYTE   WORD   DWORD   REAL   LREAL   STRING    
   Value                Type       Default                Type       Min                Type       Max                Type          d        Member    	             ����   Index-Offset                 ��         SubIndex-Offset                 �          Accesslevel          !         low   middle   high       Accessright          1      	   read only
   write only
   read-write       Min                Member       Max                Member          �  	   	   Name                 ����   Member    	             ����
   Value                Member    
   Index                 ��         SubIndex                 �          Accesslevel          !         low   middle   high       Accessright          1      	   read only
   write only
   read-write       Min                Member       Max                Member          �  	   	   Name                 ����
   Index                 ��         SubIndex                 �          Accesslevel          !         low   middle   high       Accessright          1      	   read only
   write only
   read-write       Variable    	             ����
   Value                Variable       Min                Variable       Max                Variable                         ����  ��������               �   _Dummy@    @   @@    @   @             ��@             ��@@   @     �v@@   ; @+   ����  ��������                                  �v@      4@   �             �v@      D@   �                       �       @                           �f@      4@     �f@                �v@     �f@     @u@     �f@        ���          __not_found__-1__not_found__    __not_found__     IB          % QB          % MB          %    ��^	?�/K     ��������           VAR_GLOBAL
END_VAR
                                                                                  "     ��������              ?�/K                 $����  ��������               ��������           Standard ��K	��K      ��������                         	?�/K     ��������           VAR_CONFIG
END_VAR
                                                                                   '              , , : �           Global_Variables ?�/K	?�/K     ��������        X   VAR_GLOBAL
	IN:BOOL;
	lamp1:BOOL;
	lamp2:BOOL;
	lamp3:BOOL;
	lamp4:BOOL;
END_VAR
                                                                                               '           	     ��������           Variable_Configuration ?�/K	?�/K	     ��������           VAR_CONFIG
END_VAR
                                                                                                 C   |0|0 @9    @   Arial @                �����              �                �      �   ���  �3 ���   � ���                  DEFAULT             System      C   |0|0 @9    @   Arial @                �����              �          HH':'mm':'ss   dd'-'MM'-'yyyy'            ,   , $ D ��           PLC_PRG C,M	1,M      ��������        9   PROGRAM PLC_PRG
VAR
	S1: SIGNAL;
	S2: SIGNAL;
END_VAR)    ����               TRUE!        ����                      SEQUENCED                                          M-1-1   ����      !          S1    SIGNAL+                                                M-3-1    M-3-2    M-3-3    M-3-4   ����7      ;         %QX1.0,             ����8      <         %QX1.1,            ����8      <         %QX1.2,            ����8   	   <   	      %QX1.3,            ����                 S2    SIGNAL+                                                M-27-1    M-27-2    M-27-3    M-27-4   ����*      .         %QX1.0,             ����*      .         %QX1.1,             ����*      .         %QX1.2,         !   ����+      /         %QX1.3,         d                  -   ,   �w           SEQUENCE ?�/K	?�/K      ��������        q   PROGRAM SEQUENCE
VAR_INPUT
	start:BOOL;
END_VAR
VAR_OUTPUT
	signal:INT;
END_VAR
VAR
	delay:WAIT;
END_VAR       Init .     ��������           Action Init =�/K
   	LD		0
	ST		signal       start      
   first_lamp /     ��������           Action first_lamp =�/K
1   	LD		1
	ST		signal
	CAL		delay(TIME_IN:=t#1s)
       delay.ok         second_lamp 0     ��������           Action second_lamp =�/K
/   	LD		2
	ST		signal
	CAL		delay(TIME_IN:=t#1s)       delay.OK      
   third_lamp '     ��������           Action third_lamp =�/K
/   	LD		3
	ST		signal
	CAL		delay(TIME_IN:=t#1s)       delay.ok         fourth_lamp 1     ��������           Action fourth_lamp =�/K
/   	LD		4
	ST		signal
	CAL		delay(TIME_IN:=t#1s)       delay.ok         third_rev_lamp )     ��������           Action third_rev_lamp =�/K
/   	LD		3
	ST		signal
	CAL		delay(TIME_IN:=t#1s)       delay.OK         second_rev_lamp *     ��������           Action second_rev_lamp =�/K
1   	LD		2
	ST		signal
	CAL		delay(TIME_IN:=t#1s)
       delay.OK  
   first_lampd                  +   , n � H           SIGNAL ��^	�+M      ��������        �   FUNCTION_BLOCK SIGNAL
VAR_INPUT
	status:INT;
END_VAR
VAR_OUTPUT
	first:BOOL;
	second:BOOL;
	third:BOOL;
	fourth:BOOL;
END_VAR
VAR
END_VAR�  CASE	status OF
	1:
      first:=FALSE;
      second:=FALSE;
	third:=TRUE;
	fourth:=FALSE;
	2:
       first:=FALSE;
	second:=FALSE;
	third:=TRUE;
	fourth:=TRUE;
	3:
        first:=FALSE;
	second:=TRUE;
	third:=FALSE;
	fourth:=FALSE;
	4:
       first:=FALSE;
	second:=TRUE;
       third:=FALSE;
       fourth:=TRUE;


	ELSE
	first:=second:=third:=fourth:=FALSE;
	END_CASE               2   , 6 ^ �           SIGNALS ?�/K	?�/K      ��������        �   FUNCTION_BLOCK SIGNALS
VAR_INPUT
	status:INT;
END_VAR
VAR_OUTPUT
	first:BOOL;
	second:BOOL;
	third:BOOL;
	fourth:BOOL;
END_VAR
VAR
END_VAR      statusA1EQ  first     statusA2EQ  second     statusA3EQ  third     statusA4EQ  fourthd                  3   ,  � Y?           WAIT ?�/K	?�/K      ��������        v   FUNCTION_BLOCK WAIT
VAR_INPUT
	TIME_IN:TIME;
END_VAR
VAR_OUTPUT
	OK:BOOL:=FALSE;
END_VAR
VAR
	ZAB:TP;
END_VAR
�   	LD		ZAB.Q
	JMPC	mark

	CAL		ZAB(IN:=FALSE)
	LD		TIME_IN
	ST		ZAB.PT
	CAL		ZAB(IN:=TRUE)
	JMP		end

mark:
	CAL		ZAB
end:
	LDN		ZAB.Q
	ST		OK
	RET                 ����  ��������         #   STANDARD.LIB 4.10.05 11:14:46 @�9BC!   IECSFC.LIB 13.4.06 15:51:28 @PI>D&   ANALYZATION.LIB 5.10.99 09:05:06 @��7      CONCAT @                	   CTD @        	   CTU @        
   CTUD @           DELETE @           F_TRIG @        
   FIND @           INSERT @        
   LEFT @        	   LEN @        	   MID @           R_TRIG @           REPLACE @           RIGHT @           RS @        	   RTC @        
   SEMA @           SR @        	   TOF @        	   TON @           TP @               F   SFCActionControl @      SFCActionType       SFCStepType                      Globale_Variablen @              AnalyzeExpression @                   AppendErrorString @              Globale_Variablen @                          ��������           2 �  �           ����������������  
             ����  ��������        ����  ��������                      POU                 PLC_PRG  ,                   SEQUENCE  -                  SIGNAL  +                   SIGNALS  2                   WAIT  3   ����             ���� ������  ����             ������������  ����              ���������� ����������                 Global_Variables                     Variable_Configuration  	   ����                                         ��������             ��K               �l                	   localhost            P      	   localhost            P      	   localhost            P     ��K    e(�x