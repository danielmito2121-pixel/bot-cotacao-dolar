# 💵 Bot de Cotação do Dólar

Bot em Python que envia automaticamente a cotação do dólar via Telegram.

## O que faz
- Busca a cotação do dólar em tempo real
- Envia mensagem automática no Telegram todo dia às 9h e 18h

## Tecnologias usadas
- Python 3
- python-telegram-bot
- requests
- schedule

## Como usar

### 1. Instale as dependências
pip install requests python-telegram-bot schedule

### 2. Configure o bot
No arquivo `bot_cotacao.py`, substitua:
- `TOKEN` pelo token do seu bot (obtido no @BotFather)
- `CHAT_ID` pelo seu chat ID (obtido no @userinfobot)

### 3. Execute
python bot_cotacao.py

## Autor
Daniel — estudante de Engenharia de Software
