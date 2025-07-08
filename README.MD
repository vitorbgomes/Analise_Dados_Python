# Projeto 1: Análise de Dados de Criptomoedas com Python

## 🎯 Objetivo

Este projeto demonstra um fluxo completo de engenharia de dados, desde a coleta de dados em tempo real via API até o tratamento e a preparação para análise. O objetivo é criar um dataset limpo e estruturado com informações sobre as 100 principais criptomoedas do mercado, utilizando Python e bibliotecas essenciais do ecossistema de dados.

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python 3.x
* **Bibliotecas:**
    * `requests`: Para realizar requisições HTTP e consumir a API da CoinGecko.
    * `pandas`: Para estruturação, manipulação e limpeza dos dados em DataFrames.
    * `numpy`: Para operações numéricas e criação de colunas calculadas.
* **Fonte de Dados:** API pública da [CoinGecko](https://www.coingecko.com/pt/api).

## 📊 O Processo

O script `analise_cripto.py` executa as seguintes etapas:

1.  **Coleta de Dados:** Conecta-se ao endpoint `coins/markets` da API da CoinGecko para buscar dados atualizados das 100 maiores criptomoedas por capitalização de mercado, com valores em Real (BRL).
2.  **Estruturação:** Converte a resposta JSON da API em um DataFrame do pandas para facilitar a manipulação.
3.  **Limpeza e Tratamento (Cleaning):**
    * **Seleção de Colunas:** Filtra apenas as colunas relevantes para a análise.
    * **Verificação de Nulos:** Checa a existência de dados faltantes.
    * **Conversão de Tipos:** Ajusta o tipo de dado da coluna de data (`last_updated`) para o formato `datetime`.
    * **Padronização de Nomes:** Renomeia as colunas para um formato consistente (letras minúsculas).
4.  **Transformação e Preparação (Wrangling):**
    * **Criação de Features:** Adiciona uma nova coluna (`faixa_preco_24h`) que calcula a diferença entre o preço máximo e mínimo das últimas 24 horas.
5.  **Armazenamento:** Salva o DataFrame final e limpo em um arquivo `dados_cripto_tratados.csv`, pronto para ser consumido por ferramentas de análise, BI ou modelos de machine learning.

## 🚀 Como Executar o Projeto

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/seu-usuario/projeto_python_cripto.git](https://github.com/seu-usuario/projeto_python_cripto.git)
    cd projeto_python_cripto
    ```

2.  **Crie e ative um ambiente virtual (recomendado):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows: venv\Scripts\activate
    ```

3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Execute o script:**
    ```bash
    python analise_cripto.py
    ```

Ao final da execução, um arquivo chamado `dados_cripto_tratados.csv` será criado nesta pasta.