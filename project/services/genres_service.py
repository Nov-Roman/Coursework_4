from project.dao.base import BaseDAO
from project.exceptions import ItemNotFound
from project.models import Genre


class GenresService:
    def __init__(self, dao: BaseDAO) -> None:
        self.dao = dao

    def get_by_id(self, pk: int) -> Genre:
        if genre := self.dao.get_by_id(pk):
            return genre
        else:
            raise ItemNotFound(f'Genre with pk={pk} not exists.')

    def get_all(self, **kwargs) -> list[Genre]:
        return self.dao.get_all(page=kwargs["page"])
