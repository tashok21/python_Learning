Lab 1 Problem 1A
Input:

* Bring in the library ... 
.lib 'cmoslibrary.lib' nominal

* My VCC is 
.param pvcc = 3

* Sizing Variables
.param alpha = 1.7

* Set Power and Ground as Global
.global vcc! gnd!

.subckt inv A Z 
  m1 Z A gnd! gnd! nmos w=1.4u l=0.35u AD=0.7p 
  m2 Z A vcc! vcc! pmos w=(1.4u*alpha) l=0.35u AD=0.7p*alpha  
.ends 

Cload z gnd! 30pF

Vin a gnd! 0V PWL 0 0NS 1NS 3 20NS 3

* Power Supplies
Vgnd gnd! 0 DC = 0
Vvcc vcc! 0 DC = 3V

* Analysis
.tran 1NS 80NS
.print tran v(a) v(z)

.OPTION MEASFORM=3

.OPTION POST
.TEMP 25 

.measure TRAN config_inv  TRIG v(Xinv1.a) VAL = 1.5 RISE = 1 TARG v(z) VAL=1.5 FALL = 1











Output:

.param fan = 11
Xinv1 a b inv M=1
.endXinv2 b c inv M=fan
.endXinv3 c d inv M=fan*fan
.endXinv4 d e inv M=fan*fan*fan
.endXinv5 e f inv M=fan*fan*fan*fan
.endXinv6 f g inv M=fan*fan*fan*fan*fan
.endXinv7 g h inv M=fan*fan*fan*fan*fan*fan
.endXinv8 h i inv M=fan*fan*fan*fan*fan*fan*fan
.endXinv9 i j inv M=fan*fan*fan*fan*fan*fan*fan*fan
.endXinv10 j k inv M=fan*fan*fan*fan*fan*fan*fan*fan*fan
.endXinv11 k l inv M=fan*fan*fan*fan*fan*fan*fan*fan*fan*fan
.endXinv12 l m inv M=fan*fan*fan*fan*fan*fan*fan*fan*fan*fan*fan
.endXinv13 m z inv M=fan*fan*fan*fan*fan*fan*fan*fan*fan*fan*fan*fan
.end
~       
