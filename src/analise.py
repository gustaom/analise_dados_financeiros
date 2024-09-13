import pandas as pd

# Carregar os dados
df = pd.read_csv('../dados/dados_financeiros.csv')

# Converter a coluna 'Data' para o formato datetime
df['Data'] = pd.to_datetime(df['Data'])

# Salvar o dataframe processado
df.to_csv('../dados/dados_processados.csv', index=False)

print("Arquivo dados_processados.csv foi criado com sucesso.")
# Verificar se há valores nulos
print("Valores nulos por coluna:\n", df.isnull().sum())

# Separar Entradas e Saídas
df_entrada = df[df['Tipo'] == 'Entrada']
df_saida = df[df['Tipo'] == 'Saída']

# Exibir resumo das Entradas e Saídas
print("\nResumo das Entradas:")
print(df_entrada[['Data', 'Descrição', 'Valor']])

print("\nResumo das Saídas:")
print(df_saida[['Data', 'Descrição', 'Valor']])

# Total de entradas e saídas
total_entrada = df_entrada['Valor'].sum()
total_saida = df_saida['Valor'].sum()

print(f"\nTotal de Entradas: R$ {total_entrada}")
print(f"Total de Saídas: R$ {total_saida}")
print(f"Saldo Final: R$ {total_entrada + total_saida}")

# Salvar o dataframe processado
df.to_csv('../dados/dados_processados.csv', index=False)
