'''Класс с расчетом сглаживающих множителей для нереккурсивных фильтров
Каждый метод класса возвращает список со значениями коэффициентов множителей
На данный момент единственная реализация, которую я представляю...
Но как говорится, нет предела совершенству!'''
# todo: Необходимо добавить расчет множителей Кайзера и Парзена


import math


class FiltersMultipliers:
    def __init__(self, l_fourier):
        self.multiplier_hamming = 0.54
        self.multiplier_hanna = 0.50
        self.l_fourier = l_fourier

    def multiplier_bartlett(self):
        list_bartlett = [0]
        for el in range(0, self.l_fourier + 1):
            tmp_bartlett = 1 - el / self.l_fourier
            list_bartlett.append(tmp_bartlett)
        return list_bartlett

    def multiplier_lanczos(self):
        list_lanczos = [0]
        for el in range(0, self.l_fourier + 1):
            tmp_lanczos = (math.sin(el * math.pi / self.l_fourier)) / (el * math.pi / self.l_fourier)
            list_lanczos.append(tmp_lanczos)
        return list_lanczos

    def multiplier_hamming_func(self):
        list_hamming = [0]
        for el in range(0, self.l_fourier + 1):
            tmp_hamming = self.multiplier_hamming + (1 - self.multiplier_hamming) * math.cos(
                el * math.pi / self.l_fourier)
            list_hamming.append(tmp_hamming)
        return list_hamming

    def multiplier_hanna_func(self):
        list_hanna = [0]
        for el in range(0, self.l_fourier + 1):
            tmp_hanna = self.multiplier_hanna + (1 - self.multiplier_hanna) * math.cos(el * math.pi / self.l_fourier)
            list_hanna.append(tmp_hanna)
        return list_hanna

    def multiplier_blackman(self):
        list_blackman = [0]
        for el in range(0, self.l_fourier + 1):
            tmp_blackman = 0.42 + 0.5 * math.cos(el * math.pi / self.l_fourier) + 0.08 * math.cos(
                2 * el * math.pi / self.l_fourier)
            list_blackman.append(tmp_blackman)
        return list_blackman
