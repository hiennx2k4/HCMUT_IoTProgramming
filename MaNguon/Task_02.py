# Declare and import library
# Using library of Yolo:Uno device
from yolo_uno import *
# Define LED_change() function to change LED RGB color
# Set delay time to 1.000 ms (1 second) per action
async def LED_change():
  while True:
    # Set LED color to green
    neopix.show(0, hex_to_rgb('#00ff00'))
    await asleep_ms(1000)
    # Set LED color to yellow
    neopix.show(0, hex_to_rgb('#ffff00'))
    await asleep_ms(1000)
    # Set LED color to red
    neopix.show(0, hex_to_rgb('#ff0000'))
    await asleep_ms(1000)
# Define the initial() function to manage task
async def initial():
  # Show application status
  print('App started')
  # Create an independent task or process for LED_change()
  # function
  create_task(LED_change())
# Define the main() function
async def main():
  await setup()
  while True:
    await asleep_ms(0)
# Run and loop infinitely application by main() function
run_loop(main())
