import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

# Funkcja definiująca atraktor Lorenza
def lorenz(xyz, s=10, r=28, b=2.667):
    x, y, z = xyz
    x_dot = s * (y - x)
    y_dot = r * x - y - x * z
    z_dot = x * y - b * z
    return np.array([x_dot, y_dot, z_dot])

# Pytanie użytkownika o wybór parametrów
choice = input("Wprowadź 1, aby użyć domyślnych parametrów (s=10, r=28, b=2.667), lub 0, aby wprowadzić własne wartości: ")

if choice == '0':
    s = float(input("Wprowadź wartość parametru s: "))
    r = float(input("Wprowadź wartość parametru r: "))
    b = float(input("Wprowadź wartość parametru b: "))
else:
    s, r, b = 10, 28, 2.667

dt = 0.01  # Krok czasowy
num_steps = 10000  # Liczba kroków

# Inicjalizacja tablicy na współrzędne
xyzs = np.empty((num_steps + 1, 3))
xyzs[0] = (0., 1., 1.05)  # Ustawienie wartości początkowych

# Symulacja ruchu cząsteczki
for i in range(num_steps):
    xyzs[i + 1] = xyzs[i] + lorenz(xyzs[i], s, r, b) * dt

# Tworzenie wykresu 3D
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
line, = ax.plot([], [], [], lw=0.6)

# Ustawienia osi
ax.set_xlim((min(xyzs[:, 0]), max(xyzs[:, 0])))
ax.set_ylim((min(xyzs[:, 1]), max(xyzs[:, 1])))
ax.set_zlim((min(xyzs[:, 2]), max(xyzs[:, 2])))
ax.set_xlabel("Oś X")
ax.set_ylabel("Oś Y")
ax.set_zlabel("Oś Z")
ax.set_title("Atraktor Lorenza")

# Funkcja inicjalizująca animację
def init():
    line.set_data([], [])
    line.set_3d_properties([])
    return line,

# Funkcja aktualizująca animację
def update(num):
    line.set_data(xyzs[:num, 0], xyzs[:num, 1])
    line.set_3d_properties(xyzs[:num, 2])
    return line,

# Tworzenie animacji
ani = FuncAnimation(fig, update, frames=num_steps, init_func=init, blit=True, interval=10)

# Wyświetlenie animacji
plt.show()
