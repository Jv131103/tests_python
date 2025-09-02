from calculadora import soma2

try:
    print(soma2('15', 15))
except AssertionError as ae:
    print(f"Conta inválida: {ae}")
except TypeError as e:
    print("Conta inválida!")
    print(e)
