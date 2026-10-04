from jsonschema import validate


def validate_schema(response_data: dict, schema: dict) -> None:
    """Validate API response data against a JSON schema."""
    validate(instance=response_data, schema=schema)