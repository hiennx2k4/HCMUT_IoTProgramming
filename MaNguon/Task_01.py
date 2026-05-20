# Declare and import library
# Using library of Yolo:Uno device
from yolo_uno import *
# Using library of pins control
from pins import *
# Declare LED as 13th pin
led_D13 = Pins(D13_PIN)
# Define LED_blink() function to control LED status (ON/OFF)
# Set delay time to 1.000 ms (1 second)
async def LED_blink():
  while True:
    led_D13.write_digital(1)
    await asleep_ms(1000)
    led_D13.write_digital(0)
    await asleep_ms(1000)
# Define the initial() function to manage task
async def initial():
  # Show application status
  print('App started')
  # Create an independent task or process for LED_blink() 
  # function
  create_task(LED_blink())
# Define the main() function
async def main():
  await initial()
  while True:
    await asleep_ms(0)
# Run and loop infinitely application by main() function
run_loop(main())
