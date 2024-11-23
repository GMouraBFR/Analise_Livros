import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Análise de Vendas de Carros Usados")

# Carregar dados (substitua pelo caminho correto do seu conjunto de dados)
df = pd.read_csv('vehicles.csv')

# Exibir as primeiras linhas do DataFrame
st.write(df.head())

# Botão para Criar um Histograma
hist_button = st.button('Criar Histograma')

if hist_button:
    st.write('Criando um histograma para a coluna price')
    fig = px.histogram(df, x='price', nbins=50, title='Distribuição de Preços')
    st.plotly_chart(fig, use_container_width=True)

# Botão para Criar um Gráfico de Dispersão
scatter_button = st.button('Criar Gráfico de Dispersão')

if scatter_button:
    st.write('Criando um gráfico de dispersão para Preço vs. Quilometragem')
    fig = px.scatter(df, x='price', y='odometer',
                     title='Preço vs. Quilometragem')
    st.plotly_chart(fig, use_container_width=True)

# Gráfico de Barras: Contagem por Tipo de Carro com cores contrastantes
fig = px.bar(df, x='type', title='Contagem por Tipo de Carro',
             color='type',
             color_discrete_sequence=px.colors.qualitative.Bold)  # Usando cores contrastantes
st.plotly_chart(fig, use_container_width=True)

# Caixa de Seleção para Criar um Histograma
build_histogram = st.checkbox('Criar um histograma')

if build_histogram:
    st.write('Criando um histograma para a coluna odometer')
    fig = px.histogram(df, x='odometer')
    st.plotly_chart(fig, use_container_width=True)
