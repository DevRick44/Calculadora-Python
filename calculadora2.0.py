from operator import add, truediv, mul, sub, pow
import os
            
listaint, listasimb = [], []
simb = {"+": add, "-": sub, "*": mul, "/": truediv, "^": pow, "!" : pow}
simbol = ["*", "/", "^", "!", "-", "+", "="]
i1, i2, a = 0, 0, 0
resposta="Não defenido"

print("a")
os.system('cls')

def findOpe(operacao, simbolos = []):
    for i in range (0, len(simbolos)) :
        if (operacao.find(simbolos[i],1)>-1) :
            return str(simbolos[i])

def pararCalculador(operacao) :
    if operacao.find("=")>-1 :
        return "parar"

def conta(operacao) :
    try :
        fimOpe = 0
        a=findOpe(operacao, simbol)
        primNum = int(operacao[:operacao.find(a,1)])
        segNum = int(operacao[operacao.find(a,1)+1:len(operacao)])
        simbOpe = simb[a]
        if a == "!" :
            fimOpe = simbOpe(primNum, (1/segNum))
        else :
            fimOpe = simbOpe(primNum, segNum)
        return fimOpe
    except :
        return "Algo deu errado tente novamente"

while True:

    print("- para subtração\t + para soma\n* para multipicação\t/ para divizão\n^ para potencia\t\t! para raiz\n= para finalizar a conta\n")
    print("\nFormato (Primeiro Número + Operador + Segundo Número)")
    opera = str(input("\nQual a conta que deseja realizar : "))
    if pararCalculador(opera) == "parar" :
        os.system('cls')
        print("\nUltimo resultado : ", resposta)
        input("\nPrecione enter para continuar\n\n_")
        os.system('cls')
        break
    os.system('cls')
    print("\nResultado = ", conta(opera))
    resposta = conta(opera)
    input("\nPrecione enter para continuar\n\n_")
    os.system('cls')