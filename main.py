from docxtpl import DocxTemplate
from datetime import datetime
from functions import mes, cpf, nome, setor, cargo, cidade
from functions import formatar_string

doc = DocxTemplate("modelo.docx")  # Abrindo Modelo Word

modelo = input("Modelo: ")
imei = input("IMEI: ")
numero = input("Número: ")
valor = float(input("Valor: "))
valor_parcela = valor / 8


# dicionario dos campos que serão alterados
referencias = {
    "nome" : nome(),
    "cpf" : cpf(),
    "setor" : setor(),
    "cidade" : cidade(),
    "modelo" : modelo,
    "imei" : imei,
    "numero" : numero,
    "valor" : (f"valor:,.2f"),
    "cargo" : cargo(),
    "valor_parcela" : valor_parcela,
    "dia" : datetime.now().day,
    "mes" : mes(),
    "ano" : datetime.now().year
}

doc.render(referencias) # renderizando os campos para o documento
doc.save(f"TERMO_{nome}.docx")






