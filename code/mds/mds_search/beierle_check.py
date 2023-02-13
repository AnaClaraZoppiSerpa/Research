#The following matrices, found by Beierle \cite{LightweightGF22016}, are not specific of a finite field, i.e they are MDS for any field $GF(2^m)$, as long as some restrictions regarding $m$ and the $\alpha$ parameter are satisfied.

# Corpo finito genérico GF(2^m)
# Pra serem MDS, alpha != 0 e alpha != 1

#Matrices \eqref{mat:beierle-2x2} (inverse: \eqref{mat:beierle-2x2-inv}) and \eqref{mat:beierle-3x3} (inverse: \eqref{mat:beierle-3x3-inv}) are MDS for all $\alpha \neq 0, 1$.

def circ():
    pass

def alpha_power():
    pass

def alpha_sub(alpha, v):
    pass

alpha=0

beierle_2x2=[
    [1, alpha],
    [alpha, 1],
]

#\begin{equation}\label{mat:beierle-2x2}
#circ(1, \alpha) =
#\begin{bmatrix}
#1 & \alpha \\
#\alpha & 1
#\end{bmatrix}
#\end{equation}

negative_alpha=0

beierle_2x2_inv=[
    [1, negative_alpha],
    [negative_alpha, 1],
]

#\begin{equation}\label{mat:beierle-2x2-inv}
#\frac{1}{1-\alpha^2} \cdot
#\begin{bmatrix}
#1 & -\alpha\\
#-\alpha & 1
#\end{bmatrix}
#\end{equation}

alpha=0

beierle_3x3=[
    [1, 1, alpha],
    [alpha, 1, 1],
    [1, alpha, 1],
]

#\begin{equation}\label{mat:beierle-3x3}
#circ(1, 1, \alpha) =
#\begin{bmatrix}
#1 & 1 & \alpha \\
#\alpha & 1 & 1 \\
#1 & \alpha & 1
#\end{bmatrix}
#\end{equation}

one_minus_alpha=0
alpha_pow_2=0
alpha_pow_2_minus_1=0

beierle_3x3_inv=[
    [one_minus_alpha & alpha_pow_2_minus_1 & one_minus_alpha],
    [one_minus_alpha & one_minus_alpha & alpha_pow_2_minus_1],
    [alpha_pow_2_minus_1 & one_minus_alpha & one_minus_alpha],
]

#\begin{equation}\label{mat:beierle-3x3-inv}
#\frac{1}{(1-\alpha)-(\alpha-1)+\alpha(\alpha^2-1)} \cdot
#\begin{bmatrix}
#1-\alpha & \alpha^2-1 & 1-\alpha \\
#1-\alpha & 1-\alpha & \alpha^2-1 \\
#\alpha^2-1 & 1-\alpha & 1-\alpha
#\end{bmatrix}
#\end{equation}

alpha_pow_minus_2 = 0

beierle_4x4=circ(1, 1, alpha, alpha_pow_minus_2)

#Matrix \eqref{mat:beierle-4x4} is MDS for $m > 3$ and any $\alpha$ that is not a root of the following polynomials:

#\begin{align*}
#x\\
#x + 1\\
#x^2+x+1\\
#x^3+x+1\\
#x^3+x^2+1\\
#x^4+x^3+x^2+x+1\\
#x^5+x^2+1
#\end{align*}

#% m > 3
#% alpha não pode ser raiz de
#% x
#% x + 1
#% x^2+x+1
#% x^3+x+1
#% x^3+x^2+1
#% x^4+x^3+x^2+x+1
#% x^5+x^2+1
#\begin{equation}\label{mat:beierle-4x4}
#circ(1, 1, \alpha, \alpha^{-2})
#\end{equation}

beierle_5x5=circ(1,1,alpha,alpha_pow_minus_2,alpha)

#Matrix \eqref{mat:beierle-5x5} is MDS for $m > 3$ and any $\alpha$ that is not a root of the following polynomials:

#\begin{align*}
#x\\
#x+1\\
#x^2+x+1\\
#x^3+x+1\\
#x^3+x^2+1\\
#x^4+x+1\\
#x^4+x^3+1
#\end{align*}

#% m > 3
#% alpha não pode ser raiz de
#% x
#% x+1
#% x^2+x+1
#% x^3+x+1
#% x^3+x^2+1
#% x^4+x+1
#% x^4+x^3+1
#\begin{equation}\label{mat:beierle-5x5}
#circ(1, 1, \alpha, \alpha^{-2}, \alpha)
#\end{equation}

#Matrix \eqref{mat:beierle-6x6} is MDS for $m > 5$. For this matrix, we refer the reader to \cite{LightweightGF22016}, because the list of restricted polynomials is bigger.

#% m > 5, see Beierle for the list of restrictions

alpha_pow_minus_1=0
alpha_pow_3=0

beierle_6x6=circ(1, alpha, alpha_pow_minus_1, alpha_pow_minus_2, 1, alpha_pow_3)

#\begin{equation}\label{mat:beierle-6x6}
#circ(1, \alpha, \alpha^{-1}, \alpha^{-2}, 1, \alpha^3)
#\end{equation}

#Matrix \eqref{mat:beierle-7x7} is MDS for $m > 5$. For this matrix, we refer the reader to \cite{LightweightGF22016}, because the list of restricted polynomials is bigger.

#% m > 5, see Beierle for the list of restrictions

beierle_7x7=circ(1, 1, alpha_pow_minus_2, alpha, alpha_pow_2, alpha_pow_minus_2)

#\begin{equation}\label{mat:beierle-7x7}
#circ(1, 1, \alpha^{-2}, \alpha, \alpha^2, \alpha, \alpha^{-2})
#\end{equation}

#Matrix \eqref{mat:beierle-8x8} is MDS for $m > 7$. For this matrix, we refer the reader to \cite{LightweightGF22016}, because the list of restricted polynomials is bigger.

alpha_pow_4 = 0

beierle_8x8=circ(1,1,alpha_pow_minus_1,alpha,alpha_pow_minus_1,alpha_pow_3,alpha_pow_4,)

#% m > 7, see Beierle for the list of restrictions
#\begin{equation}\label{mat:beierle-8x8}
#circ(1, 1, \alpha^{-1}, \alpha, \alpha^{-1}, \alpha^3, \alpha^{4}, \alpha^{-3})
#\end{equation}