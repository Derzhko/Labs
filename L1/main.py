from math import cos, pi, fabs
g_l = 1.62
M = 2150
v_p = 3660
a_max = 29.43
m = 200
H_0 = 570
v_0 = 70

H = H_0
v = v_0

def autopilot(angle, delta_m, time):
    if angle == 180:
        angle = pi
    a = fabs(-1 * g_l * cos(angle) + (-1) * cos(angle) / M * delta_m * v_p)
    v = (-1) * a * time * cos(angle) + v_0
    H = H_0 + v_0 * time + (-1) * cos(angle) * a * pow(time, 2) / 2

    return v, H




while H > 0:
    if v > 0:
        delta_m = (a_max - g_l) * M / v_p
        time = v / a_max
        m -= delta_m * time
        v, H = autopilot(0, delta_m, time)
        v_0, H_0 = v, H
        print(v, H)
    else:
        a = g_l
        time = pow(2 * H / a, 0.5)
        delta_m = (a + g_l) * M / v_p
        if delta_m * time < m:
            v, H = autopilot(180, delta_m, time)
            v_0, H_0 = v, H
            print(v, H)
