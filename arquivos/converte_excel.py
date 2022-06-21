import pandas as pd

datatypes_per_column = {
        "DATA": "datetime64[ns]",
        "PEDIDO": "string",
        "CNPJ": "string",
        "ARQUIVO": "string",
        "EAN": "string",
        "QTDE": "int64"
    }

pedidos = pd.read_csv('pedidos.csv', delimiter=';')
#pedidos['DATA'] =  pd.to_datetime(pedidos['DATA']).dt.normalize()
pedidos = pedidos.dropna()
pedidos = pedidos.astype(datatypes_per_column)
pedidos = pedidos.sort_values(by=['DATA', 'PEDIDO'])
pedidos.to_excel('pedidos.xlsx', index=False, sheet_name = 'Pedidos MaterFormula')