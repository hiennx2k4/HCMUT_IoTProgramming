# Declare and import library
# Using library of Yolo:Uno device
from yolo_uno import *
# Using library of temperature and humidity sensor
from dht20 import *
# Declare variable for command
dht20 = DHT20()
# Define DHT_value() function to get value from sensor
# Set delay time to 1.000 ms (1 second) per action
async def DHT_value():
  while True:
    await asleep_ms(1000)
    print("Temperature: ",dht20.temperature(),". Humidity: ", dht20.humidity())
# Define the initial() function to manage task
async def initial():
  # Show application status
  print('\nRead data from sensor')
  # Create an independent task or process for DHT_value()
  # function
  create_task(DHT_value())
# Define the main() function
async def main():
  await initial()
  while True:
    await asleep_ms(0)
# Run and loop infinitely application by main() function
run_loop(main())
