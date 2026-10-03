from rd03d import RD03D
import time

# Initialize the RD-03D radar
radar = RD03D()   # Uses default UART pins GP0/GP1

while True:
    if radar.update():
        target1 = radar.get_target(1)
        target2 = radar.get_target(2)
        target3 = radar.get_target(3)

        print(
            f"{target1.angle},{target1.distance},{target1.speed},"
            f"{target2.angle},{target2.distance},{target2.speed},"
            f"{target3.angle},{target3.distance},{target3.speed}"
        )

    time.sleep(0.05)
