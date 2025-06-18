
def consultar_processo(numero_processo):
    # Simulação para demonstração
    processos_demo = {
        "0000000-00.2023.8.19.0001": {
            "parte": "Maria Silva x Estado do RJ",
            "assunto": "Aposentadoria por invalidez",
            "situacao": "Em andamento",
            "ultima_movimentacao": "Sentença proferida em 15/06/2025"
        },
        "0800620-36.2021.8.19.0002": {
            "parte": "João da Silva x INSS",
            "assunto": "Auxílio-doença",
            "situacao": "Em andamento",
            "ultima_movimentacao": "Concluso para decisão em 12/06/2025"
        }
    }
    return processos_demo.get(numero_processo)
