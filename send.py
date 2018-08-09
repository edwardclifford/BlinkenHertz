import socket
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

UDP_IP = "10.0.0.195"
UDP_PORT = 7129
MESSAGE = "12"

print "UDP target IP: ", UDP_IP
print "UDP target port: ", UDP_PORT
print "Message: ", MESSAGE

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while(True):
        if GPIO.input(10) == GPIO.HIGH:
                sock.sendto(MESSAGE , (UDP_IP, UDP_PORT))
                print "ON"
        else:
                sock.sendto("0", (UDP_IP, UDP_PORT))
                print "OFF"


