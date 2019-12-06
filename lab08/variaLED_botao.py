#esse programa irá incrementar ou decrementar o brilho do led a partir de botões

import RPi.GPIO as GPIO

#configura gpios
GPIO.setmode(GPIO.BCM)

#botão pull down
GPIO.setup(24,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

#botão pull up
GPIO.setup(25,GPIO.IN,pull_up_down=GPIO.PUD_UP)


#configura gpio do led
pinoPWM = 23
PWM_freq_Hz = 200
GPIO.setup(pinoPWM, GPIO.OUT)
meuPWM = GPIO.PWM(pinoPWM, PWM_freq_Hz)

#inicia duty cycle em 0%
meuPWM.start(0)

x=0;


while True:

	#se o botão pull down for apertado, aumenta o brilho do LED
	if GPIO.input(24) == GPIO.HIGH:

		x = x + 10;

		meuPWM.ChangeDutyCycle(x)

	#se o bottão pull up for apertado, diminui o brilho do LED
	elif GPIO.input(25) == GPIO.LOW:

		x = x - 10;

		meuPWM.ChangeDutyCycle(x)
	