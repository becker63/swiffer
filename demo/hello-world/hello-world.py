import hub
from spikedev.motor import MotorSpeedDPS
from spikedev.tank import MoveDifferential
from spikedev.unit import DistanceInches, DistanceStuds
from spikedev.wheel import SpikeWheel

md = MoveDifferential(hub.port.A, hub.port.B, SpikeWheel, DistanceStuds(11))

# rotate 90 degrees clockwise
md.turn_right(90, MotorSpeedDPS(100))
