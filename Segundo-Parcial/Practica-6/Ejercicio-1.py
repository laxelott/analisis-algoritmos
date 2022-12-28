def comparar(a1, a2):
    with open(a1) as file:
        secuencia1 = file.read()
    with open(a2) as file:
        secuencia2 = file.read()
        
    return lcs(secuencia1, secuencia2, len(secuencia1), len(secuencia2))

# Longest Common Sequence
def lcs(sec1, sec2, len1, len2):
    if len1 == 0 or len2 == 0:
        # Límite
        return 0
    elif sec1[len1-1] == sec2[len2-1]:
        # Si hay secuencia común, sigue sumando
        return 1 + lcs(sec1, sec2, len1-1, len2-1)
    else:
        # Si no, sigue buscando
        return max(lcs(sec1, sec2, len1, len2-1), lcs(sec1, sec2, len1-1, len2))

print(comparar("archivo1.txt", "archivo2.txt"))