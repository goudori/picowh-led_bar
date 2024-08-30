import machine  # type: ignore
import utime  # type: ignore
import random  # type: ignore


pin = [6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
led = []
for i in range(10):
    led.append(machine.Pin(pin[i], machine.Pin.OUT))


while True:
    # 順番に点灯
    for i in range(10):
        led[i].value(1)  # 点灯
        utime.sleep(0.2)
        led[i].value(0)  # 消灯
        utime.sleep(0.2)

    # ランダムに点灯
    for _ in range(10):
        random_index = random.randint(
            0, 9
        )  # 0 から 9 までのランダムなインデックスを生成
        led[random_index].value(1)  # ランダムに選択した要素を点灯
        utime.sleep(0.2)
        led[random_index].value(0)  # ランダムに選択した要素を消灯
        utime.sleep(0.2)
