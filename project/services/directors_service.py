from project.dao.base import BaseDAO
from project.exceptions import ItemNotFound
from project.models import Director


class DirectorsService:
    def __init__(self, dao: BaseDAO) -> None:
        self.dao = dao

    def get_by_id(self, did: int) -> Director:
        if director := self.dao.get_by_id(did):
            return director
        else:
            raise ItemNotFound(f'Director with did={did} not exists.')

    def get_all(self, **kwargs) -> list[Director]:
        return self.dao.get_all(page=kwargs["page"])
