def assert_response_time(response, max_seconds: float = 5.0) -> None:
    """Assert that an API response is returned within the allowed time."""
    elapsed = response.elapsed.total_seconds()

    assert elapsed < max_seconds, (
        f"Response took {elapsed:.2f}s, "
        f"which exceeds the limit of {max_seconds:.2f}s"
    )