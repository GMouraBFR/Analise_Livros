import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Análise de Vendas de Carros")

# Carregar dados (substitua pelo seu próprio conjunto de dados)
df = pd.read_csv('caminho/para/seu/dataset.csv')

st.write(df.head())

# Exibir gráfico
fig = px.histogram(df, x='preco', nbins=50, title='Distribuição de Preços')
st.plotly_chart(fig)
