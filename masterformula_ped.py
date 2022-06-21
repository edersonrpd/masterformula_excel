import os

diretorio = os.getcwd()
arquivos = list()
saida = "pedidos_TESTE.csv"
excel = 'pedidos.xlsx'

for arquivo in diretorio:
    if arquivo.endswith('.ped'):
        arquivos.append(arquivo)


#pedido = ['904607821', '904608448']


def master_formula(file: str) -> str:
    produtos = list()
    produtos_qtde = list()
    linhas = len(produtos)

    with open(file, mode='r', encoding='utf-8') as arquivo:
        linha = arquivo.readline()
        while linha:

            if linha.startswith('01'):
                identificador = linha[:2]
                layout = linha[2:6]
                cnpj = linha[8:22]
                cod_cli = linha[23:31]
                pedido = linha[31:40]
                data = linha[40:48]
                dia = data[6:8]
                mes = data[4:6]
                ano = data[:4]

            if linha.startswith('03'):
                produtos.append(linha[3:16])
                produtos_qtde.append(int(linha[16:23]))

            if linha.startswith('09'):
                qtde_itens = int(linha[3:6])
                qtde_total_unid = int(linha[7:15])

            linha = arquivo.readline()

        for produto, qtde in zip(produtos, produtos_qtde):
                print(f'{dia}/{mes}/{ano};{pedido};{cnpj};{file};{produto};{qtde}')
        # for i in range(linhas) :
        #     #for i in pedido:
        #      #   if pedido == i:
        #     print(f'{dia}/{mes}/{ano};{pedido};{file};{produtos[i]};{produtos_qtde[i]}' )
        


print(f'DATA;PEDIDO;CNPJ;ARQUIVO;EAN;QTDE')
for arquivo in arquivos:
    master_formula(arquivo)