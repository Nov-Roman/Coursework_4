from project.dao.base import BaseDAO
from project.exceptions import ItemNotFound
from project.models import Movie


class MoviesService:
    def __init__(self, dao: BaseDAO) -> None:
        self.dao = dao

    def get_by_id(self, mid: int) -> Movie:
        if movie := self.dao.get_by_id(mid):
            return movie
        else:
            raise ItemNotFound(f'Movie with mid={mid} not exists.')

    def get_all(self, **kwargs) -> list[Movie]:
        return self.dao.get_all(**kwargs)
