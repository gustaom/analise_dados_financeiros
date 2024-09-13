import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar os dados
df = pd.read_csv('../dados/dados_financeiros.csv')
df['Data'] = pd.to_datetime(df['Data'])

# Configurações do gráfico
sns.set(style='whitegrid')

# Gráfico de Entradas e Saídas ao Longo do Tempo
plt.figure(figsize=(12, 6))
sns.lineplot(data=df, x='Data', y='Valor', hue='Tipo', marker='o')
plt.title('Entradas e Saídas ao Longo do Tempo')
plt.xlabel('Data')
plt.ylabel('Valor (R$)')
plt.legend(title='Tipo')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('../visualizacoes/entradas_saidas_tempo.png')
plt.show()

# Gráfico de Total de Entradas e Saídas por Mês
df['Mês'] = df['Data'].dt.to_period('M')
df_mensal = df.groupby(['Mês', 'Tipo'])['Valor'].sum().unstack().fillna(0)

plt.figure(figsize=(12, 6))
df_mensal.plot(kind='bar', stacked=True)
plt.title('Total de Entradas e Saídas por Mês')
plt.xlabel('Mês')
plt.ylabel('Valor (R$)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('../visualizacoes/entradas_saidas_mes.png')
plt.show()
