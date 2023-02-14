from __future__ import annotations

from pybricks.parameters import Port

from swerve_module import SwerveModule


class TwoWheelCoaxialSwerve:
    def __init__(self, front: SwerveModule, back: SwerveModule) -> None:
        self.front = front
        self.back = back
        self.modules = (front, back)

    @staticmethod
    def from_ports(
        front: tuple[Port, Port], back: tuple[Port, Port]
    ) -> TwoWheelCoaxialSwerve:
        return TwoWheelCoaxialSwerve(SwerveModule(*front), SwerveModule(*back))

    def forward(self, speed: int) -> None:
        for m in self.modules:
            m.set_speed(speed)

    def stop(self) -> None:
        for m in self.modules:
            m.set_speed(0)

    def strafe(self, angle: int) -> None:
        for m in self.modules:
            m.set_angle(angle)
