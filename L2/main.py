from math import cos, pi, fabs, sin, radians
g_l = 1.62
M = 2150
v_p = 3660
a_max = 29.43
m = 1000
L_0 = 0
length = 250000
v_y0 = 0
v_x0 = 0
v_x = v_x0
v_y = v_y0

H_1 = int(input("введите конечную высоту"))
H_0 = int(input("введите начальную высоту"))

H_min = H_1 - 1
L_min = -1

H = H_0
L = L_0

delta_m = 0

time = 0.1

alpha = 45

def is_right_vielosity(v_y, v_x):
    if v_x == 0:
        return False
    else:
        budogba = (- v_y / v_x - pow(pow(v_y / v_x, 2) + 2 * g_l * (H_0 - H_1) / pow(v_x, 2), 0.5)) / (-1 * g_l / pow(v_x, 2)) + L_0
        print(budogba)
        return (- v_y / v_x - pow(pow(v_y / v_x, 2) + 2 * g_l * fabs(H_0 - 50) / pow(v_x, 2), 0.5)) / (-1 * g_l / pow(v_x, 2)) + L_0 <= length

def autopilot(angle, delta_m, time):
    a_y = (-1 * g_l + 1 / M * delta_m * v_p) * cos(radians(angle))
    a_x = (-1 * g_l + 1 / M * delta_m * v_p) * sin(radians(angle))
    H = H_0 + v_y0 * time + a_y * pow(time, 2) / 2
    L = L_0 + v_x0 * time + a_x * pow(time, 2) / 2
    v_x = v_x0 + a_x * time
    v_y = v_y0 + a_y * time
    return v_x, v_y, L, H

while is_right_vielosity(v_x, v_y) or (L == 0 and v_x == 0 and v_y == 0) :
    alpha = 45
    delta_m = (M / v_p) * (a_max + g_l)
    m -= delta_m * time
    v_x, v_y, L, H = autopilot(alpha, delta_m, time)
    print(f"vx0: {v_x0}, vy0: {v_y0} высота н: {H_0}, dlina: {L_0} угол: {alpha}, расход топл: {delta_m}, вре: {time}")
    v_x0, v_y0, L_0, H_0 = v_x, v_y, L, H
    print(f"оставшееся топливо: {m}")
a = pow(pow(a_max, 2) - pow(g_l, 2), 0.5)
L_min = length + 5 - pow(v_x0, 2) / (2 * a)

while H_0 > H_1 or v_y0 > 0:
    if L_0 < L_min - 10:
        alpha = 0
        delta_m = 0
        m -= delta_m * time
        v_x, v_y, L, H = autopilot(alpha, delta_m, time)
        L_min = length + 5 - pow(v_x0, 2) / (a * pow(2, 0.5))
    elif v_x0 > 0:
        alpha = -45
        delta_m = (M / v_p) * (a_max + g_l)
        m -= delta_m * time
        v_x, v_y, L, H = autopilot(alpha, delta_m, time)
    elif H_0 > 115:
        alpha = 0
        delta_m = 0
        m -= delta_m * time
        v_x, v_y, L, H = autopilot(alpha, delta_m, time)
        H_min = H_1 + pow(v_y0, 2) / (2 * a_max)
    elif H_0 > H_1 and v_y0 < 0:
        alpha = 0
        a = - pow(v_y0, 2) / (2 * (H_1 - H_0))
        if a > a_max:
            a = a_max
        delta_m = (M / v_p) * (a + g_l)
        m -= delta_m * time
        v_x, v_y, L, H = autopilot(alpha, delta_m, time)
    else:
        alpha = 0
        delta_m = 0
        m -= delta_m * time
        v_x, v_y, L, H = autopilot(alpha, delta_m, time)
    print(f"vx0: {v_x0}, vy0: {v_y0} высота н: {H_0}, dlina: {L_0} угол: {alpha}, расход топл: {delta_m}, вре: {time}")
    v_x0, v_y0, L_0, H_0 = v_x, v_y, L, H
print(f"оставшееся топливо: {m}")