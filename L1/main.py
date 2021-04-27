from math import cos, pi, fabs
g_l = 1.62
M = 2150
v_p = 3660
a_max = 29.43
m = 200
M += m
v_0 = int(input("введите начальную скорость"))
H_0 = int(input("введите начальную высоту"))

H_min = -1

H = H_0
v = v_0

time = 0.001

alpha = 0

def autopilot(angle, delta_m, time):
    if angle == 180:
        angle = pi
    a = -1 * g_l - cos(angle) / M * delta_m * v_p
    v = a * time + v_0
    H = H_0 + v_0 * time + a * pow(time, 2) / 2

    return v, H

while H > 0 and m > 0:
    if v > 0:
        alpha = 0
        delta_m = (a_max - g_l) * M / v_p
        m -= delta_m * time
        v, H = autopilot(alpha, delta_m, time)
    elif v < 0 and H < H_min:
        alpha = 180
        delta_m = (a_max + g_l) * M / v_p
        if delta_m * time < m:
            m -= delta_m * time
            v, H = autopilot(alpha, delta_m, time)
        else:
            v, H = autopilot(alpha, 0, time)
    else:
        alpha = 180
        delta_m = 0
        m -= delta_m * time
        v, H = autopilot(alpha, delta_m, time)
        H_min = pow(v, 2) / (2 * a_max)
        #print(H_min)
    print(f"скорость начальная: {v_0}, высота   начальная: {H_0}, угол положения двигателя: {alpha}, расход топлива: {delta_m}, время: {time}")
    v_0, H_0 = v, H
print(f"оставшееся топливо: {m}")
