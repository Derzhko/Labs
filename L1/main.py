from math import cos
g_l = 1.62
M = 2150
v_p = 3660
a_max = 29.43
m = 200
H_0 = 570
v_0 = 70


def autopilot(angle, delta_m, time):
    a = -1 * g_l + cos(angle) / M * delta_m
    v = a * time + v_0
    H = H_0 + v_0 * time + cos(angle) * a * pow(time, 2) / 2
    return v, H


H = H_0

while H > 0:
    delta_m = (a_max + g_l) * M
