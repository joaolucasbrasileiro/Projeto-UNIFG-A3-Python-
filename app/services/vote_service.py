from app.repositories.vote_repository import VoteRepository
from app.services.session_service import SessionService


class VoteService:
    # Recebe as dependências necessárias para validar a sessão e persistir votos.
    def __init__(self, vote_repository: VoteRepository, session_service: SessionService):
        self.vote_repository = vote_repository
        self.session_service = session_service

    # Registra um voto em um destino válido dentro da sessão ativa.
    def register_vote(self, destination: str):
        session = self.session_service.get_active_session()

        if not session.is_active:
            raise RuntimeError("A sessão já foi encerrada!")

        results = self.vote_repository.read_session_results(session.name)

        if destination not in results:
            raise ValueError("Destino inválido para esta sessão.")

        self.vote_repository.increment_destination_vote(session.name, destination)

    # Lê os resultados atuais da sessão ativa.
    def get_current_results(self):
        session = self.session_service.get_active_session()

        return self.vote_repository.read_session_results(session.name)
