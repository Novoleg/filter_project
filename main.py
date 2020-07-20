from filter import BandpassFilter
import matplotlib.pyplot as plt
import os

if __name__ == '__main__':
    # f = Bandpass_Filter(int(input('Введи w: ')), int(input('Введи W: ')),
    #                     float(input('Введи dwp: ')), float(input('Введи kf: ')),
    #                     float(input('Введи dt: ')), int(input('Введи L: ')))
    f = BandpassFilter(9, 12, 0.5, 0.5, 0.2)

    fig, ax = plt.subplots(figsize=(16, 9))
    ax.plot(f.time_func(), f.parameter_wk(), color="blue", label="Импульсная характеристика")
    ax.set_xlabel("t")
    ax.set_ylabel("wk")
    ax.legend()
    plt.grid()
    fig.savefig(os.path.join('C:\\Users\\novol\\OneDrive\\Общие документы\\Graphics', 'impulse responce.png'))

    final_list_aw = []
    final_list_phiw = []
    tmp = f.parameter_aw()

    for el in tmp:
        if el > 0:
            final_list_aw.append(el)
        else:
            final_list_phiw.append(el)

    fig, ax1 = plt.subplots(figsize=(16, 9))
    ax1.plot(f.func_w1(), final_list_aw, color="red", label="АЧХ")
    ax1.set_xlabel("ω")
    ax1.set_ylabel("A(ω)")
    ax1.legend()
    plt.grid()
    fig.savefig(os.path.join('C:\\Users\\novol\\OneDrive\\Общие документы\\Graphics', 'amplitude.png'))

    fig, ax1 = plt.subplots(figsize=(16, 9))
    ax1.plot(f.func_w1(), final_list_phiw, color="red", label="ФЧХ")
    ax1.set_xlabel("ω")
    ax1.set_ylabel("Phi(ω)")
    ax1.legend()
    plt.grid()
    fig.savefig(os.path.join('C:\\Users\\novol\\OneDrive\\Общие документы\\Graphics', 'phase.png'))
