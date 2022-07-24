from flask_restx import Namespace, Resource

from project.container import movie_service
from project.setup.api.models import movie
from project.setup.api.parsers import page_parser

api = Namespace('movies')


@api.route('/')
class MoviesView(Resource):
    @api.expect(page_parser)
    @api.marshal_with(movie, as_list=True, code=200, description='OK')
    def get(self):
        return movie_service.get_all(**page_parser.parse_args()), 200


@api.route('/<int:mid>/')
class MovieView(Resource):
    @api.marshal_with(movie, code=200, description='OK')
    def get(self, mid: int):
        return movie_service.get_by_id(mid), 200
