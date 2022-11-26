
def imprimi(funcao):
    def wrapper(*args):
        print(f'CAPITAL: {args[0]} - TAXA: {args[1]} - PRAZO: {args[2]}')
        print(f'RESULTADO: ', end='')
        funcao(*args)
        return 
    return wrapper


@imprimi
def juros_simples(capital, taxa, prazo):
    resultado = capital * (taxa / 100) * prazo
    return print(resultado)


juros_simples(1000, 5, 6)