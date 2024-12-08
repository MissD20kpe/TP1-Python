import matplotlib.pyplot as plt
import numpy as np
def tracer_cercle(rayon):
    theta = np.linspace(0, 2 * np.pi, 100)
    x = rayon * np.cos(theta)
    y = rayon * np.sin(theta)
    plt.plot(x, y, label=f'Cercle de rayon {rayon}')
    plt.plot([0, rayon], [0, 0], label=f'Rayon = {rayon}', color='red', linestyle='--')
    plt.plot([-rayon, rayon], [0, 0], label=f'Diamètre = {2 * rayon}', color='green', linestyle=':')
    plt.text(rayon / 2, 0.05, f'Rayon = {rayon}', color='red', ha='center')
    plt.text(0, 0.1, f'Diamètre = {2 * rayon}', color='green', ha='center')
    plt.axhline(0, color='black',linewidth=1)
    plt.axvline(0, color='black',linewidth=1)
    plt.gca().set_aspect('equal', adjustable='box')  # Aspect égal pour le cercle
    plt.legend()
rayon = int(input("Le rayon du cercle:"))
tracer_cercle(rayon)
plt.title("Cercle avec rayon et diamètre")
plt.show()
