from handlers.base_rest_handler import BaseRestHandler
from .schemas import AGGREGATE_NUMBERS_POST_REQUEST_SCHEMA

from services import aggregate_telephone_numbers

from jsonschema import validate, ValidationError

import json
from http import HTTPStatus



class AggregateNumbersHandler(BaseRestHandler):
    def post(self):
        request_body = self.get_body_as_json()
        if request_body is not None:
            try:
                validate(instance=request_body, schema=AGGREGATE_NUMBERS_POST_REQUEST_SCHEMA)
                # From now on we can assume that request_body is a list of strings
                response = aggregate_telephone_numbers(request_body)
                self.write(response)
            except ValidationError:
                self.set_status(HTTPStatus.BAD_REQUEST)
                self.write({"error": "The body of the request has to be a list of strings"})
