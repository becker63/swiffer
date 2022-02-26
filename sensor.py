from spikedev.sensor import ColorSensor, TouchSensor

cs = ColorSensor(hub.port.E)

print("color sensor RGB values are {}".format(cs.rgb(scale_by_intensity=True)))