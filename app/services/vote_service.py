from app.repositories.vote_repository import VoteRepository
from app.services.session_service import SessionService


class VoteService:
    def __init__(self, vote_repository: VoteRepository, session_service: SessionService):
        self.vote_repository = vote_repository
        self.session_service = session_service

    def register_vote(self, destination: str):
        session = self.session_service.get_current_session()

        if not session.is_active:
            raise RuntimeError("A sessão já foi encerrada!")

        self.vote_repository.increment_vote(session.name, destination)

    def get_current_results(self):
        session = self.session_service.get_current_session()

        return self.vote_repository.read_results(session.name)
