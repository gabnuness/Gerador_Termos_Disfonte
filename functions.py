from decimal import Decimal, InvalidOperation
from datetime import datetime

import phonenumbers
from validate_docbr import CPF

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
    quantidade_digitos = mascara.count("#")
    if len(valor) != quantidade_digitos:
        raise ValueError("O valor não corresponde ao tamanho da máscara.")

    resultado = ""
    indice = 0

    for char in mascara:
        if char == "#":
            resultado += valor[indice]
            indice += 1
        else:
            resultado += char

    return resultado

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

        texto_imei = input("IMEI: ").replace(" ", "")

        if texto_imei.strip() == "":                              # verifica se mesmo após remover os espaços no início e do fim, a variavel continua vazia
            print("Este campo não pode ser vazio!")     
            continue

        if not texto_imei.isdigit():
            print("Digite apenas números!")
            continue

        if 15 < len(texto_imei) or  len(texto_imei) < 15:
            print("IMEI inválido")
            continue

        imei_limpo = aplicar_mascara(texto_imei, "######/##/######/#")

        return imei_limpo

def numero():
    while True:
        possui_numero = input("Possui Número (S/N)?: ").strip().upper() # remove espaços nas extremidades e deixa maíuscula

        if possui_numero == "N":
            return "S/N"            # sem numero

        if possui_numero != "S":        
            print("Resposta inválida. Digite S para sim ou N para não.")
            continue
        
        while True:
            texto_numero = input("Digite o número de telefone: ").strip()

            if not texto_numero:
                print("O número não pode ser vazio.")
                continue

            try:
                numero_informado = phonenumbers.parse(texto_numero, "BR")   # aqui o parse apenas interpreta, com o codigo nacional no numero ou com o segundo parametro
            except phonenumbers.NumberParseException:                       # verifica se nao foi passado outro valor sem ser o numero
                print("Número inválido. Digite um telefone válido.")
                continue

            if not phonenumbers.is_valid_number(numero_informado):
                print("Número inválido. Digite um telefone válido.")
                continue

            # formata o numero 'formata string'
            return phonenumbers.format_number(
                numero_informado,
                phonenumbers.PhoneNumberFormat.NATIONAL # aqui só informa o formato, no caso o padrão nacional, sem o código do país
            )

def valores():
    while True:
        texto_valor = input("Valor: ").strip()

        if not texto_valor:
            print("Esse campo não pode ser vazio!")
            continue

        try:
            valor = Decimal(
                texto_valor.replace(".", "").replace(",", ".")
            )
        except InvalidOperation:
            print("Digite apenas números!")
            continue

        if not valor.is_finite() or valor <= 0:
            print("O valor deve ser maior que zero.")
            continue

        valor_parcela = valor / Decimal("8")

        return {
            "valor": f"{valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."),
            "valor_parcela": f"{valor_parcela:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
        }
