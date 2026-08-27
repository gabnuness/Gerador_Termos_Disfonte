from docxtpl import DocxTemplate
from datetime import datetime
from functions import mes, cpf, nome, setor, cargo, cidade, modelo, imei, numero, valores
from functions import formatar_string, coletar_dados

doc = DocxTemplate("modelo.docx")  # Abrindo Modelo Word


# funcionario = coletar_dados()

    
# dicionario dos campos que serão alterados
referencias = {
    "nome" : nome(),
    "cpf" : cpf(),
    "setor" : setor(),
    "cidade" : cidade(),
    "modelo" : modelo(),
    "imei" : imei(),
    "numero" : numero(),
    **valores,
    "cargo" : cargo(),
    "dia" : datetime.now().day,
    "mes" : mes(),
    "ano" : datetime.now().year
}

doc.render(referencias) # renderizando os campos para o documento
doc.save(f"TERMO_{nome}.docx")






