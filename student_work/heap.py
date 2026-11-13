import matplotlib.pyplot as plt


class Heap:
    """Min heap con las mismas convenciones de la página de Galles:
    arreglo[0] = -inf (centinela), raíz en 1, hijos de i en 2*i y 2*i+1."""

    def __init__(self):
        self.arreglo = [float('-inf')]

    # ---------- utilidades internas ----------
    def _subir(self, i):
        # sube mientras el padre sea estrictamente mayor
        while self.arreglo[i // 2] > self.arreglo[i]:
            self.arreglo[i // 2], self.arreglo[i] = self.arreglo[i], self.arreglo[i // 2]
            i //= 2

    def _bajar(self, i):
        n = len(self.arreglo) - 1
        while 2 * i <= n:
            menor = 2 * i
            # el hijo derecho solo gana si es estrictamente menor
            if menor + 1 <= n and self.arreglo[menor + 1] < self.arreglo[menor]:
                menor += 1
            if self.arreglo[menor] < self.arreglo[i]:
                self.arreglo[i], self.arreglo[menor] = self.arreglo[menor], self.arreglo[i]
                i = menor
            else:
                break

    # ---------- operaciones de la página ----------
    def insert(self, valor, imagen=False):
        self.arreglo.append(valor)
        self._subir(len(self.arreglo) - 1)
        if imagen:
            self._mostrar()

    def remove_smallest(self, imagen=False):
        if len(self.arreglo) == 1:
            if imagen:
                self._mostrar()
            return None
        minimo = self.arreglo[1]
        ultimo = self.arreglo.pop()
        if len(self.arreglo) > 1:
            self.arreglo[1] = ultimo
            self._bajar(1)
        if imagen:
            self._mostrar()
        return minimo

    def build_heap(self, lista, imagen=False):
        self.arreglo = [float('-inf')] + list(lista)
        for i in range((len(self.arreglo) - 1) // 2, 0, -1):
            self._bajar(i)
        if imagen:
            self._mostrar()

    # ---------- imagen del árbol ----------
    def _mostrar(self):
        n = len(self.arreglo) - 1
        fig, ax = plt.subplots(figsize=(max(4, n * 0.35), 4))
        ax.axis('off')
        if n == 0:
            ax.text(0.5, 0.5, 'Heap vacío', ha='center', va='center')
            plt.show()
            return

        niveles = n.bit_length()              # número de niveles del árbol
        pos = {}
        for i in range(1, n + 1):
            d = i.bit_length() - 1            # nivel (raíz = 0)
            j = i - 2 ** d                    # lugar dentro del nivel
            pos[i] = ((j + 0.5) / 2 ** d, -d) # izquierda a derecha, raíz arriba

        for i in range(2, n + 1):             # aristas padre -> hijo
            (x1, y1), (x2, y2) = pos[i // 2], pos[i]
            ax.plot([x1, x2], [y1, y2], color='gray', zorder=1)

        for i in range(1, n + 1):             # nodos
            x, y = pos[i]
            ax.text(x, y, str(self.arreglo[i]), ha='center', va='center', zorder=2,
                    bbox=dict(boxstyle='circle,pad=0.35', fc='lightblue', ec='black'))

        ax.set_xlim(0, 1)
        ax.set_ylim(-niveles + 0.4, 0.6)
        plt.show()


if __name__ == "__main__":
    H = Heap()
    H.insert(10)
    H.insert(4)
    H.insert(7, imagen=True)
    H.remove_smallest(imagen=True)
    H.build_heap(list(range(31, 0, -1)), imagen=True)
    print(H.arreglo)
