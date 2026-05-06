import csv
import os
import re


class VoteRepository:
    def __init__(self, folder_path="storage/sessions"):
        self.folder_path = folder_path
        self.ensure_folder_exists()

    # Garante que a pasta onde os arquivos CSV das sessões serão salvos exista.
    def ensure_folder_exists(self):
        if not os.path.exists(self.folder_path):
            os.makedirs(self.folder_path)

    # Normaliza o nome da sessão para ser usado como nome de arquivo CSV.
    def format_session_name(self, session_name):
        formatted_name = session_name.strip().lower()

        formatted_name = re.sub(r"\s+", "_", formatted_name)
        formatted_name = re.sub(r"[^a-z0-9_]", "", formatted_name)

        return formatted_name

    # Monta o caminho completo do arquivo CSV da sessão.
    def get_file_path(self, session_name):
        formatted_name = self.format_session_name(session_name)

        return f"{self.folder_path}/{formatted_name}.csv"

    # Cria o arquivo CSV da sessão com os destinos e a contagem inicial de votos.
    def create_session_file(self, session_name, destinations):
        self.ensure_folder_exists()

        file_path = self.get_file_path(session_name)

        if not os.path.exists(file_path):
            with open(file_path, mode="w", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerow(["destination", "votes"])

                for destination in destinations:
                    writer.writerow([destination, 0])

    # Lê o CSV da sessão e retorna um dicionário no formato {destino: votos}.
    def read_results(self, session_name):
        file_path = self.get_file_path(session_name)

        results = {}

        if not os.path.exists(file_path):
            return results

        with open(file_path, mode="r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                destination = row["destination"]
                votes = int(row["votes"])

                results[destination] = votes

        return results

    # Regrava o CSV da sessão com os resultados atualizados.
    def save_results(self, session_name, results):
        file_path = self.get_file_path(session_name)

        with open(file_path, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["destination", "votes"])

            for destination, votes in results.items():
                writer.writerow([destination, votes])

    # Incrementa um voto para o destino informado dentro da sessão.
    def increement_vote(self, session_name, destination):
        results = self.read_results(session_name)

        if destination not in results:
            results[destination] = 0

        results[destination] += 1

        self.save_results(session_name, results)
