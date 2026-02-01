import os
from fpdf import FPDF

# 1. FUNÇÃO QUE GERA O PDF (Coloquei aqui dentro para não dar erro de pasta!)
def salvar_como_pdf(lista_triagem):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", "B", 16)
    pdf.cell(200, 10, "RELATÓRIO DE TRIAGEM LOGÍSTICA", ln=True, align="C")
    pdf.ln(10)
    pdf.set_font("Arial", size=12)
    
    for item in lista_triagem:
        pdf.cell(200, 10, txt=item, ln=True)
    
    pdf.output("Relatorio_Triagem.pdf")
    print("\n[ARQUIVO PDF GERADO COM SUCESSO!]")

# 2. SEU CÓDIGO DE LÓGICA
print("-" * 30)
print("SISTEMA DE ANÁLISE DE RISCO")
print("-" * 30)

triagem = []

for i in range(3):
    mercadoria = input(f"\nNOME DA MERCADORIA {i+1}: ")
    valor = float(input(f"VALOR DA MERCADORIA {i+1}: "))

    if valor > 5000:
        resultado = f"{mercadoria}: R$ {valor} - [ALTO RISCO - REQUER ESCOLTA]"
    else:
        resultado = f"{mercadoria}: R$ {valor} - [RISCO BAIXO - LIBERADO]"
    
    triagem.append(resultado)
    print("Analisando...")

# 3. FINALIZAÇÃO
print("\n" + "=" * 30)
print("PROCESSANDO RELATÓRIO...")
salvar_como_pdf(triagem)
print("[SISTEMA EM STANDBY]")
print("=" * 30)