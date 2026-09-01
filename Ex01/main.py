#########################################################
############ ENTREGA EX 01: PI 4 - COMPUTAÇÃO CIENTÍFICA
# PEDRO HENRIQUE PATRICIO DE SOUZA
# JOAO PEDRO BARBOSA MOZ
# CAUA CARVALHO
#########################################################

import Conversoes

def TipoInput():
    print("ESCREVA O TIPO DE DADO QUE SERA DIGITADO:\n")
    print("JARDA\n")
    print("METRO\n")
    print("PE\n")

def TipoConverter():
    print("ESCREVA PARA QUE TIPO DE DADO QUE SERA DIGITADO:\n")
    print("JARDA\n")
    print("METRO\n")
    print("PE\n")

TipoInput()
TipoEntrada = input("> ")
DadoEntrada = input("Digite o valor para ser convertido:")

TipoConverter()
TipoConvertido = input("> ")

if (TipoEntrada.upper() == "JARDA" and TipoConvertido.upper() == "METRO"):
    DadoSaida = Conversoes.ConverteJardaMetro(float(DadoEntrada))
elif (TipoEntrada.upper() == "JARDA" and TipoConvertido.upper() == "PE"):
    DadoSaida = Conversoes.ConverteJardaPe(float(DadoEntrada))
elif (TipoEntrada.upper() == "METRO" and TipoConvertido.upper() == "JARDA"):
    DadoSaida = Conversoes.ConverteMetroJarda(float(DadoEntrada))
elif (TipoEntrada.upper() == "METRO" and TipoConvertido.upper() == "PE"):
    DadoSaida = Conversoes.ConverteMetroPe(float(DadoEntrada))
elif (TipoEntrada.upper() == "PE" and TipoConvertido.upper() == "METRO"):
    DadoSaida = Conversoes.ConvertePeMetro(float(DadoEntrada))
elif (TipoEntrada.upper() == "PE" and TipoConvertido.upper() == "JARDA"):
    DadoSaida = Conversoes.ConvertePeJarda(float(DadoEntrada))
else:
    print("Nenhum dos dados inseridos estao corretos.\n")
    DadoSaida = 0
    DadoEntrada = 0
    TipoEntrada = "Desconhecido"
    TipoConvertido = "Desconhecido"

print(f"A conversao de {TipoEntrada} para {TipoConvertido} é {DadoSaida}")
