import math
from Consts import Consts


class Filter:

    def __init__(self, w, big_w, dwp, kf, dt, L):
        self.w = w
        self.big_w = big_w
        self.dwp = dwp
        self.kf = kf
        self.dt = dt
        self.L = L

    def describe_filter(self):
        print('w: ', self.w)
        print('W: ', self.big_w)
        print('Dwp: ', self.dwp)
        print('Kf: ', self.kf)
        print('Dt', self.dt)
        print('L:', self.L)


class BandpassFilter(Filter):

    def __init__(self, w, big_w, dwp, kf, dt, L):
        self.c = Consts(9, 12, 0.5, 0.2)
        super().__init__(w, big_w, dwp, kf, dt, L)

    def time_func(self):
        time_list = []
        for el in range(0, 2 * self.L + 1):
            tmp_time = el * self.dt
            time_list.append(tmp_time)
        return time_list

    def parametr_sigma(self):
        list_sigma = [0]
        p = 0.54
        for el in range(1, self.L + 1):
            tmp_sigma = p + (1 - p) * math.cos((el * math.pi) / self.L)
            list_sigma.append(tmp_sigma)
        return list_sigma

    def parametr_pk(self):
        list_pk = []
        tmp_list_sigma = self.parametr_sigma()
        for el in range(0, self.L):
            tmp_pk = tmp_list_sigma[self.L - el] * self.kf / ((self.L - el) * math.pi)
            list_pk.append(tmp_pk)
        return list_pk

    def parametr_wk(self):
        list_wk = []
        wv = math.pi / self.dt
        wl = self.kf * (self.c.result_big_wp() - self.c.result_wp()) / wv
        tmp_list_pk = self.parametr_pk()
        for el in range(0, self.L):
            tmp_wk = tmp_list_pk[el] * (
                    (math.sin((self.L - el) * self.c.result_big_wzv())) - math.sin((self.L - el) * self.c.result_wzw()))
            list_wk.append(tmp_wk)
        for el in reversed(list_wk):
            list_wk.append(el)
        list_wk.insert(self.L, wl)
        # print(len(list_wk),'Импульсная характеристика: ', list_wk)
        return list_wk

    def parametr_aw(self):
        wv = math.pi / self.dt
        wl = self.kf * (self.c.result_big_wp() - self.c.result_wp()) / wv
        list_aw = []
        list_phiw = []
        dw = wv / self.L
        tmp_list_wk = self.parametr_wk()
        for el in range(0, self.L + 1):
            w1 = el * dw
            tmp = 0
            for j in range(1, self.L + 1):
                tmp = tmp + tmp_list_wk[self.L - j] * math.cos(j * self.dt * w1)
            tmp_aw = math.fabs(wl + 2 * tmp)
            tmp_phiw = -self.L * self.dt * w1
            list_aw.append(tmp_aw)
            list_phiw.append(tmp_phiw)
        print(len(list_aw), 'List aw: ', list_aw)
        print(len(list_aw), 'List phiw: ', list_phiw)
        return list_aw + list_phiw

    def func_w1(self):
        wv = math.pi / self.dt
        dw = wv / self.L
        list_w1 = []
        for el in range(0, self.L + 1):
            tmp_w1 = el * dw
            list_w1.append(tmp_w1)
        return list_w1
