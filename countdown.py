import playsound

from time import sleep

for number in range(10,0000,-1):
    print (number, "\a")
    sleep(1)
print ("бомба взорвалась" )
playsound.playsound('zvuk-vzryvy-zvuk-vzryva-v-tveri-21_11_12-i-signalizaciy-avtomobili.mp3', True)


