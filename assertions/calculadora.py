def soma(x, y):
    return x + y


def soma2(x, y):
    assert isinstance(x, (int, float)), f"{x} não é um tipo válido\n\
        TIPO DE {x}: {type(x).__name__}"
    assert isinstance(y, (int, float)), f"{y} não é um tipo válido\n\
        TIPO DE {y}: {type(y).__name__}"
    return x + y
