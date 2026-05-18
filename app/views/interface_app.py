
import customtkinter as ctk
from app.controllers.vote_controller import VotingController


class InterfaceApp(ctk.CTk):
    def __init__(self, controller: VotingController):
        super().__init__()
        self.controller = controller
