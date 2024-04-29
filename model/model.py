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
        self._ricorsione([], set(range(1, N*N+1)), N)


    def _ricorsione(self, parziale, rimanenti, N):
        self._n_iterazioni += 1
        # caso terminale
        if len(parziale) == N*N:
            # if self._is_soluzione(parziale, N):
            print(parziale)
            self._n_soluzioni += 1
            self._soluzioni.append(copy.deepcopy(parziale))
        #caso ricorsivo
        else:
            for i in rimanenti:
                parziale.append(i)
                if self._is_soluzione_parziale(parziale, N):
                    nuovi_rimanenti = copy.deepcopy(rimanenti)
                    nuovi_rimanenti.remove(i)
                    self._ricorsione(parziale, nuovi_rimanenti, N)
                parziale.pop()

    def _is_soluzione(self, parziale, N):
        numero_magico = N*(N*N+1)/2
        # vincolo 1) righe
        for row in range(N): # per ognuna delle N righe
             somma = 0
             sottolista = parziale[row*N:(row+1)*N]
             for elemento in sottolista:
                 somma += elemento
             if somma != numero_magico:
                 return False

        # vincolo 2) colonne
        for col in range(N):
            somma = 0
            sottolista = parziale[0*N + col : (N-1)*N+col + 1: N]
            for elemento in sottolista:
                somma += elemento
            if somma != numero_magico:
                return False

        # vincolo 3) diagonale 1
        somma = 0
        for riga_col in range(N):
            somma += parziale[riga_col*N + riga_col]
        if somma != numero_magico:
            return False

        # vincolo 4) diagonale 2
        somma = 0
        for riga_col in range(N):
            somma += parziale[riga_col * N + (N-1-riga_col)]
        if somma != numero_magico:
            return False

        # tutti vincoli soddisfatti
        return True


    def _is_soluzione_parziale(self, parziale, N):
        numero_magico = N*(N*N+1)/2
        # vincolo 1) righe
        n_righe = len(parziale)//N
        for row in range(n_righe): # per ognuna delle N righe
             somma = 0
             sottolista = parziale[row*N:(row+1)*N]
             for elemento in sottolista:
                 somma += elemento
             if somma != numero_magico:
                 return False

        # vincolo 2) colonne
        n_col = max(len(parziale) - N*(N-1), 0)
        for col in range(n_col):
            somma = 0
            sottolista = parziale[0*N + col : (N-1)*N+col + 1: N]
            for elemento in sottolista:
                somma += elemento
            if somma != numero_magico:
                return False

        # vincolo 3) diagonale 1. Da verificare solo se parziale ha lunghezza N*N
        if len(parziale) == N*N:
            somma = 0
            for riga_col in range(N):
                somma += parziale[riga_col*N + riga_col]
            if somma != numero_magico:
                return False


        # vincolo 4) diagonale 2. Da verificare solo se sono arrivato ad inserire in parziale il primo elemento dell'ultima riga
        if len(parziale) == N*(N-1)+1:
            somma = 0
            for riga_col in range(N):
                somma += parziale[riga_col * N + (N-1-riga_col)]
            if somma != numero_magico:
                return False

        # tutti vincoli soddisfatti
        return True

    def stampa_soluzione(self, soluzione, N):
        print("----------")
        for row in range(N):
            print( [v for v in soluzione[row*N:(row+1)*N]] )
        print("----------")


if __name__ == '__main__':
    N = 3
    model = Model()
    model.risolvi_quadrato(N)
    print(f"Quadrato di lato {N} risolto con {model._n_iterazioni} iterazioni")
    print(f"Trovate {model._n_soluzioni} soluzioni")
    for soluzione in model._soluzioni:
        model.stampa_soluzione(soluzione, N)