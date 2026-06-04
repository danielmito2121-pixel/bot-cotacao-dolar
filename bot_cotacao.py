import requests
import schedule
import time
import asyncio
from telegram import Bot

# --- CONFIGURAÇÕES ---
TOKEN = "8778457626:AAFFzlmO6XakEknfIWgB3dcAPWQhCtEsIfc"
CHAT_ID = "6773497676"

# --- FUNÇÕES ---
def buscar_cotacao():
    url = "https://economia.awesomeapi.com.br/json/last/USD-BRL"
    resposta = requests.get(url)
    dados = resposta.json()
    cotacao = float(dados["USDBRL"]["bid"])
    return cotacao

async def enviar_mensagem(texto):
    bot = Bot(token=TOKEN)
    await bot.send_message(chat_id=CHAT_ID, text=texto)

def tarefa():
    try:
        cotacao = buscar_cotacao()
        mensagem = f"💵 Dólar agora: R$ {cotacao:.2f}"
        asyncio.run(enviar_mensagem(mensagem))
        print(f"Enviado: {mensagem}")
    except Exception as e:
        print(f"Erro: {e}")

# --- AGENDAMENTO ---
schedule.every().day.at("09:00").do(tarefa)
schedule.every().day.at("18:00").do(tarefa)

print("Bot rodando...")
tarefa()  # roda uma vez imediatamente ao iniciar

while True:
    schedule.run_pending()
    time.sleep(60)