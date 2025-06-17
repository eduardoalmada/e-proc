
# Assistente Jurídico - Consulta de Processos TJ-RJ

Este projeto é um sistema de demonstração que responde automaticamente pelo WhatsApp sobre o andamento de processos no TJ-RJ.

## Componentes

- Flask: Backend
- Simulação de scraping do TJ-RJ
- Integração com Typebot ou Evolution API

## Como usar

1. Instale as dependências:
```
pip install -r requirements.txt
```

2. Rode o servidor localmente:
```
python app.py
```

3. Use o endpoint `/webhook` para enviar um JSON com:
```json
{ "mensagem": "0000000-00.2023.8.19.0001" }
```

4. O sistema responde com dados simulados.

## Deploy sugerido

- Subir no [Render.com](https://render.com) como Web Service
- Porta 10000
- Webhook do Typebot ou Evolution API aponta para `/webhook`
