import numpy as np
import matplotlib.pyplot as plt
import seaborn

# Constantes
t = np.linspace(0,1,50)
x0 = np.array([15,25,20])
c = np.array([1.4,2.3,1.6])

mu = np.array([0.0,0.0,0.0])
sigma = np.array([[5.0, 2.2, -1.1],
                   [2.2, 6.8, 4.1],
                   [-1.1, 4.1, 4.6]])

# Generacion del proceso aleatorio
x = [x0]
for i in range(1,len(t)):
    xk = c + x[-1] + np.random.multivariate_normal(mu, sigma)
    x.append(xk)

# Grafico
plt.style.use('seaborn-dark-palette')
plt.plot(t, x)
plt.title('Evolución de precios $x_k$')
plt.xlabel('$t$')
plt.ylabel('$x_k$')
plt.legend(['$x_1$', '$x_2$', '$x_3$'])
plt.show()