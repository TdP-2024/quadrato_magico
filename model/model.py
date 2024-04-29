import copy


class Model:
    def __init__(self):
        self._n_iterazioni = 0
        self._n_soluzioni = 0
        self._soluzioni = []

    def risolvi_quadrato(self, N):
        self._n_iterazioni = 0
        self._n_soluzioni = 0
        self._soluzioni = []
        # set di tutte le possibili celle
        rimanenti = set()
        for riga in range(N):
            for colonna in range(N):
                rimanenti.add((riga,colonna))
        self._ricorsione([], rimanenti, N)

    def _ricorsione(self, parziale, rimanenti, N):
        self._n_iterazioni += 1
        # caso terminale
        if len(parziale) == N * N:
            print(parziale)
            self._n_soluzioni += 1
            self._soluzioni.append(copy.deepcopy(parziale))
        # caso ricorsivo
        else:
            for cella in rimanenti:
                # per il prossimo numero, provo ad assegnare una delle celle libere rimaste
                parziale.append(cella)

                if self._is_soluzione_parziale(parziale, N):
                    nuovi_rimanenti = copy.deepcopy(rimanenti)
                    nuovi_rimanenti.remove(cella)
                    self._ricorsione(parziale, nuovi_rimanenti, N)
                parziale.pop()



    def _is_soluzione_parziale(self, parziale, N):
        numero_magico = N * (N * N + 1) / 2

        # vincolo 1) verifica righe
        for row in range(N):  # per ognuna delle N righe
            somma = 0
            counter = 0
            for i in range(len(parziale)):
                if parziale[i][0] == row:
                    somma += i+1
                    counter += 1
            if somma != numero_magico and counter == N:
                return False

        # vincolo 2) colonne
        for col in range(N):  # per ognuna delle N righe
            somma = 0
            counter = 0
            for i in range(len(parziale)):
                if parziale[i][1] == col:
                    somma += i+1
                    counter += 1
            if somma != numero_magico and counter == N:
                return False

        # vincolo 3) diagonale 1
        somma = 0
        counter = 0
        for i in range(len(parziale)):
            if parziale[i][0] == parziale[i][1]: #se riga==colonna la cella è sulla diagonale
                somma += i+1
                counter += 1
        if somma != numero_magico and counter == N:
            return False

        # vincolo 4) diagonale 2. Da verificare solo se sono arrivato ad inserire in parziale il primo elemento dell'ultima riga
        somma = 0
        counter = 0
        for i in range(len(parziale)):
            if parziale[i][0] == N-1-parziale[i][1]:  # se riga==colonna la cella è sulla diagonale
                somma += i+1
                counter += 1
        if somma != numero_magico and counter == N:
            return False

        # tutti vincoli soddisfatti
        return True

    def stampa_soluzione(self, soluzione, N):
        print("----------")
        for row in range(N):
            riga = [0 for i in range(N)] #lista di zeri
            for i in range(N*N):
                if soluzione[i][0] == row:
                    riga[soluzione[i][1]] = i+1
            print(riga)
        print("----------")


if __name__ == '__main__':
    N = 3
    model = Model()
    model.risolvi_quadrato(N)
    print(f"Quadrato di lato {N} risolto con {model._n_iterazioni} iterazioni")
    print(f"Trovate {model._n_soluzioni} soluzioni")
    for soluzione in model._soluzioni:
        model.stampa_soluzione(soluzione, N)
