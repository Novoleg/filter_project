import test
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(16, 9))
ax.plot(test.list_time, test.final_list_wk, color="blue", label="Импульсная характеристика")
ax.set_xlabel("t")
ax.set_ylabel("wk")
ax.legend()
plt.grid()
fig.savefig('impulse responce.png')

fig, ax1 = plt.subplots(figsize=(16, 9))
ax1.plot(test.list_w1, test.list_aw, color="red", label="АЧХ")
ax1.set_xlabel("ω")
ax1.set_ylabel("A(ω)")
ax1.legend()
plt.grid()
fig.savefig('amplitude.png')

fig, ax2 = plt.subplots(figsize=(16, 9))
ax2.plot(test.list_w1, test.list_phiw, color="green", label="ФЧХ")
ax2.set_xlabel("ω")
ax2.set_ylabel("Φ(ω)")
ax2.legend()
plt.grid()
fig.savefig('phase.png')
