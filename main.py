import calculadora

def main():
    suma = calculadora.suma(2,2)
    resta = calculadora.resta(2,2)
    mult = calculadora.multiplicar(2,2)
    div = calculadora.dividir(2,2)
    print("La suma es:" ,suma)
    print("La resta es:" ,resta)
    print("La miltiplicacion es:" ,mult)
    print("La divicion es:" ,div)

if __name__ == '__main__':
    main()