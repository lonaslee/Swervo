from pybricks.hubs import InventorHub
from pybricks.parameters import Port
from pybricks.tools import wait
from uselect import poll
from usys import stdin

from swerve_drive import TwoWheelCoaxialSwerve
from swerve_module import SwerveModule


def main():
    hub = InventorHub()
    drive = TwoWheelCoaxialSwerve(
        SwerveModule(Port.B, Port.D),
        SwerveModule(Port.A, Port.C, turn_reversed=True),
    )

    keyboard = poll()
    keyboard.register(stdin)

    running = False
    while True:
        wait(10)
        if not keyboard.poll(0):
            continue

        key = stdin.read(1)

        angle: int
        if key == "4":
            angle = 90
        elif key == "7":
            angle = 45
        elif key == "1":
            angle = 135

        elif key == "6":
            angle = -90
        elif key == "9":
            angle = -45
        elif key == "3":
            angle = -135

        elif key == "8":
            angle = 0
        elif key == "2":
            angle = 180

        else:
            angle = drive.front.get_angle()

        diff = angle - drive.front.get_angle()
        drive.strafe(diff)
        print(drive.front.get_angle())

        if key == "5":
            running = not running
            if running:
                drive.forward(300)
            else:
                drive.stop()


if __name__ == "__main__":
    main()
