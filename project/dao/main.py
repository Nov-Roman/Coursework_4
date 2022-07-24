from project.dao.base import BaseDAO
from project.models import Genre, Director, User, Movie 


class GenresDAO(BaseDAO[Genre]):
    __model__ = Genre


class DirectorsDAO(BaseDAO[Director]):
    __model__ = Director


class UsersDAO(BaseDAO[User]):
    __model__ = User


class MoviesDAO(BaseDAO[Movie]):
    __model__ = Movie


class AuthDAO(BaseDAO[User]):
    __model__ = User