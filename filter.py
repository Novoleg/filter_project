import math


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


class Bandpass_Filter(Filter):

    def __init__(self, w, big_w, dwp, kf, dt, L):
        super().__init__(w, big_w, dwp, kf, dt, L)

    def const(self):
        list_const = []
        wp = self.w - self.dwp / 2
        list_const.append(wp)
        big_wp = self.big_w + self.dwp / 2
        list_const.append(big_wp)
        big_wzw = big_wp * self.dt
        list_const.append(big_wzw)
        wzv = wp * self.dt
        list_const.append(wzv)
        # print(list_const)
        return list_const

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

        tmp_list_const = self.const()
        wl = self.kf * (tmp_list_const[1] - tmp_list_const[0]) / wv
        tmp_list_pk = self.parametr_pk()
        for el in range(0, self.L):
            tmp_wk = tmp_list_pk[el] * (
                    (math.sin((self.L - el) * tmp_list_const[2])) - math.sin((self.L - el) * tmp_list_const[3]))
            list_wk.append(tmp_wk)

        for el in reversed(list_wk):
            list_wk.append(el)
        list_wk.insert(self.L, wl)
        # print(len(list_wk),'Импульсная характеристика: ', list_wk)
        return list_wk

    def parametr_aw(self):
        wv = math.pi / self.dt
        tmp_list_const = self.const()
        wl = self.kf * (tmp_list_const[1] - tmp_list_const[0]) / wv
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
        print('List aw: ', list_aw)
        print('List phiw: ', list_phiw)
        return list_aw + list_phiw
