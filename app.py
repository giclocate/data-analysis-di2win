import pandas as pd
import plotly.express as px
import streamlit as st
import os
from sqlalchemy import create_engine
from dotenv import load_dotenv


# Configurando a página
st.set_page_config(page_title="ExtrAIdados Dashboard",
                   page_icon=":bar_chart:",
                   layout="wide"
    
)

def get_db_engine():
    dotenv_path = r'C:/Users/giova/Desktop/Projeto Di2win/.env'
    
    # Carregar o arquivo .env
    load_dotenv(dotenv_path=dotenv_path)

    user = os.getenv('DB_USER')
    password = os.getenv('DB_PASSWORD')
    host = os.getenv('DB_HOST')
    port = os.getenv('DB_PORT')
    database = os.getenv('DB_NAME')

    engine = create_engine(f'postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}')
    return engine

engine = get_db_engine()

df = pd.read_sql_query("SELECT * FROM reports;", engine)

# ---- SIDEBAR ----#
st.sidebar.image("img/logo-completa-branco.png", caption="Plataforma ExtrAIdados")

st.sidebar.header("Por favor, filtre aqui:")
tipo_doc = st.sidebar.multiselect(
    "Selecione o tipo de documento:",
    options=df['type_document'].unique(),
    default=df['type_document'].unique()
)

corretude = st.sidebar.multiselect(
    "Selecione campos corretos(TRUE) ou campos incorretos(FALSE):",
    options=df['edit'].unique(),
    default=df['edit'].unique()
)

total_null = st.sidebar.multiselect(
    "Selecione campos nulos(True) ou não-nulos(False):",
    options=df['is_null'].unique(),
    default=df['is_null'].unique()
)

df_selection = df.query(
    f"type_document in {tipo_doc} and edit in {corretude} and is_null in {total_null}"
)


# ---- MAINPAGE ----#
st.title(":bar_chart: Di2win Dashboard")
st.markdown("Este é um dashboard interativo para análise de documentos do banco ExtrAIdados.")



# TOP KPI'S
total_extractions = df.shape[0]

# Calcule a média da porcentagem de campos corretos por documento
average_correct = round((df['edit'] == False).mean() * 100, 1)  
average_incorrect = 100 - average_correct

left_column, middle_column, right_column = st.columns(3)
with left_column:
    st.subheader("Total de Documentos Extraídos:")
    st.title(f"{total_extractions:,}")
with middle_column:
    st.subheader("Porcentagem de Campos Corretos:")
    st.subheader(f"{average_correct}%")
with right_column:
    st.subheader("Total de Documentos Incorretos:")
    st.title(f"{round(average_incorrect, 2)}%")

st.markdown("---")

# Filtrar apenas os documentos corretos (edit = False)
df_correct_docs = df_selection[df_selection['edit'] == False]

# Agrupar por tipo de documento e contar o número de documentos corretos
sales_by_document_type = (
    df_correct_docs.groupby(by=["type_document"])
    .size()
    .reset_index(name="Total")
    .sort_values(by="Total", ascending=False)
)

# Criar o gráfico de barras horizontal para os documentos corretos por tipo de documento
fig_document_sales = px.bar(
    sales_by_document_type,
    x="Total",
    y="type_document",
    orientation="h",
    title="<b>Documentos Corretos por Tipo de Documento</b>",
    color_discrete_sequence=["#f94dac"] * len(sales_by_document_type),
    template="plotly_white"
)

# Exibir o gráfico no Streamlit
st.plotly_chart(fig_document_sales)


# Contagem de campos corretos e incorretos
field_counts = df_selection['edit'].value_counts().reset_index()
field_counts.columns = ['edit', 'count']
field_counts['label'] = field_counts['edit'].apply(lambda x: "Corretos" if not x else "Incorretos")

# Criar o gráfico de rosca
fig_donut = px.pie(
    field_counts,
    values='count',
    names='label',
    title="<b>Distribuição de Campos Corretos e Incorretos</b>",
    hole=0.4,
    color_discrete_sequence=["#f94dac", "#dbdbdb"]
)

# Exibir o gráfico no Streamlit
st.plotly_chart(fig_donut)

# Agrupar dados por tipo de documento e se o campo é correto ou incorreto
document_edit_counts = df_selection.groupby(['type_document', 'edit']).size().reset_index(name='count')
document_edit_counts['label'] = document_edit_counts['edit'].apply(lambda x: "Corretos" if not x else "Incorretos")

# Iterar sobre cada tipo de documento e gerar um gráfico de pizza
for document_type in document_edit_counts['type_document'].unique():
    doc_data = document_edit_counts[document_edit_counts['type_document'] == document_type]

    # Criar o gráfico de pizza
    fig_pie = px.pie(
        doc_data,
        values='count',
        names='label',
        title=f"<b>Distribuição de Campos Corretos e Incorretos - {document_type}</b>",
        color_discrete_sequence=["#f94dac", "#dbdbdb"]
    )
    fig_pie.update_traces(textinfo="percent+label")
    
    # Exibir o gráfico no Streamlit
    st.plotly_chart(fig_pie)
