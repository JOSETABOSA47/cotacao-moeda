import requests
from datetime import datetime

def send_message(token, chat_id, message):
    try:
        data = {"chat_id": chat_id, "text": message}
        url = "https://api.telegram.org/bot{}/sendMessage".format(token)
        requests.post(url, data)
    except Exception as e:
        print("Erro no sendMessage:", e)

requisicao = requests.get(
    "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

requisicao_dic = requisicao.json()
cotacao_dolar = float(requisicao_dic["USDBRL"]["bid"])
cotacao_euro = float(requisicao_dic["EURBRL"]["bid"])
cotacao_btc = float(requisicao_dic["BTCBRL"]["bid"])

msg = f"Cotação Atualizada. {datetime.now()}\nDólar: R${cotacao_dolar:,.2f}\nEuro: R${cotacao_euro:,.2f}\nBTC: R${cotacao_btc:,.2f}\n\nInvestir um valor de R$298,13 e USDT56,29 na data 07/10/2022"

automacao = '5495104211:AAHJIrse-oxrpomZrVnJvySGaqfCqqx_0Ls'

send_message(automacao, '830463079', msg)
