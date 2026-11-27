import pandas as pd
idades_lista = [25,30,22,28]
idades_series = pd.Series([25,30,22,28])
# print(f"Lista:\n{idades_lista}")
# print(f"Series\n{idades_series}")



notas = pd.Series([9.5,8.0,7.5,9.0], index=['João','Maria','Pedro','Ana'])
# print(notas['Maria'])                  # Acessando a nota da Maria pelo rótulo
# print(notas.iloc[2])                   # Acessando a nota do Pedro pela posição                
# print(notas.mean())                    # Calculando a média das notas
# print(notas[notas > 8])                # Filtrando as notas maiores que 8.0
# print(notas.describe())                # Estatísticas descritivas das notas


# Operações Aritméticas
notas_ajustadas = notas * 1.10
# print(notas_ajustadas)

# Comparando duas Series
notas_exame_final = pd.Series([10, 7.5, 8.0, 9.5], index=['João','Maria','Pedro','Ana'])
diferença = notas_exame_final - notas_ajustadas
# print(diferença)

# DataFrames: Lendo planilhas do Excel
df = pd.read_excel('base_invest.xlsx')     #Lê a planilha do Excel e cria um DataFrame
print(df.head())  # Exibindo as 05 primeiras linhas do DataFrame
print(df.info())  # Exibindo informações sobre o DataFrame
print(df.duplicated())  # Verificando se há linhas duplicadas no DataFrame
