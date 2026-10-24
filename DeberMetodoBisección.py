import math
import numpy as np
import matplotlib.pyplot as plt

def biseccion(f, a, b, tol, max_iter):
    fa = f(a)
    fb = f(b)

    if fa == 0:
        return a

    if fb == 0:
        return b

    if fa * fb > 0:
        print("Error: el intervalo no tiene cambio de signo.")
        return None

    i = 1

    while i <= max_iter:
        p = a + (b - a) / 2
        fp = f(p)

        if fp == 0 or (b - a) / 2 < tol:
            return p

        if fa * fp > 0:
            a = p
            fa = fp
        else:
            b = p

        i = i + 1

    print("El metodo fracaso despues del maximo de iteraciones.")
    return None

# Ecuacion x = tan(x)
def funcion(x):
    return math.tan(x) - x

raiz = biseccion(funcion, 4, 4.5, 0.00001, 100)

if raiz is not None:
    print("Solucion aproximada de x = tan(x):", format(raiz, ".6f"))


# Grafica de y = x y y = tan(x)
x = np.linspace(0, 5, 1000)

plt.figure(figsize=(10, 6))
plt.plot(x, x, label="y = x")

# Se divide la tangente en segmentos para mostrar las asintotas
limite = 0.05
intervalos = [
    (0, math.pi / 2 - limite),
    (math.pi / 2 + limite, 3 * math.pi / 2 - limite),
    (3 * math.pi / 2 + limite, 5)
]

for inicio, fin in intervalos:
    xt = np.linspace(inicio, fin, 500)
    yt = np.tan(xt)
    plt.plot(xt, yt, color="orange",
             label="y = tan(x)" if inicio == 0 else "")

# Marcar la solucion aproximada
if raiz is not None:
    plt.scatter(raiz, raiz, color="red", zorder=5,
                label="Solucion aproximada")
    plt.annotate("x ≈ " + format(raiz, ".4f"), (raiz, raiz),
                 xytext=(10, 10), textcoords="offset points")

plt.axvline(math.pi / 2, linestyle="--", color="gray",
            label="Asintotas de tan(x)")
plt.axvline(3 * math.pi / 2, linestyle="--", color="gray")

plt.xlim(0, 5)
plt.ylim(-10, 10)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Grafica de y = x y y = tan(x)")
plt.grid(True)
plt.legend()
plt.tight_layout()

plt.savefig("grafica_biseccion.png", dpi=300)
plt.show()