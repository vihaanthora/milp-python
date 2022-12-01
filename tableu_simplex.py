import numpy as np

class LinearModel:
    def __init__(self, A=np.empty([0, 0]), b=np.empty([0, 0]), c=np.empty([0, 0]), minmax="MAX"):
        self.A = A
        self.b = b
        self.c = c
        self.x = [float(0)] * len(c)
        self.minmax = minmax
        self.printIter = False
        self.optimalValue = None

    def getTableau(self):
        # construct starting tableau

        t1 = np.array([None, 0])
        numVar = len(self.c)
        numSlack = len(self.A)

        t1 = np.hstack(([None], [0], self.c, [0] * numSlack))

        basis = np.array([0] * numSlack)

        for i in range(0, len(basis)):
            basis[i] = numVar + i

        A = self.A

        if not ((numSlack + numVar) == len(self.A[0])):
            B = np.identity(numSlack)
            A = np.hstack((self.A, B))

        t2 = np.hstack((np.transpose([basis]), np.transpose([self.b]), A))

        tableau = np.vstack((t1, t2))

        tableau = np.array(tableau, dtype="float")

        return tableau

    def optimize(self):

        tableau = self.getTableau()

        # assume initial basis is not optimal
        optimal = False

        # keep track of iterations for display
        iter = 1
        # itermap = {0:np.dot(self.x,self.c)}

        while True:

            if self.minmax == "MAX":
                for profit in tableau[0, 2:]:
                    if profit > 0:
                        optimal = False
                        break
                    optimal = True
            else:
                for cost in tableau[0, 2:]:
                    if cost < 0:
                        optimal = False
                        break
                    optimal = True

            # if all directions result in decreased profit or increased cost
            if optimal == True:
                break

            # nth variable enters basis, account for tableau indexing
            if self.minmax == "MAX":
                n = tableau[0, 2:].tolist().index(np.amax(tableau[0, 2:])) + 2
            else:
                n = tableau[0, 2:].tolist().index(np.amin(tableau[0, 2:])) + 2

            # minimum ratio test, rth variable leaves basis
            minimum = 99999
            r = -1

            for i in range(1, len(tableau)):
                if tableau[i, n] > 0:
                    val = tableau[i, 1] / tableau[i, n]
                    if val < minimum:
                        minimum = val
                        r = i

            pivot = tableau[r, n]

            # perform row operations
            # divide the pivot row with the pivot element
            tableau[r, 1:] = tableau[r, 1:] / pivot

            # pivot other rows
            for i in range(0, len(tableau)):
                if i != r:
                    mult = tableau[i, n] / tableau[r, n]
                    tableau[i, 1:] = tableau[i, 1:] - mult * tableau[r, 1:]

            # new basic variable
            tableau[r, 0] = n - 2

            # itermap[iter] = np.dot(self.x,self.c)
            iter += 1

        self.x = np.array([0] * len(self.c), dtype=float)
        # save coefficients
        for key in range(1, (len(tableau))):
            if tableau[key, 0] < len(self.c):
                self.x[int(tableau[key, 0])] = tableau[key, 1]

        self.optimalValue = -1 * tableau[0, 1]

        return self.x, iter