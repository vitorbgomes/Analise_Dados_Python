import requests
import pandas as pd
import numpy as np


def coletar_dados_cripto():
    """
    Coleta dados da API da CoinGecko para as 100 principais criptomoedas.
    Retorna um DataFrame do pandas com os dados ou None em caso de erro.
    """
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        'vs_currency': 'brl',
        'order': 'market_cap_desc',
        'per_page': 100,
        'page': 1,
        'sparkline': 'false'
    }

    print("Coletando dados da API da CoinGecko...")
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Lança um erro para respostas HTTP 4xx/5xx
        dados = response.json()
        print("Dados coletados com sucesso!")
        return pd.DataFrame(dados)
    except requests.exceptions.RequestException as e:
        print(f"Erro ao acessar a API: {e}")
        return None


def tratar_e_preparar_dados(df):
    """
    Realiza a limpeza, tratamento e preparação do DataFrame de criptomoedas.
    Retorna o DataFrame tratado.
    """
    if df is None:
        return None

    print("\nIniciando tratamento e preparação dos dados...")

    # 1. Seleção de Colunas Relevantes
    colunas_relevantes = [
        'id', 'symbol', 'name', 'current_price', 'market_cap',
        'total_volume', 'high_24h', 'low_24h', 'price_change_percentage_24h', 'last_updated'
    ]
    df = df[colunas_relevantes]
    print("- Colunas selecionadas.")

    # 2. Verificação de Dados Nulos
    # Para esta API específica, é raro haver nulos nas colunas principais, mas a verificação é uma boa prática.
    if df.isnull().sum().any():
        print("- Tratando valores nulos (se houver)...")
        # Exemplo: preencher valores nulos com 0, mas outra estratégia poderia ser usada.
        df.fillna(0, inplace=True)
    else:
        print("- Nao foram encontrados valores nulos.")

    # 3. Conversão de Tipos de Dados
    df['last_updated'] = pd.to_datetime(df['last_updated'])
    print("- Tipo de dado da coluna 'last_updated' convertido para datetime.")

    # 4. Padronização de Nomes de Colunas
    df.columns = [col.lower() for col in df.columns]
    print("- Nomes das colunas padronizados para letras minúsculas.")

    # 5. Criação de Nova Feature (Coluna Calculada)
    # Usando numpy para garantir performance e tratamento correto de tipos numéricos.
    df['faixa_preco_24h'] = np.abs(df['high_24h'] - df['low_24h'])
    print("- Nova coluna 'faixa_preco_24h' criada.")

    print("\nTratamento de dados concluído!")
    return df


def salvar_dados(df, nome_arquivo="dados_cripto_tratados.csv"):
    """
    Salva o DataFrame em um arquivo CSV.
    """
    if df is not None:
        try:
            df.to_csv(nome_arquivo, index=False, encoding='utf-8')
            print(f"\nDados salvos com sucesso no arquivo '{nome_arquivo}'")
        except Exception as e:
            print(f"Erro ao salvar o arquivo: {e}")


# --- Fluxo Principal de Execução ---
if __name__ == "__main__":
    df_bruto = coletar_dados_cripto()
    df_tratado = tratar_e_preparar_dados(df_bruto)

    if df_tratado is not None:
        print("\nAmostra dos dados tratados:")
        print(df_tratado.head())

        print("\nInformações do DataFrame final:")
        df_tratado.info()

        salvar_dados(df_tratado)