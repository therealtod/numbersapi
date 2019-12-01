from tornado.testing import AsyncHTTPTestCase
from jsonschema import validate

import json
from http import HTTPStatus

from main import make_app
from .schemas import AGGREGATE_NUMBERS_POST_RESPONSE_SCHEMA


class TestHandler(AsyncHTTPTestCase):
    def get_app(self):
        return make_app()


class TestAPIHandler(TestHandler):
    def get_post_response(self, request_body):
        url = self.get_app().reverse_url("aggregate")
        response = self.fetch(
            url,
            method="POST",
            body=json.dumps(request_body))
        return response

    def test_get_not_allowed(self):
        url = self.get_app().reverse_url("aggregate")
        response = self.fetch(
            url,
            method="GET"
        )
        self.assertEqual(response.code, HTTPStatus.METHOD_NOT_ALLOWED)

    def test_post_wrong_schema_not_allowed1(self):
        # An empty json is not allowed
        response = self.get_post_response({})
        self.assertEqual(response.code, HTTPStatus.BAD_REQUEST)

    def test_post_wrong_schema_not_allowed2(self):
        # A non-empty object is not allowed
        response = self.get_post_response({"some-content": "here"})
        self.assertEqual(response.code, HTTPStatus.BAD_REQUEST)

    def test_post_wrong_schema_not_allowed3(self):
        # A list of numbers is not allowed
        response = self.get_post_response([1, 2, 3])
        self.assertEqual(response.code, HTTPStatus.BAD_REQUEST)

    def test_post_OK(self):
        # A list of strings is ok
        response = self.get_post_response(["a string", "another string"])
        self.assertEqual(response.code, HTTPStatus.OK)

    def test_post_reponse_is_json(self):
        response = self.get_post_response({})
        self.assertEqual(response.headers.get("Content-Type"), "application/json; charset=UTF-8")

    def test_response_schema(self):
        response = self.get_post_response(["+13454787"])
        validate(instance=json.loads(response.body), schema=AGGREGATE_NUMBERS_POST_RESPONSE_SCHEMA)
