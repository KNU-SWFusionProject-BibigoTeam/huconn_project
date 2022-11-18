import RPi.GPIO as GPIO
import time

#라이트, 창문, 문, 클락션, 기어, 출발, 브레이크, 미디어플레이어, 사이드미러
button = [17, 27, 22, 5, 6, 13, 19, 26, 21]
#클락션 울리기 위한 부저
Horn = 20

def setup():
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
	GPIO.setup(Horn, GPIO.OUT)
	GPIO.setwarnings(False)

# ButtonNumber = 5 기어 변속
def checkInput(ButtonNumber):
    if let[ButtonNumber] == 0:
        let[ButtonNumber] = 1
        print("On")
    elif let[ButtonNumber] == 1:
        let[ButtonNumber] = 0
        print("Off")
    elif ButtonNumber == 4: 
    	let[ButtonNumber] = let[ButtonNumber] + 1 
  
def loop():
	
	while True:
		
		if GPIO.input(button[0]) == True:	# 라이트
			time.sleep(0.2)
            print("light Button")
            time.sleep(0.2)                	
            checkInput(0)
	        print(let[0])               	
		elif GPIO.input(button[1]) == True:	# 창문
			time.sleep(0.2)
            print("car window Button")
            time.sleep(0.2)
            checkInput(1)
		elif GPIO.input(button[2]) == True:	# 문
            time.sleep(0.2)
            print("car Door Button")
            time.sleep(0.2)
            checkInput(2)
		elif GPIO.input(button[3]) == True:	# 클락션
            time.sleep(0.2)
            print("Horn Button")
            time.sleep(0.2)
            GPIO.output(Horn, True)
		elif GPIO.input(button[3]) == False:	# 클락션
            GPIO.output(Horn, False)
        elif GPIO.input(button[4]) == True:	# 기어
            time.sleep(0.2)
            print("Gear Button")
            time.sleep(0.2)
            checkInput(4)
        elif GPIO.input(button[5]) == True:	# 출발
            time.sleep(0.2)
            print("start Button")
            time.sleep(0.2)
            checkInput(5)
	    elif GPIO.input(button[6]) == True:	# 브레이크
            time.sleep(0.2)
            print("break Button")
            time.sleep(0.2)
            checkInput(6)
        elif GPIO.input(button[7]) == True:	# 미디어플레이어
            time.sleep(0.2)
            print("media Button")
            time.sleep(0.2)
            checkInput(7)  
		elif GPIO.input(button[8]) == True:	# 사이드미러
            time.sleep(0.2)
            print("side mirror Button")
            time.sleep(0.2)
            checkInput(8)	
                 
def endprogram():
    	GPIO.cleanup()
     
if __name__ == '__main__':
	global let
	let  = [0, 0, 0, 0, 0, 0, 0, 0, 0]	
 
	setup()
	try:
		loop()
	except KeyboardInterrupt:
		print("keyboard interrupt detected")
		endprogram()
