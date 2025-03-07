import matplotlib.pyplot as plt
import numpy as np

# Definimos los rangos de X
x = np.linspace(-10, 10, 400)

# Definimos las ecuaciones
y1 = 2 * x + 1
y2 = -x + 1

# Graficamos las funciones
plt.plot(x, y1, label="Y = 2x + 1", color="blue")
plt.plot(x, y2, label="Y = -X + 1", color="red")

# Estilizamos el gráfico
plt.axhline(0, color="black", linewidth=0.5)
plt.axvline(0, color="black", linewidth=0.5)
plt.grid(color="gray", linestyle="--", linewidth=0.5)
plt.title("Gráficas de las ecuaciones lineales")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()

# Mostramos el gráfico
plt.show()
