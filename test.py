import math

w = 9
big_w = 12
dwp = 0.5
kf = 0.5
dt = 0.2
L = 75

list_sigma = [0]
p = 0.54
for el in range(1, L + 1):
    tmp_sigma = p + (1 - p) * math.cos((el * math.pi) / L)
    list_sigma.append(tmp_sigma)
wp = w - dwp / 2
big_wp = big_w + dwp / 2
big_wzw = big_wp * dt
wzv = wp * dt

list_pk = []
for el in range(0, L):
    tmp_pk = list_sigma[L - el] * kf / ((L - el) * math.pi)
    list_pk.append(tmp_pk)

wv = math.pi / dt
wl = kf * (big_wp - wp) / wv
list_wk = []
for el in range(0, L):
    tmp_wk = list_pk[el] * ((math.sin((L - el) * big_wzw)) - math.sin((L - el) * wzv))
    list_wk.append(tmp_wk)

list_aw = []
list_phiw = []
dw = wv / L
list_w1 = []
for el in range(0, L + 1):
    w1 = el * dw
    tmp = 0
    for j in range(1, L + 1):
        tmp = tmp + list_wk[L - j] * math.cos(j * dt * w1)
    tmp_aw = math.fabs(wl + 2 * tmp)
    list_aw.append(tmp_aw)
    tmp_phiw = - L * dt * w1
    list_phiw.append(tmp_phiw)
    list_w1.append(w1)

list_wk_1 = []
for el in reversed(list_wk):
    tmp_wk_1 = el
    list_wk_1.append(el)
list_wk.append(wl)
final_list_wk = list_wk + list_wk_1

list_time = []
for el in range(0, 2 * L + 1):
    tmp_time = el * dt
    list_time.append(tmp_time)
