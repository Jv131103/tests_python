def soma(x, y):
    """
    Função que retorna a soma de dois números

    PS: Precisam ser do tipo:

        > int
        > float
        > cloplex

    Em outros casos gerará um ValueError

    EX de teste:

    Teste: python -m doctest -v test1.py

    OU

    if __name__ == "__main__":
        import doctest
        doctest.testmod()  # roda doctests encontrados no módulo

    >>> soma(2, 2)
    4
    >>> soma(3.5, 2)
    5.5
    >>> soma(2, 5.9)
    7.9
    >>> soma(2+0j, 2)
    (4+0j)
    >>> soma(-1, 1)
    0
    >>> soma("10", 10)
    Traceback (most recent call last):
    ...
    AssertionError: x precisa ser int, float ou complex
    """
    assert isinstance(x, (int, float, complex)), \
        "x precisa ser int, float ou complex"
    assert isinstance(x, (int, float, complex)), \
        "y precisa ser int, float ou complex"
    return x + y
