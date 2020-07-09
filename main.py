from filter import Filter, Bandpass_Filter

if __name__ == '__main__':
    # f = Bandpass_Filter(int(input('Введи w: ')), int(input('Введи W: ')),
    #                     float(input('Введи dwp: ')), float(input('Введи kf: ')),
    #                     float(input('Введи dt: ')), int(input('Введи L: ')))
    f = Bandpass_Filter(9, 12, 0.5, 0.5, 0.2, 75)
    # f.describe_filter()
    f.parametr_aw()
    # f.parametr_wk()
