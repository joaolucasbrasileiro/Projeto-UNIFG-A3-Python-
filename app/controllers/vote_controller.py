from app.services.session_service import SessionService
from app.services.vote_service import VoteService


class VoteController:
    def __init__(self, session_service: SessionService, vote_service: VoteService):
        self.session_service = session_service
        self.vote_service = vote_service

    def start_new_session(self, session_name: str, destinations: list[str]):
        return self.session_service.start_new_session(session_name, destinations)

    def finish_session(self):
        return self.session_service.finish_current_session()

    def register_vote(self, destination: str):
        self.vote_service.register_vote(destination)

    def get_current_results(self):
        return self.vote_service.get_current_results()

    def has_active_session(self):
        return self.session_service.has_active_session()
