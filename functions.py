
from datetime import datetime
from validate_docbr import CPF

documento_cpf = CPF()

#  regra para pegar mês atual 
def mes():
    meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
    mes = datetime.now().month
    return meses[mes - 1]

# verifica e corrige ortografia
def nome():
    while True:

        nome = input("Nome: ")
        if nome.split() == "":                              # verifica se mesmo após remover os espaços no início e do fim, a variavel continua vazia
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

# verifica cpf        
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
        if setor.split() == "":                              # verifica se mesmo após remover os espaços no início e do fim, a variavel continua vazia
            print("Este campo não pode ser vazio!")     
            continue

        if any(char.isdigit() for char in setor):            # verifica se "qualquer" caractere é um dígito (número) na variavel
            print("O campo não pode conter números!")
            continue

        if not setor.replace(" ", "").isalpha():             # remove todos os espaços para verificar se o nome possui caracteres especiais
            print("Digite apenas letras!")
            continue

        setor = " ".join(setor.split()).upper().strip()       # remove espaços extras no entre nome e sobrenome
        return setor

def cargo():
    while True:
    
        cargo = input("Cargo: ")
        if cargo.split() == "":                              # verifica se mesmo após remover os espaços no início e do fim, a variavel continua vazia
            print("Este campo não pode ser vazio!")     
            continue
    
        if any(char.isdigit() for char in cargo):            # verifica se "qualquer" caractere é um dígito (número) na variavel
            print("O campo não pode conter números!")
            continue
    
        if not cargo.replace(" ", "").isalpha():             # remove todos os espaços para verificar se o nome possui caracteres especiais
            print("Digite apenas letras!")
            continue
    
        cargo = " ".join(cargo.split()).title().strip()       # remove espaços extras no entre nome e sobrenome
        return cargo

def cidade():
    while True:
    
        cidade = input("Cidade: ")
        if cidade.split() == "":                              # verifica se mesmo após remover os espaços no início e do fim, a variavel continua vazia
            print("Este campo não pode ser vazio!")     
            continue
    
        if any(char.isdigit() for char in cidade):            # verifica se "qualquer" caractere é um dígito (número) na variavel
            print("O campo não pode conter números!")
            continue
    
        if not cidade.replace(" ", "").isalpha():             # remove todos os espaços para verificar se o nome possui caracteres especiais
            print("Digite apenas letras!")
            continue
    
        cidade = " ".join(cidade.split()).upper().strip()       # remove espaços extras no entre nome e sobrenome
        return cidade  

def formatar_string(string):
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