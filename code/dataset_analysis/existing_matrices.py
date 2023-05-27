# Matrizes que já estão no LaTeX
# Instâncias das matrizes genéricas - consigo achá-las nos logs dos cálculos de custo
# Uma ideia é verificar se a matriz obedece alguma das fórmulas genéricas
# Mas talvez essa ideia possa ser citada como uma verificação futura do trabalho
# A das instâncias e do próprio LaTeX é mais suave

# Preciso apenas dos coeficientes para um experimento com respeito a custo de encriptação

# A avaliação de MDS pressupõe um corpo finito, posso iniciar com GF(2^4) e GF(2^8) como padrão.

# Se não for implementar a checagem das que estão no LaTeX em formato de equação, explicar exatamente como foi o processo de busca e que isso precisaria ser verificado ainda.

# Precisa ver também como fazer para matrizes que estejam denotadas como circ(...), had(...), hc(...) e por aí vai.

# Mas, por enquanto, só implementar um lookup que descobre que uma certa matriz já está na lista deve funcionar.

# Dá para fazer isso com algumas matrizes pequenas mesmo.

# Pior caso a matriz é 32x32, existem 1935 matrizes na lista. Isso dá 32*32*1935 comparações no pior caso, dá para fazer rápido.

