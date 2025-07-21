import requests
import pandas as pd
import urllib3
import os
import boto3

# Desativa alerta de SSL
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# URL inicial
url = "https://swapi.dev/api/species/"
especies = []

# Paginação
while url:
    try:
        response = requests.get(url, verify=False)
        response.raise_for_status()
        data = response.json()
        especies.extend(data['results'])
        url = data.get('next')

    except requests.exceptions.RequestException as e:
        print(f"Erro na requisição: {e}")
        break

# Nome do arquivo temporário
filename = "especies.csv"

# Salvar CSV
df = pd.DataFrame(especies)
df.to_csv(filename, index=False)
print(f"✅ Arquivo salvo como {filename}")

s3 = boto3.client('s3')
bucket = "sw-datalake-rodrigo"
key = "planilhas/especies.csv"
s3.upload_file(filename, bucket, key)
print(f"✅ Arquivo enviado para s3://{bucket}/{key}")

# Apagar o arquivo local
if os.path.exists(filename):
    os.remove(filename)
    print(f"🗑️ Arquivo {filename} apagado com sucesso.")
else:
    print("⚠️ Arquivo não encontrado para apagar.")
