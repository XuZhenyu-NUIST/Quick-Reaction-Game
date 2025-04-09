from gpiozero import LED,Button
from time import sleep
from random import uniform
led = LED(4)
i=5
player1=0
player2=0
right_button = Button(15)
left_button = Button(14)
def pressed(button):
    global button_pressed
    global player1,player2
    if not button_pressed:
        button_pressed = True
        if button.pin.number == 14:
            player1+=1
            print(left_name + ' won the game')
        else:
            player2+=1
            print(right_name + ' won the game')
left_name = input('left player name is ')
right_name = input('right player name is ')
right_button.when_pressed = pressed
left_button.when_pressed = pressed

while i>0:
  i-=1
  button_pressed=False
  led.on()
  sleep(uniform(1,2))
  led.off()
  sleep(2)
print("Game over")
if player1>player2:
  print(left_name + 'won the game')
else:
  print(left_name + 'won the game')










