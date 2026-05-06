from datetime import datetime


class Vote:
    def __init__(self, destination: str):
        self.destination = destination
        self.create_at = datetime.now()
