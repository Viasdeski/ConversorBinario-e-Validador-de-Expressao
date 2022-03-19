from classes import Pilha

def validaExpressao(expr):

    expr = list(expr)

    p = Pilha()

    simbInicia = ['{', '[', '('] 
    simbFecha = ['}', ']', ')']

    for simb in expr:        
        
        if simb in simbInicia:
            p.push(simb)
            continue

        if simb in simbFecha:
            indice = simbFecha.index(simb)
            if p.peek() == simbInicia[indice]:
                p.pop()                
            else:
                print("Símbolo não encotrado")                       

    if len(p) > 0:
        return "Expressão Inválida"
    else:
        return "Expressão Válida"

if __name__ == "__main__":
    expr = list(input("Digite a expressão a ser validada: "))
    print(validaExpressao(expr))
