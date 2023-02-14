from typing import Optional

from pybricks.parameters import Direction, Port
from pybricks.pupdevices import Motor


class SwerveModule:
    def __init__(
        self,
        wheel: Port,
        turn: Port,
        wheel_reversed: bool = False,
        turn_reversed: bool = False,
    ) -> None:
        self._wheel = Motor(
            wheel,
            positive_direction=Direction.CLOCKWISE
            if not wheel_reversed
            else Direction.COUNTERCLOCKWISE,
        )
        self._wheel.control.limits(1000)  # type: ignore
        self._wheel.brake()
        self._wheel_signum = 1 if not wheel_reversed else -1

        self._turn = Motor(
            turn,
            positive_direction=Direction.CLOCKWISE
            if not turn_reversed
            else Direction.COUNTERCLOCKWISE,
            gears=self.TURN_GEAR_TRAIN,
        )
        self._turn.reset_angle(0.0)
        self._turn.control.limits(1000)  # type: ignore
        self._turn_signum = 1 if not turn_reversed else -1

    def get_speed(self) -> int:
        return self._wheel.speed()

    def set_speed(self, new: int) -> None:
        if new == 0.0:
            self._wheel.brake()
        else:
            self._wheel.run(new)

    def get_angle(self) -> int:
        return self._turn.angle()

    def set_angle(self, new: int, speed: Optional[int] = None) -> None:
        self._turn.run_angle(
            speed if speed is not None else self.TURN_SPEED,
            new * self._turn_signum,
            wait=False,
        )

    TURN_SPEED = 1000
    TURN_GEAR_TRAIN = [12, 28]
