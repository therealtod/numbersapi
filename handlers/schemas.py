AGGREGATE_NUMBERS_POST_REQUEST_SCHEMA = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "array",
    "items": {
        "type": "string"
        }
    }

AGGREGATE_NUMBERS_POST_RESPONSE_SCHEMA = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "additionalProperties": {
        "type": "object",
        "additionalProperties": {
            "type": "number"
            }
        }
}
