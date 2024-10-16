import matplotlib.pyplot as plt

x = range(10)
y = range(10)

fig, ax = plt.subplots(1, 2)

plot1 = ax[0]
plot2 = ax[1]

plot1.plot(range(10), 'r') #row=0, col=0
plot2.plot(range(10), 'g') #row=0, col=1

plt.show()
