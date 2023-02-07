from metrics_and_flags import *

#% Duwal

#The following matrices have been reported by Duval and Leurent \cite{LwCircuits2018}.

#% GF(2^2)
#% x^2+x+1

duwal_1_int = [[2, 1, 1],[1, 2, 1],[1, 1, 2]]
duwal_2_int = [[3, 2, 2],[2, 3, 2],[2, 2, 3]]

#% GF(2^3) eu acho, por causa do textinho da seção 5 (Results) que fala k = 3 e F_2^k. Tem que ver qual o polinômio irredutível só.

duwal_3_int = [[2, 1, 3],[1, 1, 1],[3, 1, 2]]
duwal_3_inv_int = [[3, 1, 2],[1, 1, 1],[2, 1, 3]]
duwal_4_int = [[3, 1, 3],[1, 1, 2],[2, 1, 1]]
duwal_5_int = [[2, 1, 1],[1, 2, 1],[1, 1, 2]]

#% Table 4
#% GF(2^4) pras que têm número, NA pras outras porque pode instanciar com outro k aparentemente
#% O que é alfa, beta, gama?
#% alfa é x, beta é x^(k+1), gama é x^(k+1)^2 - confirmar isso aqui

duwal_6_int = [[2, 2, 3, 1], [1, 3, 6, 4],[3, 1, 4, 4],[3, 2, 1, 3]]

def ffsum():
    pass

def ffsum3():
    pass

alpha=0
gamma=0
beta=0

duwal_7 = [
    [beta, 1, beta+1, 1],
    [gamma, alpha, gamma, ffsum(alpha,1)],
    [gamma, ffsum(alpha,1), ffsum(gamma,1), ffsum3(alpha,gamma,1)],
    [ffsum(beta,gamma), 1, ffsum3(beta,gamma,1), ffsum(gamma,1)]
    ]

duwal_8_int = [[2, 2, 3, 1],[1, 3, 6, 4],[3, 1, 4, 4],[3, 2, 1, 3]]
duwal_9_int = [[5, 7, 1, 3],[4, 6, 1, 1],[1, 3, 5, 7],[1, 1, 4, 6]]
duwal_10_int = [[6, 7, 1, 5],[2, 3, 1, 1],[1, 5, 6, 7],[1, 1, 2, 3]]
duwal_11_int = [[3, 2, 1, 3],[2, 3, 1, 1],[4, 3, 6, 4],[1, 1, 4, 6]]

def ffsum():
    pass

alpha=0
gamma=0
beta=0

duwal_12 = [
    [ffsum(alpha,1), alpha, ffsum(gamma,1), ffsum(gamma,1)],
    [beta, ffsum(beta,1), 1, beta],
    [1, 1, gamma, ffsum(gamma,1)],
    [alpha, ffsum(alpha,1), ffsum(gamma,1), gamma]
    ]

duwal_13_int = [[1, 2, 4, 3],[2, 3, 2, 3],[3, 3, 5, 1],[3, 1, 1, 3]]

alpha=0
gamma=0
beta=0
alphainv=0

duwal_14 = [
    [ffsum(alpha,alphainv), alpha, 1, 1],
    [1, ffsum(alpha,1), alpha, alphainv],
    [ffsum(1,alphainv), 1, 1, ffsum(1,alphainv)],
    [alphainv, alphainv, ffsum(1,alphainv), 1]
    ]