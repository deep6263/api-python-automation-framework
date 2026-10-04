import requests
from utils.logger import logger
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

class BaseApiClient:
    """Reusable HTTP client for API automation."""

    def __init__(self, base_url: str):
        self.base_url = base_url.rstrip("/")
        retry_strategy = Retry(
            total=2,
            connect=2,
            read=2,
            backoff_factor=0.5,
            allowed_methods={"GET"},
        )

        adapter = HTTPAdapter(max_retries=retry_strategy)

        self.session = requests.Session()
        self.session.mount("https://", adapter)
        self.session.mount("http://", adapter)

    def get(self, endpoint: str, **kwargs):
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        logger.info(f"GET {url}")

        response = self.session.get(url, **kwargs)

        logger.info(
            f"GET {url} -> {response.status_code} "
            f"({response.elapsed.total_seconds():.2f}s)"
        )

        return response

    def post(self, endpoint: str, **kwargs):
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        logger.info(f"POST {url}")

        response = requests.post(url, **kwargs)

        logger.info(
            f"POST {url} -> {response.status_code} "
            f"({response.elapsed.total_seconds():.2f}s)"
        )

        return response

    def put(self, endpoint: str, **kwargs):
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        logger.info(f"PUT {url}")

        response = requests.put(url, **kwargs)

        logger.info(
            f"PUT {url} -> {response.status_code} "
            f"({response.elapsed.total_seconds():.2f}s)"
        )

        return response

    def patch(self, endpoint: str, **kwargs):
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        logger.info(f"PATCH {url}")

        response = requests.patch(url, **kwargs)

        logger.info(
            f"PATCH {url} -> {response.status_code} "
            f"({response.elapsed.total_seconds():.2f}s)"
        )

        return response

    def delete(self, endpoint: str, **kwargs):
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        logger.info(f"DELETE {url}")

        response = requests.delete(url, **kwargs)

        logger.info(
            f"DELETE {url} -> {response.status_code} "
            f"({response.elapsed.total_seconds():.2f}s)"
        )
        return response