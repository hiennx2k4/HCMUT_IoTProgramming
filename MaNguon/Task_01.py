# Khai báo thư viện sử dụng
# Thư viện các tập lệnh riêng của thiết bị Yolo:Uno
from yolo_uno import *
# Thư viện các tập lệnh về chân cắm
from pins import *
# Khai báo chân cắm số 13 (đèn LED)
led_D13 = Pins(D13_PIN)
# Tạo hàm điều khiển đèn LED (tắt/mở)
# Thời gian chờ giữa mỗi lệnh là 1.000 ms (1 giây)
async def LED_blink():
  while True:
    await asleep_ms(50)
    led_D13.write_digital(1)
    await asleep_ms(1000)
    led_D13.write_digital(0)
    await asleep_ms(1000)
# Hàm khởi chạy cho thiết bị
async def initial():
  print('App started')
  # Khai báo tác vụ (tiến trình) chạy độc lập cho hàm LED_blink()
  create_task(LED_blink())
# Hàm khởi chạy chính cho thiết bị
async def main():
  await initial()
  while True:
    await asleep_ms(100)
# Hàm khởi chạy hàm chính với vòng lặp vô tận
run_loop(main())
