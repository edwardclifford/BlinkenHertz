import socket
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)

UDP_IP = "10.0.0.195"
UDP_PORT = 7129

sock = socket.socket(socket.AF_INET, # Internet
socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

while True:
        data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
        print "received message: ", data
        if(data == "12"):
                GPIO.output(12, True)
        else:
                GPIO.output(12, False)





