
from datetime import datetime
from validate_docbr import CPF

documento_cpf = CPF()


def coletar_dados():

      funcionario = {
          "nome" : input("Nome: "),
          "cpf" : input("CPF: "),
          "setor": input("Setor: "),
          "cidade" : input("Cidade: "),
          "modelo": input("Modelo: "),
          "imei" : input("IMEI: "),
          "valor" : float(input("Valor: ")),
          "cargo" : input("Cargo: ")
      }

      return funcionario

def formatar_string(dicionario):
    for campo, valor in dicionario.items():
        print(campo, valor)
        
    while True:

        string = input(f"{string}: ")
        if string.split() == "":                              # verifica se mesmo após remover os espaços no início e do fim, a variavel continua vazia
            print("Este campo não pode ser vazio!")     
            continue

        if any(char.isdigit() for char in string):            # verifica se "qualquer" caractere é um dígito (número) na variavel
            print("O campo não pode conter números!")
            continue

        if not string.replace(" ", "").isalpha():             # remove todos os espaços para verificar se a string possui caracteres especiais
            print("Digite apenas letras!")
            continue

        string = " ".join(string.split()).upper().strip()       # remove espaços extras no entre uma string e a outra 
        return string


def aplicar_mascara(valor, mascara):
    try:
        resultado = ""
        indice = 0

        for char in mascara:
            if char == "#":
                resultado += valor[indice]
                indice += 1
            else:
                resultado += char

        return resultado

    except IndexError:
        print("Erro")

#  regra para pegar mês atual 
def mes():
    meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
    mes = datetime.now().month
    return meses[mes - 1]

# # verifica e corrige ortografia
def nome():
    while True:

        nome = input("Nome: ")
        if nome.strip() == "":                              # verifica se mesmo após remover os espaços no início e do fim, a variavel continua vazia
            print("Este campo não pode ser vazio!")     
            continue

        if any(char.isdigit() for char in nome):            # verifica se "qualquer" caractere é um dígito (número) na variavel
            print("O campo não pode conter números!")
            continue

        if not nome.replace(" ", "").isalpha():             # remove todos os espaços para verificar se o nome possui caracteres especiais
            print("Digite apenas letras!")
            continue

        nome = " ".join(nome.split()).upper().strip()       # remove espaços extras no entre nome e sobrenome
        return nome


def cpf():
    while True: 
        cpf = input("CPF: ")
        if documento_cpf.validate(cpf):
            break
        print("CPF Inválido")
            
    return documento_cpf.mask(cpf) # retorna em outra variável o cpf formatado

        
def setor():
    while True:

        setor = input("Setor: ")
        if setor.strip() == "":                              # verifica se mesmo após remover os espaços no início e do fim, a variavel continua vazia
            print("Este campo não pode ser vazio!")     
            continue

        if any(char.isdigit() for char in setor):            # verifica se "qualquer" caractere é um dígito (número) na variavel
            print("O campo não pode conter números!")
            continue

        if not setor.replace(" ", "").isalpha():             # remove todos os espaços para verificar se o nome possui caracteres especiais
            print("Digite apenas letras!")
            continue

        setor = " ".join(setor.split()).upper().strip()
        return setor       # remove espaços extras no entre os espaços

def cargo():
    while True:
    
        cargo = input("Cargo: ")
        if cargo.strip() == "":                              # verifica se mesmo após remover os espaços no início e do fim, a variavel continua vazia
            print("Este campo não pode ser vazio!")     
            continue
    
        if any(char.isdigit() for char in cargo):            # verifica se "qualquer" caractere é um dígito (número) na variavel
            print("O campo não pode conter números!")
            continue
    
        if not cargo.replace(" ", "").isalpha():             # remove todos os espaços para verificar se o nome possui caracteres especiais
            print("Digite apenas letras!")
            continue
    
        cargo = " ".join(cargo.split()).title().strip()       # remove espaços extras no entre os espaços
        return cargo

def cidade():
    while True:
    
        cidade = input("Cidade: ")
        if cidade.strip() == "":                              # verifica se mesmo após remover os espaços no início e do fim, a variavel continua vazia
            print("Este campo não pode ser vazio!")     
            continue
    
        if any(char.isdigit() for char in cidade):            # verifica se "qualquer" caractere é um dígito (número) na variavel
            print("O campo não pode conter números!")
            continue
    
        if not cidade.replace(" ", "").isalpha():             # remove todos os espaços para verificar se o nome possui caracteres especiais
            print("Digite apenas letras!")
            continue
    
        cidade = " ".join(cidade.split()).upper().strip()       # remove espaços extras no entre os espaços
        return cidade  

def modelo():
        while True:

            modelo = input("Modelo: ")
            if modelo.strip() == "":                              # verifica se mesmo após remover os espaços no início e do fim, a variavel continua vazia
                print("Este campo não pode ser vazio!")     
                continue

            modelo = " ".join(modelo.split()).upper().strip()       # remove espaços extras no entre os espaços
            return modelo

def imei():
    while True:

        imei = input("IMEI: ")
        if imei.strip() == "":                              # verifica se mesmo após remover os espaços no início e do fim, a variavel continua vazia
            print("Este campo não pode ser vazio!")     
            continue

        if not imei.replace(" ", "").isdigit():
            print("Digite apenas números!")
            continue

        imei = " ".join(imei.split()).strip()
        imei = aplicar_mascara(imei, "######/##/######/#")

        return imei

def numero():
    while True:

        numero = input("Número (digite apenas números): ")

        if not numero.replace(" ", "").isdigit():
            print("Digite apenas números!")
            continue

        if numero.split() == "":
            numero = "S/N"

            return numero

        numero = " ".join(numero.split()).strip()
        numero = aplicar_mascara(numero, "(##) #####-####")

        return numero

def valores():
    total = float(input("Valor: "))
    parcela = total / 8
    return {
        "valor" : f"{total:,.2f}",
        "valor_parcela" : f"{parcela:,.2f}"
    }



    


