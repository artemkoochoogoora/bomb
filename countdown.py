import playsound

from time import sleep

for number in range(10,0000,-1):
    print (number, "\a")
    sleep(1)
print ("бомба взорвалась" )
playsound.playsound('00562.mp3', True)


