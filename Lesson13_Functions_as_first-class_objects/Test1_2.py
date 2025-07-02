import math

def volume(r, h):
    return math.pi * r ** 2 * h

def cilinder_volume_function(r, h):
    return volume(r, h)

print(cilinder_volume_function(10, 30))