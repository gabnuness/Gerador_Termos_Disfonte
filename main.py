from datetime import datetime
from pathlib import Path

from tkinter import Tk, filedialog

from docx2pdf import convert
from docxtpl import DocxTemplate

from functions import campo_formatado, cpf, imei, mes, modelo, numero, valores


BASE_DIR = Path(__file__).resolve().parent
MODELO_PATH = BASE_DIR / "modelo.docx"
PASTA_WORD = BASE_DIR / "termos_word"


def coletar_informacoes():
    nome_funcionario = campo_formatado("Nome: ")

    referencias = {
        "nome": nome_funcionario,
        "cpf": cpf(),
        "setor": campo_formatado("Setor: "),
        "cidade": campo_formatado("Cidade: "),
        "modelo": modelo(),
        "imei": imei(),
        "numero": numero(),
        "cargo": campo_formatado("Cargo: "),
        "dia": datetime.now().day,
        "mes": mes(),
        "ano": datetime.now().year,
    }

    return referencias | valores()


def gerar_documento(informacoes):
    documento = DocxTemplate(MODELO_PATH)
    documento.render(informacoes)

    PASTA_WORD.mkdir(exist_ok=True)
    nome_arquivo = f"TERMO_{informacoes['nome']}.docx"
    caminho_docx = PASTA_WORD / nome_arquivo
    documento.save(caminho_docx)

    return caminho_docx


def escolher_pasta_pdf():
    root = Tk()
    root.withdraw()
    pasta_pdf = filedialog.askdirectory(title="Escolha o destino do PDF")
    root.destroy()
    return Path(pasta_pdf) if pasta_pdf else None


def converter_para_pdf(caminho_docx, pasta_pdf):
    caminho_pdf = pasta_pdf / caminho_docx.with_suffix(".pdf").name
    print("Convertendo para PDF...")
    convert(str(caminho_docx), str(caminho_pdf))

    if not caminho_pdf.exists():
        raise FileNotFoundError("A conversão terminou sem criar o arquivo PDF.")

    return caminho_pdf


def main():
    informacoes = coletar_informacoes()
    caminho_docx = gerar_documento(informacoes)
    pasta_pdf = escolher_pasta_pdf()

    if pasta_pdf is None:
        print("Conversão cancelada: nenhuma pasta selecionada.")
        return

    caminho_pdf = converter_para_pdf(caminho_docx, pasta_pdf)
    print(f"PDF salvo em {caminho_pdf}")


if __name__ == "__main__":
    main()
