
def consultar_processo(numero_processo):
    # Esta é uma simulação para demonstração
    # Na versão final, usar Selenium para acessar o TJ-RJ e coletar dados reais
    processos_demo = {
        "0000000-00.2023.8.19.0001": {
            "partes": "Maria Silva x Estado do RJ",
            "situacao": "Em andamento",
            "movimentacao": "Sentença proferida em 15/06/2025"
        }
    }
    processo = processos_demo.get(numero_processo)
    if processo:
        return f"Nome das partes: {processo['partes']}\nSituação: {processo['situacao']}\nÚltima movimentação: {processo['movimentacao']}"
    else:
        return "Número de processo não encontrado para demonstração."
