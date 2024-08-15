import os
import requests

# URL do site SISAB
url = "https://sisab.saude.gov.br/"

# Diretório onde o arquivo HTML será salvo
output_dir = "./data"
output_file = "sisab_homepage.html"
output_path = os.path.join(output_dir, output_file)

# Certifique-se de que o diretório existe
os.makedirs(output_dir, exist_ok=True)

try:
    # Faz a solicitação HTTP para o site
    response = requests.get(url)
    response.raise_for_status()  # Verifica se houve algum erro na requisição

    # Escreve o conteúdo HTML no arquivo
    with open(output_path, "w", encoding="utf-8") as file:
        file.write(response.text)

    print(f"HTML da página principal do SISAB salvo em: {output_path}")

except requests.exceptions.RequestException as e:
    print(f"Erro ao coletar dados do site SISAB: {e}")
