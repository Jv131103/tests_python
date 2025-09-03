"""
1 - Receber um número inteiro

2 - Saber se o número é multiplo de 3 ou 5: baconcomovos

3 - Saber se um número não é multiplo nem de 3 e nem de 5: passafome

4 - Saber se o número é multiplo de 3: bacon

5 - Saber se o número é múltiplo de 5: ovos

"""


def ismultiple_3_or_5(n):
    assert isinstance(n, int), "n deve ser int"
    if n % 3 == 0 and n % 5 == 0:
        return "baconcomovos"
    elif n % 3 == 0:
        return "bacon"
    elif n % 5 == 0:
        return "ovos"
    return "passafome"
