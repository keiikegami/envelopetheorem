import matplotlib.pyplot as pltimport numpy as npfig, ax = plt.subplots()x = np.linspace(0, 10, 200)for i in range(1,3):    y = np.sin(i*x)    ax.plot(x, y,'b-', linewidth=2)plt.show()