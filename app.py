import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Análise de Vendas de Carros Usados")

# Carregar dados
df = pd.read_csv('vehicles.csv')

# Exibir as primeiras linhas do DataFrame
st.write(df.head())

# Caixa de Seleção para Criar Histograma
hist_checkbox = st.checkbox('Criar Histograma')

if hist_checkbox:
    st.write('Criando um histograma para a coluna price')
    fig_hist = px.histogram(df, x='price', nbins=50,
                            title='Distribuição de Preços')
    st.plotly_chart(fig_hist, use_container_width=True)

    # Caixa de Seleção para Criar Gráfico de Dispersão
    scatter_checkbox = st.checkbox('Criar Gráfico de Dispersão', value=True)

    if scatter_checkbox:
        st.write('Criando um gráfico de dispersão para Preço vs. Quilometragem')
        fig_scatter = px.scatter(
            df, x='price', y='odometer', title='Preço vs. Quilometragem')
        st.plotly_chart(fig_scatter, use_container_width=True)

        # Caixa de Seleção para Criar Gráfico de Barras
        bar_checkbox = st.checkbox('Criar Gráfico de Barras', value=True)

        if bar_checkbox:
            st.write('Criando um gráfico de barras para Contagem por Tipo de Carro')
            fig_bar = px.bar(df, x='type', title='Contagem por Tipo de Carro',
                             color='type',
                             color_discrete_sequence=px.colors.qualitative.Bold)  # Usando cores contrastantes
            st.plotly_chart(fig_bar, use_container_width=True)
