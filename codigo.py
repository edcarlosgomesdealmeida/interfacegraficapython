import requests



def pegar_cotacoes(codigo_mmoeda):
    try:
        requisicao = requests.get(f"https://economia.awesomeapi.com.br/last/{codigo_mmoeda}-BRL")
        requisicao_dic = requisicao.json()
        cotacao = requisicao_dic[f'{codigo_mmoeda}BRL']['bid']
        return cotacao
    except:
        print("Código de Moeda Inválido")
        return None