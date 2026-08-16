# Coffee Shop Sales Analysis

Projeto de criação de um pipeline de dados e visualização de dados a partir do dataset Coffee Shop Sales da Maven Analytics.

## 📜 Sumário
1. [📌 Sobre o Projeto](#-sobre-o-projeto)
2. [⚙️ Tecnologias Utilizadas](#️-tecnologias-utilizadas)
3. [🚀 Como Executar](#-como-executar)
4. [📊 Estrutura do Projeto](#-estrutura-do-projeto)
5. [🗒️ Licença](#️-licença)
6. [📞 Contato](#-contato)


## 📌 Sobre o Projeto
Este repositório contém um pipeline completo de dados transacionais de uma rede de cafeterias fictícia operando em três localizações em Nova York. O objetivo é extrair insights de negócio, identificar padrões de vendas e fornecer recomendações estratégicas para otimização operacional.

![Imgur](https://i.imgur.com/9cldPlk.png)

## ⚙️ Tecnologias Utilizadas
- Python 3.12
- dlt (data load tool)
- dbt (data build tool)
- DuckDB
- Power BI

## 🚀 Como Executar
Acesse o dashboard no [Power BI Service](https://app.powerbi.com/view?r=eyJrIjoiYmY4ODBhOWYtOGNmMC00NzQ5LTk4OGMtNjM2MTBlZmEwYjM4IiwidCI6ImJmOWUzNDgwLTkyM2UtNDNmMS04OTE1LTlmMmY3YjY2NTc0MSJ9). 

![dash](https://i.imgur.com/qBBI1sG.png)

#### Pré-requisitos
- Python 3.12+
- uv

#### Execução 
1️⃣ **Clone o repositório**
```bash
git clone https://github.com/datalopes1/coffee.git
cd coffee
```

2️⃣ **Instale as dependências e crie um ambiente virtual**
```bash
pip install uv
uv sync
```
3️⃣ **Ative o ambiente virtual**
```bash
source .venv/bin/activate  # Mac e Linux
.venv\Scripts\activate  # Windows
```

4️⃣ **Execute o pipeline**
```bash
python -m src.pipeline
```

## 📊 Estrutura do Projeto
```plaintext
coffee/
├── data/
│   ├── raw/                 # Dados brutos em Excel
│   │   └── sales.xlsx
│   └── database/
│       └── db.duckdb        # Banco de dados DuckDB
├── dwh/                     # Projeto dbt
│   ├── models/
│   │   ├── stg/            # Staging (views)
│   │   │   └── stg_excel__sales.sql
│   │   ├── int/            # Intermediários (ephemeral)
│   │   │   └── int_sales_enriched.sql
│   │   └── marts/          # Marts (tables)
│   │       └── sales/
│   │           ├── fct_sales.sql
│   │           ├── obt_sales.sql
│   │           ├── dim_product.sql
│   │           └── dim_store.sql
│   ├── tests/
│   ├── seeds/
│   ├── macros/
│   ├── analyses/
│   ├── snapshots/
│   ├── dbt_project.yml
│   └── README.md
├── dashboard/
│   ├── sales_dashboard.pbip
│   ├── sales_dashboard.Report/
│   └── sales_dashboard.SemanticModel/
├── src/
│   └── pipeline.py          # Pipeline de ingestão e transformação
├── pyproject.toml
├── uv.lock
└── .python-version

```

## 🗒️ Licença
Este projeto está licenciado sob a MIT License - veja o arquivo [LICENSE](LICENSE.md) para mais detalhes.

## 📞 Contato
- LinkedIn: https://www.linkedin.com/in/datalopes1
- Portfolio: https://datalopes1.github.io/
- E-mail: datalopes1@proton.me
