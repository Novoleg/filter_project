import math
from FiltersMultipliers import FiltersMultipliers
from Consts import Consts


class Filter:

    def __init__(self, w, big_w, dwp, kf, dt):
        self.filter_multiplier = FiltersMultipliers(75)
        self.w = w
        self.big_w = big_w
        self.dwp = dwp
        self.kf = kf
        self.dt = dt

    def describe_filter(self):
        print('w: ', self.w)
        print('W: ', self.big_w)
        print('Dwp: ', self.dwp)
        print('Kf: ', self.kf)
        print('Dt', self.dt)


class BandpassFilter(Filter):

    def __init__(self, w, big_w, dwp, kf, dt):
        self.c = Consts(9, 12, 0.5, 0.2)
        super().__init__(w, big_w, dwp, kf, dt)

    def time_func(self):
        time_list = []
        for el in range(0, 2 * self.filter_multiplier.l_fourier + 1):
            tmp_time = el * self.dt
            time_list.append(tmp_time)
        return time_list

    def parameter_pk(self):
        list_pk = []
        tmp_list_sigma = self.filter_multiplier.multiplier_hamming_func()
        for el in range(0, self.filter_multiplier.l_fourier):
            tmp_pk = tmp_list_sigma[self.filter_multiplier.l_fourier - el] * self.kf / (
                    (self.filter_multiplier.l_fourier - el) * math.pi)
            list_pk.append(tmp_pk)
        return list_pk

    def parameter_wk(self):
        list_wk = []
        wv = math.pi / self.dt
        wl = self.kf * (self.c.result_big_wp() - self.c.result_wp()) / wv
        tmp_list_pk = self.parameter_pk()
        for el in range(0, self.filter_multiplier.l_fourier):
            tmp_wk = tmp_list_pk[el] * (
                    (math.sin((self.filter_multiplier.l_fourier - el) * self.c.result_big_wzv())) - math.sin(
                (self.filter_multiplier.l_fourier - el) * self.c.result_wzw()))
            list_wk.append(tmp_wk)
        for el in reversed(list_wk):
            list_wk.append(el)
        list_wk.insert(self.filter_multiplier.l_fourier, wl)
        return list_wk

    def parameter_aw(self):
        wv = math.pi / self.dt
        wl = self.kf * (self.c.result_big_wp() - self.c.result_wp()) / wv
        list_aw = []
        list_phiw = []
        dw = wv / self.filter_multiplier.l_fourier
        tmp_list_wk = self.parameter_wk()
        for el in range(0, self.filter_multiplier.l_fourier + 1):
            w1 = el * dw
            tmp = 0
            for j in range(1, self.filter_multiplier.l_fourier + 1):
                tmp = tmp + tmp_list_wk[self.filter_multiplier.l_fourier - j] * math.cos(j * self.dt * w1)
            tmp_aw = math.fabs(wl + 2 * tmp)
            tmp_phiw = -self.filter_multiplier.l_fourier * self.dt * w1
            list_aw.append(tmp_aw)
            list_phiw.append(tmp_phiw)
        return list_aw + list_phiw

    def func_w1(self):
        wv = math.pi / self.dt
        dw = wv / self.filter_multiplier.l_fourier
        list_w1 = []
        for el in range(0, self.filter_multiplier.l_fourier + 1):
            tmp_w1 = el * dw
            list_w1.append(tmp_w1)
        return list_w1
