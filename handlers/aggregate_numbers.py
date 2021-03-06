from handlers.base_rest_handler import BaseRestHandler
from jsonschema import validate, ValidationError

from http import HTTPStatus

from services import aggregate_telephone_numbers_trie
from .schemas import *


class AggregateNumbersHandler(BaseRestHandler):
    def post(self):
        request_body = self.get_body_as_json()
        if request_body is not None:
            try:
                validate(instance=request_body, schema=AGGREGATE_NUMBERS_POST_REQUEST_SCHEMA)
                # From now on we can assume that request_body is a list of strings
                response = aggregate_telephone_numbers_trie(request_body)
                if response.get("error"):
                    self.set_status(HTTPStatus.SERVICE_UNAVAILABLE)
                self.write(response)
            except ValidationError:
                self.set_status(HTTPStatus.BAD_REQUEST)
                self.write({"error": "The body of the request has to be a list of strings"})
