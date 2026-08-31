from docxtpl import DocxTemplate
from datetime import datetime
from functions import mes, cpf, nome, setor, cargo, cidade, modelo, imei, numero, valores
# from functions import formatar_string, coletar_dados
from docx2pdf import convert
from tkinter import filedialog, Tk
from pathlib import Path
from time import sleep


doc = DocxTemplate("modelo.docx")  # Abrindo Modelo Word

nome_funcionario = nome()    # pegando nome para definir o nome do documento
    
# dicionario dos campos que serão alterados
referencias = {
    "nome" : nome_funcionario,
    "cpf" : cpf(),
    "setor" : setor(),
    "cidade" : cidade(),
    "modelo" : modelo(),
    "imei" : imei(),
    "numero" : numero(),
    "cargo" : cargo(),
    "dia" : datetime.now().day,
    "mes" : mes(),
    "ano" : datetime.now().year
}

# passando valo do celular e da parcela
valores = valores()
informacoes = referencias | valores 


doc.render(informacoes)     # renderizando os campos para o documento


# salvando docx word na pasta "termos_word"
pasta_word = Path("termos_word")
pasta_word.mkdir(exist_ok=True)

nome_arquivo = (f"TERMO_{nome_funcionario}.docx")
caminho_docx = pasta_word / nome_arquivo
doc.save(str(caminho_docx))

# convertento para PDF
# Escolhendo destino
root = Tk()
root.withdraw()
pasta_pdf = filedialog.askdirectory(title="Escolha o destino do PDF")

if pasta_pdf:  # usuário pode cancelar a escolha, então vale checar
    caminho_pdf = Path(pasta_pdf) / caminho_docx.with_suffix(".pdf").name

    print("Convertendo para PDF...")
    convert(str(caminho_docx), str(caminho_pdf))
    sleep(2)
    print(f"PDF salvo em {caminho_pdf}")
else:
    print("Conversão cancelada: nenhuma pasta selecionada.")
