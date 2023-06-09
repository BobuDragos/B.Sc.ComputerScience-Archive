#Libraries
import RPi.GPIO as GPIO
import time

#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)

#set GPIO Pins
GPIO_TRIGGER = 12
GPIO_ECHO = 24
led = 11

#set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)
GPIO.setup (led, GPIO.OUT)

def distance():
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)

    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)

    StartTime = time.time()
    StopTime = time.time()

    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()

    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()

    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2

    return distance

if __name__ == '__main__':
    pwm_led = GPIO.PWM(led,50)
    pwm_led.start(100)
    print("Distance:")
    try:
        while True:
            dist = distance()
            print ("Measured Distance = %.1f cm" % dist)
            if int(dist) < 100 and int(dist) > 0:
                duty=int(dist)
                pwm_led.ChangeDutyCycle(100-duty)
                dist_old=dist
                if dist/50 > 0.5: # daca distanta este mai mare de 50 cm
                        temp=float(float(dist)/50)/0.5 #imparte in portiuni de 0.5 secunde distanta de mai sus
                        print("temp=%.lf",temp)
                        i=1
                        while i <= int(temp): #la fiecare 0.5s se citeste noua distanta si daca este mai mica decat 2/3
                                print(i)      #din distanta veche atunci se incepe imediat calcularea noii distante
                                i=i+1		  #si ledul va afisa noi valori corespunzatoare noii distante imediat
                                time.sleep(0.5)
                                dist=distance()
                                if dist < 2*dist_old/3:
                                        pwm_led.ChangeDutyCycle(0)
                                        break
                                        break
                        print("time.sleep extra: %.lf" % float(float(dist_old)/50-temp*0.5))
                        time.sleep(float(float(dist_old)/50-temp*0.5))
                else:
                        time.sleep(dist/50) # timp in care ledul este aprins
                pwm_led.ChangeDutyCycle(0)
            if 0.1*dist/10 <= 0.5:
                time.sleep(0.1*dist/10) # timp in care ledul sta oprit si nu se calculeaza distanta, maxim 0.5 sta stins
            else:
                time.sleep(0.5)
        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()
