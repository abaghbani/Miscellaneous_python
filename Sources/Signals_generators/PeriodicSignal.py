import numpy as np
import matplotlib.pyplot as plt

fs = 240.0
n = np.arange(2*fs)
f = np.arange(20.0, 80.0)
x = np.zeros((f.size, n.size))
for i in range(f.size):
    x[i] = np.sin(2*np.pi*f[i]*n/fs)

# x1 = np.sin(2*np.pi**t)
# x2 = np.sin(2*np.pi*21.0*t)
# x3 = np.sin(2*5.0*t)
# plt.subplot(311)
# plt.plot(t,x1)
# plt.subplot(312)
# plt.plot(t,x2)
# plt.subplot(313)
# plt.plot(t, x1+x2)


sumSig = sum(x[m] for m in range(f.size))
plt.subplot(311)
plt.plot(n/fs,x[0])
plt.subplot(312)
plt.plot(n/fs,x[-1])
plt.subplot(313)
plt.plot(n/fs,sumSig)

plt.show()