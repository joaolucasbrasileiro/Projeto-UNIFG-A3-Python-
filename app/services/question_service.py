from app.data.votes_data import (
    DESTINATIONS_BY_SECONDARY_ANSWER,
    PRIMARY_QUESTIONS,
    SECONDARY_QUESTIONS,
)


class QuestionService:
    # Carrega em memória as perguntas e os destinos definidos no arquivo de dados.
    def __init__(self):
        self.primary_questions = PRIMARY_QUESTIONS
        self.secondary_questions = SECONDARY_QUESTIONS
        self.destinations_by_secondary_answer = DESTINATIONS_BY_SECONDARY_ANSWER

    # Devolve a lista de perguntas iniciais do fluxo.
    def get_primary_questions(self):
        return self.primary_questions

    # Busca a pergunta secundária de acordo com a resposta primária escolhida.
    def get_secondary_question(self, primary_answer):
        if primary_answer not in self.secondary_questions:
            raise ValueError("Resposta primária inválida.")

        return self.secondary_questions[primary_answer]

    # Busca os destinos possíveis de acordo com a resposta secundária escolhida.
    def get_destinations(self, secondary_answer):
        if secondary_answer not in self.destinations_by_secondary_answer:
            raise ValueError("Resposta secundária inválida.")

        return self.destinations_by_secondary_answer[secondary_answer]

    # Junta todos os destinos cadastrados, removendo duplicados.
    def get_all_destinations(self):
        all_destinations = []

        for destinations in self.destinations_by_secondary_answer.values():
            all_destinations.extend(destinations)

        return sorted(set(all_destinations))
