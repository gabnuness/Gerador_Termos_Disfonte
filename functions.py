from datetime import datetime
from validate_docbr import CPF
import subprocess

# formatar strings (nome, setor, cargo e cidade)
def campo_formatado(campo):
    while True:

        campo = input(campo)
        if campo.strip() == "":                              # verifica se mesmo após remover os espaços no início e do fim, a variavel continua vazia
            print("Este campo não pode ser vazio!")     
            continue

        if any(char.isdigit() for char in campo):            # verifica se "qualquer" caractere é um dígito (número) na variavel
            print("O campo não pode conter números!")
            continue

        if not campo.replace(" ", "").isalpha():             # remove todos os espaços para verificar se o nome possui caracteres especiais
            print("Digite apenas letras!")
            continue

        campo = " ".join(campo.split()).upper().strip()
        return campo       # remove espaços extras no entre os espaços

# criando documento para verificação
documento_cpf = CPF()

# verifica se o CPF é valido 
def cpf():
    while True: 
        cpf = input("CPF: ")
        if documento_cpf.validate(cpf):
            break
        print("CPF Inválido")
            
    return documento_cpf.mask(cpf) # retorna em outra variável o cpf formatado

# função para formatar espaçamentos ou caracteres do IMEI, Número de Telefone ou outros... 
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

# regra para pegar mês atual 
def mes():
    meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
    mes = datetime.now().month
    return meses[mes - 1]

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

        if 15 < len(imei) or  len(imei) < 15:
            print("IMEI inválido")
            continue


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
    possui_numero = bool(input("Possui número? (S/N): ").strip().upper())
    if possui_numero:
        while True:
            if possui_numero:
                numero = input("Número(digite apenas números): ")

                if 11 < len(numero) or len(numero) > 11:
                    print("Número inválido!")
                    continue

                if not numero.replace(" ", "").isdigit():
                    print("Digite apenas números!")

def valores():
    while True:
        try:
            valor = float(input("Valor: "))
            valor = str(valor)

            if valor.strip() == "":
                print("Esse campo não pode ser vazio!")
                continue

            valor = float(valor)
            valor_parcela = valor / 8

            return {
            "valor": f"{valor:_.2f}".replace(".", ",").replace("_", "."),
            "valor_parcela": f"{valor_parcela:_.2f}".replace(".", ",").replace("_", ".")
            }
        
        except ValueError:
            print("Digite apenas números!")

numero = numero()
print(f"Número: {numero}")

