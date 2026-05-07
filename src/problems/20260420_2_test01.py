import matplotlib.pyplot as plt

S = 1
deltat = 0.01
I_0 = 0.1

for i in range(1,1001):
    I_i = I_0 - deltat * (I_0 - S)
    print(I_i)
    plt.plot(i, I_i)
    I_0 = I_i

plt.show()