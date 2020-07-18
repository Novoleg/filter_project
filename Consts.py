class Consts:
    def __init__(self, w, big_w, dwp, dt):
        self.w = w
        self.dwp = dwp
        self.big_w = big_w
        self.dt = dt

    def result_wp(self):
        return self.w - self.dwp / 2

    def result_big_wp(self):
        return self.big_w + self.dwp / 2

    def result_wzw(self):
        return self.result_wp() * self.dt

    def result_big_wzv(self):
        return self.result_big_wp() * self.dt



