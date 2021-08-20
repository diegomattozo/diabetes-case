## Diabetes Case

## Utilização

Após clonar esse repositório, você deve realizar os passos a seguir:
Crie um ambiente virtual no python:
```bash
python3 -m venv .venv
```
Ative seu ambiente virtual:
```bash
source .venv/bin/activate
```
Instale os pacotes necessários:
```bash
> pip install -r requirements.txt
```
Inicie o jupyter lab para ver os resultados nos notebooks
```bash
> jupyter lab --no-browser
```

Os notebooks com a análise explorátoria, resposta das questões, data prep e modelagem estão na pasta notebooks.

## Escoragem em um novo público
Para escorar um público específico é só utilizar o cli disponível:
```bash
python cli.py --input-data='data/raw/diabetes_data_upload.csv' --output-data='data/processed/diabetes_data_scored.csv'
```
Vale ressaltar que é necessário que a base esteja em disco e no formato csv.
