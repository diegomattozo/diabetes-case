## Diabetes Case

## Utilização

Após clonar esse repositório, você deve realizar os passos a seguir:

Crie um ambiente virtual no python:
> python3 -m venv .venv

Ative seu ambiente virtual:
> source .venv/bin/activate

Instale dos pacotes necessários:
> pip install -r requirements.txt

Inicie o jupyter lab para ver os resultados nos notebooks
> jupyter lab --no-browser

Os notebooks com a análise explorátoria, resposta das questões, data prep e modelagem estão na pasta notebooks.

## Escoragem em um novo público
Para escorar o modelo em um novo publico desejado ou no público de treino basta digita:

> python cli.py --input-data='data/raw/diabetes_data_upload.csv' --output-data='data/processed/diabetes_data_scored.csv'
