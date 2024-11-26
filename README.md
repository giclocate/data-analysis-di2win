# Data Analysis Di2win🤩🌟🩷

## 🌏 Visão geral do projeto
Este projeto é realizado em parceria com a empresa Di2win🩷, onde efetuamos o tratamento e a análise de dados. Com base nos dados fornecidos pela empresa, elaboramos um relatório detalhado sobre as taxas de documentos processados.

## 📍Stack utilizada

<div> 
  <img align="inline_block" alt="python" src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img align="inline_block" alt="pandas" src="https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white"/>
  <img align="inline_block" alt="PostegresSQL" src="https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white"/>
  <img align="inline_block" alt="jupyter Notebook" src="https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white"/>
  <img align="inline_block" alt="PowerBi" src="https://img.shields.io/badge/power_bi-F2C811?style=for-the-badge&logo=powerbi&logoColor=black"/> 
  <img align="inline_block" alt="Docker" src="https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white"/> 
  <img align="inline_block" alt="Docker" src="https://img.shields.io/badge/Streamlit-%23FE4B4B.svg?style=for-the-badge&logo=streamlit&logoColor=white"/> 
</div>

## 📋Pré-requisitos

Antes de começar, certifique-se de ter o seguinte instalado em seu ambiente:

- Python 3.8+
- PostgreSQL 12+
- Jupyter Notebook
- Pandas
- SQLAlchemy 
- psycopg2
- Streamlit
  
## 🧾 Funcionalidades 

- [x] Gerar relatório de taxa de documentos processados
- [x] Dados de formatação exigida na documentação do projeto da residência
- [X] Saída realizada pelo Excel 
- [X] Histograma dos dados corretos e incorretos por tipo de documentos
- [X] Formatação em cores
- [X] Gráficos de pizza de porcentagem de cada documentos
- [X] Inserção das tabelas no documento Excel
 
## 💡Diferenciais
- [X] gerar gráficos em PowerBi
- [X] Criar o Streamlit
- [X] Isolamento e escalabilidade com Docker
- [ ] Deploy integrado no Back4App **🚧Em Construção**

## 📂 Estrutura do Projeto

```
├── /data                
├── /src                  
│   ├── app.py            
│   ├── analysis.py      
│   ├── database.py       
├── /assets              
├── Dockerfile         
├── requirements.txt      
├── README.md            
└── ...
````

## 🏛️ Arquitetura do projeto
```mermaid
graph TD
    Cliente[Cliente] --> ExtraiDados[Extrai Dados]
    ExtraiDados --> Login[Login]
    Login --> Streamlit[Streamlit]
    Streamlit --> TratamentoDados[Tratamento dos Dados]
    TratamentoDados --> Excel[Extração do Excel]
    TratamentoDados --> Graficos[Geração de Gráficos]
    Graficos --> PowerBI[PowerBI]

    subgraph Infraestrutura
        Streamlit -->|Conexão| PostgreSQL[(PostgreSQL)]
        PostgreSQL --> Jupyter[Jupyter Notebook]
        Streamlit --> Docker(Docker)
       Streamlit --> Kubernetes[Kubernetes]
    end

````

## 🔮 Futuras Melhorias

| **Área**             | **Descrição**                                                                 |
|----------------------|------------------------------------------------------------------------------|
| **🔗 Integrações**   | Acesso a APIs externas para coleta de dados em tempo real.                   |
| **🚀 Escalabilidade**| Suporte a outras plataformas de nuvem como AWS e Azure.                     |
| **📊 Visualização**  | Gráficos interativos no Streamlit com filtros dinâmicos.                     |
| **📊 Relatórios**    | Relatórios personalizados com seleção de dados e formatação.                 |
| **🔒 Segurança**     | Autenticação via OAuth2/SSO e logs de auditoria para rastreabilidade.         |
| **📂 Estrutura de Dados** | Otimização de queries e índices no PostgreSQL; suporte a MySQL e MongoDB. |


## 👥 Grupo

- [@Marcellyz](https://github.com/Marcellyz) - Marcelly Eduarda Santos da Silva
- [@giclocate](https://github.com/giclocate) - Giovanna Clócate Cavalcante de Almeida
- [@katiarochaalmeida](https://github.com/katiarochaalmeida) - Katia Rocha de Almeida
- [@HelengAraujo](https://github.com/HelengAraujo) - Helen Gabriely Lima de Araujo
- [@rubyzim](https://github.com/rubyzim) - Higor Gomes Ramos da Silva

## 🙏 Agradecimentos 
Agradecemos profundamente à empresa Di2Win 🏢🩷 pela parceria e apoio, aos professores 🎓📚 pelo conhecimento compartilhado, à equipe 👥🤝 pelo trabalho dedicado, e a todos que, de alguma forma, contribuíram para a realização deste projeto. Cada um de vocês foi fundamental para o sucesso desta iniciativa 💖✨.
