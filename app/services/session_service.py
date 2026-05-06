

from app.repositories.vote_repository import VoteRepository
from app.models.session import Session


class SessionService:
    def __init__(self, vote_repository: VoteRepository):
        self.repository = vote_repository
        self.current_session = None

    #cria uma nova sessão de votação e chama o repository
    def start_new_session(self, session_name, destinations):
        if not session_name or not session_name.strip():
            raise ValueError("Nome da sessão inválido!")

        self.current_session = Session(session_name)
        self.repository.create_session_file(session_name, destinations)

        return self.current_session

    #Verifica se há sessão ativa, se n houver, lança exception, se houver, devolve a sessão
    def get_current_session(self):
        if self.current_session is None:
            raise RuntimeError("Nenhuma sessão foi iniciada")

        return self.current_session

    def has_active_session(self):
        return (self.current_session is not None
                and self.current_session.is_active)

    #Finaliza a sessão setando ela como is_active False
    def finish_current_session(self):
        session = self.get_current_session
        session.is_active = False

        return session


