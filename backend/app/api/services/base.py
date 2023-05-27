from app.core.repositories.base import BaseRepository


class Service:
    def __init__(self, repository: BaseRepository):
        self.repository = repository