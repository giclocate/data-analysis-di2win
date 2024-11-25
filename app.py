import pandas as pd
import plotly.express as px
import streamlit as st
import os
from sqlalchemy import create_engine
from dotenv import load_dotenv
from io import BytesIO
from openpyxl.styles import PatternFill, Font
from openpyxl import Workbook
from openpyxl.drawing.image import Image

# Configurando a página
st.set_page_config(page_title="ExtrAIdados Dashboard",
                   page_icon=":bar_chart:",
                   layout="wide")

def get_db_engine():
    # Carregar o arquivo .env no mesmo diretório
    load_dotenv()

    user = os.getenv('DB_USER')
    password = os.getenv('DB_PASSWORD')
    host = os.getenv('DB_HOST')
    port = os.getenv('DB_PORT', 5432)
    database = os.getenv('DB_NAME')

    # Criar a engine do SQLAlchemy
    engine = create_engine(f'postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}')
    return engine

# Teste de conexão com o banco de dados
engine = get_db_engine()

df = pd.read_sql_query("SELECT * FROM reports;", engine)

# ---- SIDEBAR ----#
st.sidebar.image("logo-completa-branco.png", caption="Plataforma ExtrAIdados")

st.sidebar.header("Por favor, filtre aqui:")
tipo_doc = st.sidebar.multiselect(
    "Selecione o tipo de documento:",
    options=df['type_document'].unique(),
    default=df['type_document'].unique()
)

corretude = st.sidebar.multiselect(
    "Selecione campos corretos ou campos incorretos:",
    options=df['edit'].unique(),
    default=df['edit'].unique()
)

total_null = st.sidebar.multiselect(
    "Selecione campos nulos ou não-nulos:",
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
average_correct = round((df['edit'] == False).mean() * 100, 1)
average_incorrect = 100 - average_correct

# Estilo CSS
st.markdown(
    """
    <style>
    .kpi-box {
        background-color: #2B2C36; /* Cor do fundo */
        padding: 15px; /* Espaçamento interno */
        border-radius: 8px; /* Bordas arredondadas */
        text-align: center; /* Centralizar conteúdo */
        margin: 5px; /* Margem */
        box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.1); /* Sombra */
    }
    .kpi-title {
        font-size: 18px; /* Tamanho do texto menor */
        margin-bottom: 5px;
        color: #fff; /* Cor do texto */
        font-weight: bold;
    }
    .kpi-value {
        font-size: 28px; /* Tamanho do valor */
        font-weight: bold;
        color: #f94dac; /* Cor do valor */
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Layout das Colunas
left_column, middle_column, right_column = st.columns(3)

with left_column:
    st.markdown(
        f"""
        <div class="kpi-box">
            <div class="kpi-title">📌<span>Total de Documentos Extraídos:</span></div>
            <div class="kpi-value">{total_extractions:,}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with middle_column:
    st.markdown(
        f"""
        <div class="kpi-box">
            <div class="kpi-title">📌<span>Campos Corretos:</span></div>
            <div class="kpi-value">{average_correct}%</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with right_column:
    st.markdown(
        f"""
        <div class="kpi-box">
            <div class="kpi-title">📌<span>Campos Incorretos:</span></div>
            <div class="kpi-value">{round(average_incorrect, 2)}%</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown("---")


# ---- Filtrar apenas os documentos corretos (edit = False) ----
df_correct_docs = df_selection[df_selection['edit'] == False]

# Verificação para documentos corretos
if df_correct_docs.empty:
    st.warning("⚠️ Nenhum documento com campos corretos encontrado com os filtros aplicados.")
else:
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

    # Exibir o gráfico na coluna esquerda
    left_column, right_column = st.columns(2)
    left_column.plotly_chart(fig_document_sales, use_container_width=True)

# ---- Contagem de campos corretos e incorretos (Gráfico de Rosca) ----
if df_selection.empty:
    st.warning("⚠️ Nenhum dado encontrado para o gráfico de distribuição com os filtros aplicados.")
else:
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

    # Exibir o gráfico na coluna direita
    right_column.plotly_chart(fig_donut, use_container_width=True)

# ---- Seletor para análise de um documento específico ----
documento_especifico = st.selectbox(
    "Qual documento você gostaria de analisar?",
    options=df_selection['type_document'].unique()
)

# Agrupar dados por tipo de documento e se o campo é correto ou incorreto
document_edit_counts = df_selection.groupby(['type_document', 'edit']).size().reset_index(name='count')
document_edit_counts['label'] = document_edit_counts['edit'].apply(lambda x: "Corretos" if not x else "Incorretos")

# Filtrar os dados para o documento específico selecionado
doc_specific_data = document_edit_counts[document_edit_counts['type_document'] == documento_especifico]

if doc_specific_data.empty:
    st.warning(f"⚠️ Nenhum dado encontrado para o documento '{documento_especifico}' com os filtros aplicados.")
else:
    # Criar o gráfico de pizza para o documento específico
    fig_pie = px.pie(
        doc_specific_data,
        values='count',
        names='label',
        title=f"<b>Distribuição de Campos Corretos e Incorretos - {documento_especifico}</b>",
        color_discrete_sequence=["#f94dac", "#dbdbdb"]
    )
    fig_pie.update_traces(textinfo="percent+label")

    # Exibir o gráfico no Streamlit
    st.plotly_chart(fig_pie)


def generate_styled_excel(df):
    # Se precisar remover uma coluna, faça isso aqui
    df = df.drop(columns=['id'])  # ajuste o nome da coluna conforme necessário

    # Renomear colunas (ajuste a lista conforme o número de colunas que você realmente tem)
    df.columns = [
        'Tipo do documento',
        'Nome do documento',
        'Nome do campo',
        'Valor inicial',
        'Valor final',
        'Campo alterado',
        'Campo vazio'
    ]

    # Adicionar coluna 'Resultado'
    df['Resultado'] = df['Campo alterado'].apply(lambda x: 'Correto' if not x else 'Incorreto')

    # Adicionar coluna 'Porcentagem' com a porcentagem de campos corretos/incorretos por documento
    correct_percentage = (
        df.groupby('Tipo do documento')['Resultado']
        .apply(lambda x: round((x == 'Correto').mean() * 100, 2))
        .rename('Porcentagem')
    )
    df = df.merge(correct_percentage, on='Tipo do documento', how='left')

    # Estilização das células
    def styling(row):
        result_color = 'background-color: #BDF5BD' if row['Resultado'] == 'Correto' else 'background-color: #FF7979'
        return [result_color if col == 'Resultado' else '' for col in df.columns]

    # Aplicar estilização apenas na coluna 'Resultado'
    styled_df = df.style.apply(styling, axis=1)

    # Gerar Excel
    output = BytesIO()
    with pd.ExcelWriter(output, engine="openpyxl") as writer:
        styled_df.to_excel(writer, sheet_name="Dados", index=False, startrow=1)

        workbook = writer.book
        worksheet = writer.sheets['Dados']

        # Adicionar a célula de título estilizada
        header_cell = worksheet["A1"]
        header_cell.value = "Tabela de documentos"
        header_cell.font = Font(color="FFFFFF", bold=True, size=14)  # Fonte branca, negrito e tamanho maior
        header_cell.fill = PatternFill(start_color="FF69B4", end_color="FF69B4", fill_type="solid")  # Fundo rosa

        # Ajustar a largura da coluna se necessário
        worksheet.column_dimensions['A'].width = 20

    output.seek(0)
    return output

if st.button("Gerar Excel"):
    excel_file = generate_styled_excel(df)
    st.download_button(
        label="Download Excel",
        data=excel_file,
        file_name="relatorio.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )

# ---- HIDE STREAMLIT STYLE ----
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)