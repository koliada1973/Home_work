import math

def cilinder_volume_function(r):
    def volume(h):
        return math.pi * r ** 2 * h
    return volume
volume_of_r10 = cilinder_volume_function(10)
print(volume_of_r10(30))
